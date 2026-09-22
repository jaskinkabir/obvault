Continues [[GEMV MEMCPY]] [[Memory DSDs]] [[CSL GEMV Program]]
Continued by [[Routing and Fabric DSDs]]
# Overview
- We will modify our code to run the GEMV operation on a row of 4 PEs.
- We do not need to modify the PE code, just the layout
- 
# Modifying the Layout
- Can use for loop to assign code to PEs
```c
param M: i16;

param N: i16;

param width: i16;

// Import memcpy layout module for 1 x 1 grid of PEs

// This module defines parameters passed to program on the single PE

const memcpy = @import_module("<memcpy/get_params>", .{

    .width = width,

     .height = 1 });

  

layout {

  

  // Use just one 1 PE (columns=1, rows=1)

  @set_rectangle(width, 1);

  

  for (@range(i16, width)) |i| {

    @set_tile_code(i, 0, "gemv_pe.csl", .{

      .memcpy_params = memcpy.get_params(i),

      .M = M,

      .N = N

    });

  }

  

  // Export device symbol for array "y"

  // Last argument is mutability: host can read y, but not write to it

  @export_name("y", [*]f32, false);

  @export_name("A", [*]f32, true);

  @export_name("x", [*]f32, true);

  @export_name("b", [*]f32, true);

  

  // Export host-callable device function

  @export_name("init_and_compute", fn()void);

}
```
# Memcpy Broadcast
- Memcpy does not have broadcast
- Use `np.tile()` to copy the host buffer data into a buffer with the same dimensions as the PE rectangle