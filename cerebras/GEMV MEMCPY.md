Continues [[CSL GEMV Program]] [[Memory DSDs]]
# Overview
- Previously, A x and b were initialized on the device
- Now, we will initialize them on the host and transfer them to the device using `memcpy_h2d`
- The program has 3 phases
	- Host copies input data to device
	- Device computes y
	- Host copies y from device
- Orchestration
	- The host controls everything
	- Before or after calling a device function, the host has control of the command stream
	- It can copy in and out all it wants
# Memcpy Function Args
- For both h2d and d2h the args are the same
- 1. Exported symbol on device
- 2. Buffer on host
- 3 & 4: NW corner of ROI
- 5 & 6: Row and column size of ROI
- 7: Number of elements to copy
- Streaming
- Order
- Data Type
- Non blocking
# Host Code Example
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
A = np.arange(M*N, dtype=np.float32)
x = np.full(shape=N, fill_value=1.0, dtype=np.float32)
b = np.full(shape=M, fill_value=2.0, dtype=np.float32)

# Calculate expected y
y_expected = A.reshape(M,N)@x + b

# Construct a runner using SdkRuntime
runner = SdkRuntime(args.name, cmaddr=args.cmaddr)

# Get symbols for A, b, x, y on device
A_symbol = runner.get_id('A')
x_symbol = runner.get_id('x')
b_symbol = runner.get_id('b')
y_symbol = runner.get_id('y')

# Load and run the program
runner.load()
runner.run()

# Copy A, x, b to device
runner.memcpy_h2d(A_symbol, A, 0, 0, 1, 1, M*N, streaming=False,
  order=MemcpyOrder.ROW_MAJOR, data_type=MemcpyDataType.MEMCPY_32BIT, nonblock=False)
runner.memcpy_h2d(x_symbol, x, 0, 0, 1, 1, N, streaming=False,
  order=MemcpyOrder.ROW_MAJOR, data_type=MemcpyDataType.MEMCPY_32BIT, nonblock=False)
runner.memcpy_h2d(b_symbol, b, 0, 0, 1, 1, M, streaming=False,
  order=MemcpyOrder.ROW_MAJOR, data_type=MemcpyDataType.MEMCPY_32BIT, nonblock=False)

# Launch the init_and_compute function on device
runner.launch('init_and_compute', nonblock=False)

# Copy y back from device
y_result = np.zeros([M], dtype=np.float32)
runner.memcpy_d2h(y_result, y_symbol, 0, 0, 1, 1, M, streaming=False,
  order=MemcpyOrder.ROW_MAJOR, data_type=MemcpyDataType.MEMCPY_32BIT, nonblock=False)

# Stop the program
runner.stop()

# Ensure that the result matches our expectation
np.testing.assert_allclose(y_result, y_expected, atol=0.01, rtol=0)
print("SUCCESS!")
```