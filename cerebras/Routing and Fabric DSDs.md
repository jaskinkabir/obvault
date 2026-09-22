Continues [[Multiple PEs]]

# Overview
- We will split the gemv task among multiple PEs
- Copy b into the left PE's y array
- Copy the left half of A's columns into the left PE and the right half into the right PE
- Copy the first N/2 elements of x into the left PE, and the last N/2 into the right PE
- Each PE will then compute Ax for its local pieces of A and x. Both PEs compute the gemv for an MxN/2 matrix. The PEs increment their local y arrays by this amount.
- Then the left PE sends its y array to the right PE, and the right PE adds this to its local y array
- The final summed y array on the right PE is our GEMV result

# Cerebras Routing
- The router of each PE has five directions
	- RAMP, NORTH, EAST, SOUTH, WEST
	- The cardinal directions refer to neightbords
	- ramp refers to the connection between the PE's router and its compute element (CE)
- Directions are from the perspective of the router, thus receiving from RAMP means receiving data pushed from the CE
# Layout Code
```c
// matrix dimensions on each PE
param M: i16;
param N: i16;

// Colors
const send_color: color = @get_color(0); // Color used to send/recv data between PEs

// This example only uses 2 PEs
const memcpy = @import_module("<memcpy/get_params>", .{
  .width = 2,
  .height = 1,
});

layout {
  // PE coordinates are (column, row)
  @set_rectangle(2, 1);

  // Left PE (0, 0)
  @set_tile_code(0, 0, "pe_program.csl", .{
    .memcpy_params = memcpy.get_params(0),
    .M = M,
    .N_per_PE = N / 2,
    .pe_id = 0,
    .send_color = send_color
  });

  // Left PE sends its result to the right
  @set_color_config(0, 0, send_color, .{.routes = .{ .rx = .{RAMP}, .tx = .{EAST} }});

  // Right PE (1, 0)
  @set_tile_code(1, 0, "pe_program.csl", .{
    .memcpy_params = memcpy.get_params(1),
    .M = M,
    .N_per_PE = N / 2,
    .pe_id = 1,
    .send_color = send_color
  });

  // Right PE receives result of left PE
  @set_color_config(1, 0, send_color, .{.routes = .{ .rx = .{WEST}, .tx = .{RAMP} }});

  // export symbol names
  @export_name("A", [*]f32, true);
  @export_name("x", [*]f32, true);
  @export_name("y", [*]f32, true);
  @export_name("compute", fn()void);
}
```
# PE Code
```c
param memcpy_params;

// Matrix dimensions
param M: i16;
param N_per_PE: i16;

// ID of PE (0 is left, 1 is right)
param pe_id: i16;

// Colors
param send_color: color; // Color used to send/recv data between PEs

// Queue IDs
const send_color_oq = @get_output_queue(2);
const send_color_iq = @get_input_queue(2);

// Task ID used by a local task to unblock cmd stream
const exit_task_id: local_task_id = @get_local_task_id(9);

// memcpy module provides infrastructure for copying data
// and launching functions from the host
const sys_mod = @import_module("<memcpy/memcpy>", memcpy_params);

// 48 kB of global memory contain A, x, y
var A: [M*N_per_PE]f32; // A is stored column major
var x: [N_per_PE]f32;
var y: [M]f32;

// DSDs for accessing A, b, y
// A_dsd accesses column of A
var A_dsd = @get_dsd(mem1d_dsd, .{ .base_address = &A, .extent = M });
var y_dsd = @get_dsd(mem1d_dsd, .{ .base_address = &y, .extent = M });

// ptrs to A, x, b, y will be advertised as symbols to host
var A_ptr: [*]f32 = &A;
var x_ptr: [*]f32 = &x;
var y_ptr: [*]f32 = &y;

// Compute gemv
fn gemv() void {
  // Loop over all columns of A
  for (@range(i16, N_per_PE)) |i| {
    // Calculate contribution to A*x from ith column of A, ith elem of x
    @fmacs(y_dsd, y_dsd, A_dsd, x[i]);
    // Move A_dsd to next column of A
    A_dsd = @increment_dsd_offset(A_dsd, M, f32);
  }
}

fn send_right() void {
  const out_dsd = @get_dsd(fabout_dsd, if (@is_arch("wse3")) .{
                    .extent = M, .output_queue = send_color_oq
                  } else .{
                    .fabric_color = send_color, .extent = M,
                    .output_queue = send_color_oq
                  });
  // After fmovs is done, activate exit_task to unblock cmd_stream
  @fmovs(out_dsd, y_dsd, .{ .async = true, .activate = exit_task_id });
}

fn recv_left() void {
  const in_dsd = @get_dsd(fabin_dsd, .{
                   .extent = M,
                   .input_queue = send_color_iq
                 });
  // After fadds is done, activate exit_task to unblock cmd stream
  @fadds(y_dsd, y_dsd, in_dsd, .{ .async = true, .activate = exit_task_id });
}

// Call gemv function and send/ receive partial result y
fn compute() void {
  gemv();
  if (pe_id == 0) {
    send_right();
  } else {
    recv_left();
  }
}

task exit_task() void {
  sys_mod.unblock_cmd_stream();
}

comptime {
  // When exit_task_id is activated, exit_task will execute
  @bind_local_task(exit_task, exit_task_id);

  // On WSE-3, we must explicitly bind the output queue to a color.
  // Input queues must be bound to a color on both architectures.
  @initialize_queue(send_color_oq, if (@is_arch("wse3")) .{ .color = send_color } else .{});
  @initialize_queue(send_color_iq, .{ .color = send_color });

  @export_symbol(A_ptr, "A");
  @export_symbol(x_ptr, "x");
  @export_symbol(y_ptr, "y");
  @export_symbol(compute);
}
```
- `A` is now stored in column-major order to make data movement easier.
## Fabric DSDs and Async Ops
- The compute function first calls gemv to compute local contribution to y
- The left PE calls send_right, while the left PE calls recv_left
- `send_right` defines a `fabout_dsd`, which is used to send wavelets to the fabric along the color send_color.
	- We give this `fabout_dsd` the extent `M` since we will send `M` elements along the fabric
	- On WSE-3, a fabric DSD is bound to a color indirectly via its queue, so its `.fabric_color` is omitted from the dsd 
	- On WSE-2, the color is specified directly on the dsd
- The `@fmvovs` operation copies the `M` elements accessed by `y_dsd` into `out_dsd`
- The operation is asynchronous and activates the `exit_task` function by specifying a local task id, which is bound to the `exit_task_id` variable at compile time.
- `recv_left` defines a fabin_dsd to receive wavelents sent along `send_color`
	- The `@fadds` operation increments the right PE's y_dsd by the elements received in `in_dsd`
	- After this operation, `y_dsd` containst he final GEMV result. This builtin also executes asynchronously, and activates the exit task upon completion
# Async Fabric builtin
- Using fabric DSDs in builtin operations should also use async
- Otherwise it can be slow or even lockup
# Host Code
```python
#!/usr/bin/env cs_python

import argparse
import json
import numpy as np

from cerebras.sdk.runtime.sdkruntimepybind import SdkRuntime, MemcpyDataType, MemcpyOrder # pylint: disable=no-name-in-module

# Read arguments
parser = argparse.ArgumentParser()
parser.add_argument('--name', help="the test compile output dir")
parser.add_argument('--cmaddr', help="IP:port for CS system")
args = parser.parse_args()

# Get matrix dimensions from compile metadata
with open(f"{args.name}/out.json", encoding='utf-8') as json_file:
  compile_data = json.load(json_file)

# Matrix dimensions
N = int(compile_data['params']['N'])
M = int(compile_data['params']['M'])

# Construct A, x, b
A = np.arange(M*N, dtype=np.float32).reshape(M,N)
x = np.full(shape=N, fill_value=1.0, dtype=np.float32)
b = np.full(shape=M, fill_value=2.0, dtype=np.float32)

# Calculate expected y
y_expected = A@x + b

# Size of N dimension on each PE
N_per_PE = N // 2

# Construct a runner using SdkRuntime
runner = SdkRuntime(args.name, cmaddr=args.cmaddr)

# Get symbols for A, x, y on device
A_symbol = runner.get_id('A')
x_symbol = runner.get_id('x')
y_symbol = runner.get_id('y')

# Load and run the program
runner.load()
runner.run()

# Copy b into y of PE (0, 0)
runner.memcpy_h2d(y_symbol, b, 0, 0, 1, 1, M, streaming=False,
  order=MemcpyOrder.ROW_MAJOR, data_type=MemcpyDataType.MEMCPY_32BIT, nonblock=False)

# Copy A in column major format
# PE (0, 0) gets first N/2 columns; PE (1, 0) gets last N/2 columns
runner.memcpy_h2d(A_symbol, A.transpose().ravel(), 0, 0, 2, 1, M*N_per_PE, streaming=False,
  order=MemcpyOrder.ROW_MAJOR, data_type=MemcpyDataType.MEMCPY_32BIT, nonblock=False)

# PE (0, 0) gets first N/2 elements; PE (1, 0) gets last N/2 elements
runner.memcpy_h2d(x_symbol, x, 0, 0, 2, 1, N_per_PE, streaming=False,
  order=MemcpyOrder.ROW_MAJOR, data_type=MemcpyDataType.MEMCPY_32BIT, nonblock=False)

# Launch the compute function on device
runner.launch('compute', nonblock=False)

# Copy y back from PE (1, 0)
y_result = np.zeros([M], dtype=np.float32)
runner.memcpy_d2h(y_result, y_symbol, 1, 0, 1, 1, M, streaming=False,
  order=MemcpyOrder.ROW_MAJOR, data_type=MemcpyDataType.MEMCPY_32BIT, nonblock=False)

# Stop the program
runner.stop()

# Ensure that the result matches our expectation
np.testing.assert_allclose(y_result, y_expected, atol=0.01, rtol=0)
print("SUCCESS!")
```
- Notice that copying A is done with one single h2d copy
- The ROI is both PEs, and they each only take N/2 elements from the array
- Same for X