Continues [[CSL GEMV Program]]
Continued by [[GEMV MEMCPY]]
# Memory Data Structure Descriptor
- Performs efficient tensor operations in CSL without explicit loops
# Modifying GEMV for DSD
```c
param memcpy_params;

// memcpy module provides infrastructure for copying data
// and launching functions from the host
const sys_mod = @import_module("<memcpy/memcpy>", memcpy_params);

// Constants definining dimensions of our matrix
const M: i16 = 4;
const N: i16 = 6;

// 48 kB of global memory contain A, x, b, y
var A: [M*N]f32; // A is stored row major

// Initialize x, b, y using builtins
var x = @constants([N]f32, 1.0);
var b = @constants([M]f32, 2.0);
var y = @zeros([M]f32);

// DSDs for accessing A, b, y
// b_dsd uses tensor access expression to specify access to M consecutive elements of b
var b_dsd = @get_dsd(mem1d_dsd, .{ .tensor_access = |i|{M} -> b[i] });
// The above expression is equivalent to:
// var b_dsd = @get_dsd(mem1d_dsd, .{ .base_address = &b, .extent = M });

// y_dsd uses base_address and extent fields to specify access to M consecutive elements of y
var y_dsd = @get_dsd(mem1d_dsd, .{ .base_address = &y, .extent = M });
// The above expression is equivalent to:
// var y_dsd = @get_dsd(mem1d_dsd, .{ .tensor_access = |i|{M} -> y[i] });

// A_dsd accesses column of A
// A_dsd uses tensor access expression to specify access to every Nth element of A
var A_dsd = @get_dsd(mem1d_dsd, .{ .tensor_access = |i|{M} -> A[i*N] });
// The above expression is equivalent to:
// var A_dsd = @get_dsd(mem1d_dsd, .{ .base_address = &A, .extent = M, .stride = N });

// ptr to y will be advertised as symbol to host
const y_ptr: [*]f32 = &y;

// Initialize A matrix
fn initialize() void {
  // for loop with range syntax
  for (@range(i16, M*N)) |idx| {
    A[idx] = @as(f32, idx);
  }
}

// Compute gemv
fn gemv() void {
  // Loop over all columns of A
  for (@range(u16, N)) |i| {
    // Calculate contribution to A*x from ith column of A, ith elem of x
    @fmacs(y_dsd, y_dsd, A_dsd, x[i]);
    A_dsd = @increment_dsd_offset(A_dsd, 1, f32);
  }
  // Add b to A*x
  @fadds(y_dsd, y_dsd, b_dsd);
}

// Call initialize and gemv functions
fn init_and_compute() void {
  initialize();
  gemv();
  sys_mod.unblock_cmd_stream();
}

comptime {
  @export_symbol(y_ptr, "y");
  @export_symbol(init_and_compute);
}
```
- Initialize x b and y using builtin constant array constructors like np.zeros
## Declaring 1D DSDs
- Declare a dsd with `@get_dsd`
	- Specify dimensionality of data in memory
	- Base_address specifies access to specify access to consecutive elements
	- `-base_address = &y, .extent = M` says starting at base address of y, access M consecutive elements
	- Tensor access parameter creates a mapping from index i to element of array
		- `|i|{M} -> b[i]` says index i has max value m and corresponds to direct memory offset of b
		- `|i|{M*N} -> A[i*N]` says incrementing i accesses every Nth element of A
			- Equivalent to base_address declaration with stride of N
- The access pattern allows for `extent` accesses in total before the offset is incremented
- For A, we have an extent of `M` and a stride of `N`
	- This means that, upon initialization, A_dsd is presented as a vector containing the first column of A
	- This is because of the stride of N, which makes `A_dsd[i+1] = A[(i+1)*N]`
## DSD Operations
- The `@fmacs` function is called with `@fmacs(y_dsd, y_dsd, A_dsd, x[i]);
	-  performs a vector-scalar multiplication between the column of A referenced by A_dsd and the scalar 
	- Performs elementwise vector addition between this result and the vector y
	- Stores the result into y
	- The arguments to the fmacs function are: dest, accumulate, mul, mul
	- Thus, each fmacs operation increments the M elements of y by the vector-scalar product of column i of A and element i of x
- The `@increment_dsd_offset` increments A_dsd to reference the next column of A. It takes A_dsd and creates a new DSD by offsetting its access by 1 f32 element.
- The final `@fadds` operation does elementwise vector addition between y and b, storing the result in y
- 

For topic #cerebras 