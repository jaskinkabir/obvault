# CSL
Continued by [[Memory DSDs]]
- Based on Zig
	- Compile-time facilities allow maintanable and performant code
- Supports if while and for
## Types
- Has bool, signed and unsigned and floats 16 and 32 bits
	- bool
	- i16 and i32
	- u16 and u32
	- f16 and f32
- Also has arrays and pointers for these types
## Functions
- Declared using `fn` keyword
- Builtin functions start with `@` symbol
# GEMV Basic Example
- Computes general matrix vector product y=Ax + b
	- A is MxN matrix
	- y, and b are M vectors
	- x is an N vector
```C
// Not a complete program; we include it here for illustrating some syntax

// Every variable must be declared either "const" or "var"
// Const cannot be modified after declaration, but var can

// Constants defining dimensions of our matrix
const M: i16 = 4;
const N: i16 = 6;

// 48 kB of global memory contain A, x, b, y
var A: [M*N]f32; // A is stored in row-major order
var x: [N]f32;
var b: [M]f32;
var y: [M]f32;

// Initialize matrix and vectors
fn initialize() void {
  // for loop with range syntax
  // loops over 0, 1, ...., M*N-1
  // idx stores the loop index
  for (@range(i16, M*N)) |idx| {
    // @as casts idx from i16 to f32
    A[idx] = @as(f32, idx);
  }

  for (@range(i16, N)) |j| {
    x[j] = 1.0;
  }

  // while loop with iterator syntax
  var i: i16 = 0;
  while (i < M) : (i += 1) {
    b[i] = 2.0;
    y[i] = 0.0;
  }
}

// Compute gemv
fn gemv() void {
  for (@range(i16, M)) |i| {
    var tmp: f32 = 0.0;
    for (@range(i16, N)) |j| {
      tmp += A[i*N + j] * x[j];
    }
    y[i] = tmp + b[i];
  }
}

// Call initialize and gemv functions
fn init_and_compute() void {
  initialize();
  gemv();
}
```

## The Layout File
```c
// Import memcpy layout module for 1 x 1 grid of PEs
// This module defines parameters passed to program on the single PE
const memcpy = @import_module("<memcpy/get_params>", .{ .width = 1, .height = 1 });

layout {

  // Use just one 1 PE (columns=1, rows=1)
  @set_rectangle(1, 1);

  // The lone PE in this program should execute the code in "pe_program.csl"
  // We pass memcpy parameters as a parameter to the program. Note that
  // memcpy parameters are parameterized by the PE's column number.
  @set_tile_code(0, 0, "pe_program.csl", .{ .memcpy_params = memcpy.get_params(0) });

  // Export device symbol for array "y"
  // Last argument is mutability: host can read y, but not write to it
  @export_name("y", [*]f32, false);

  // Export host-callable device function
  @export_name("init_and_compute", fn()void);
}
```
- Uses memcpy module
	- In csl, importing a module requires params
	- Creates a struct from those params
	- In the example, we use a 1x1 grid of pes
- Describes which PEs will be used
	- `@set_rectangle(rows, cols)`
		- Sets the size of the PE rectangle
		- Does not define coordinates of PE I think
	- `@set_tile_code`
		- Has coordinates of pe in pe rectangle
		- memcpy parameters are parametrized by the PE's col number
- Making symbols (vars/functions) available to the host from the PE requires the `@export_name` function
## Add memcpy to GEMV
```c
// Struct containing parameters for memcpy layout
param memcpy_params;

// memcpy module provides infrastructure for copying data
// and launching functions from the host
const sys_mod = @import_module("<memcpy/memcpy>", memcpy_params);

// Constants definining dimensions of our matrix
const M: i16 = 4;
const N: i16 = 6;

// 48 kB of global memory contain A, x, b, y
var A: [M*N]f32; // A is stored row major
var x: [N]f32;
var b: [M]f32;
var y: [M]f32;

// Ptr to y will be exported as symbol to host
// Ptr is const, so host can read but not write to y
const y_ptr: [*]f32 = &y;

// Initialize matrix and vectors
fn initialize() void {
  // for loop with range syntax
  for (@range(i16, M*N)) |idx| {
    A[idx] = @as(f32, idx);
  }

  for (@range(i16, N)) |j| {
    x[j] = 1.0;
  }

  // while loop with iterator syntax
  var i: i16 = 0;
  while (i < M) : (i += 1) {
    b[i] = 2.0;
    y[i] = 0.0;
  }
}

// Compute gemv
fn gemv() void {
  for (@range(i16, M)) |i| {
    var tmp: f32 = 0.0;
    for (@range(i16, N)) |j| {
      tmp += A[i*N + j] * x[j];
    }
    y[i] = tmp + b[i];
  }
}

// Call initialize and gemv functions
fn init_and_compute() void {
  initialize();
  gemv();

  // After this function finishes, memcpy's cmd_stream must
  // be unblocked on all PEs for further memcpy commands
  // to execute
  sys_mod.unblock_cmd_stream();
}

comptime {
  // Export symbol pointing to y so it is host-readable
  @export_symbol(y_ptr, "y");

  // Export function so it is host-callable by RPC mechanism
  @export_symbol(init_and_compute);
}
```
- Program requires memcpy params from layout file
- Import memcpy module using memcpy params from layout at beginning
- Declare a const ptr to the y variable, which will be exported to the host
### Yielding control
- In order for the memcpy operation to be able to touch the PE's memory, the PE's program must yield control
- This is done with the `unblock_cmd_stream()` function
- **MUST BE CALLED AT END OF PROGRAM**
### Exporting Symbols
- The symbols `y_ptr` and `init_and_compute` must be exported to the layout file at compile time
- This is done using the `comptime {}` block
## Compilation
- Use command `cslc layout.csl --fabric-dims=8,3 --fabric-offsets=4,1 --memcpy --channels=1 -o out`
- Note that the fabric must have an offset of (4,1)
	-  and a fabric dimension of `width+7, height+1` where width and height are dimensions of the program
	- Memcpy uses additional PEs to route data to and from the wafer
- Channels
	- Use 1 channel for the memcpy
	- Can use up to the height of the program or 16, whichever is smaller
	- Improvements past 8 are minimal
## Host Code
```python
#!/usr/bin/env cs_python

import argparse
import numpy as np

from cerebras.sdk.runtime.sdkruntimepybind import SdkRuntime, MemcpyDataType, MemcpyOrder # pylint: disable=no-name-in-module

# Read arguments
parser = argparse.ArgumentParser()
parser.add_argument('--name', help="the test compile output dir")
parser.add_argument('--cmaddr', help="IP:port for CS system")
args = parser.parse_args()

# Matrix dimensions
M = 4
N = 6

# Construct A, x, b
A = np.arange(M*N, dtype=np.float32).reshape(M, N)
x = np.full(shape=N, fill_value=1.0, dtype=np.float32)
b = np.full(shape=M, fill_value=2.0, dtype=np.float32)

# Calculate expected y
y_expected = A@x + b

# Construct a runner using SdkRuntime
runner = SdkRuntime(args.name, cmaddr=args.cmaddr)

# Get symbol for copying y result off device
y_symbol = runner.get_id('y')

# Load and run the program
runner.load()
runner.run()

# Launch the init_and_compute function on device
runner.launch('init_and_compute', nonblock=False)

# Copy y back from device
# Arguments to memcpy_d2h:
# - y_result is array on host which will story copied-back array
# - y_symbol is symbol of device tensor to be copied
# - 0, 0, 1, 1 are (starting x-coord, starting y-coord, width, height)
#   of rectangle of PEs whose data is to be copied
# - M is number of elements to be copied from each PE
y_result = np.zeros([1*1*M], dtype=np.float32)
runner.memcpy_d2h(y_result, y_symbol, 0, 0, 1, 1, M, streaming=False,
  order=MemcpyOrder.ROW_MAJOR, data_type=MemcpyDataType.MEMCPY_32BIT, nonblock=False)

# Stop the program
runner.stop()

# Ensure that the result matches our expectation
np.testing.assert_allclose(y_result, y_expected, atol=0.01, rtol=0)
print("SUCCESS!")
```
### ARGS
- Name arg is passed to the sdk runtime instance
	- Creates output folder and populates with runtime data
- CMDADDR:
	- Real wafer engines are network-attached accelerators
	- This address is the actual ip of the accelerator
	- 
### Memcpy D2H
- This function has many args. In order they are:
	- Allocated host dest buffer
	- Exported symbol from device
	- Northwest corner of rectangle of PEs from which to copy (called Region of Interest ROI)
	- Width and height of ROI
	- How many elements to copy from each PE in the ROI


For topic #cerebras