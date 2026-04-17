# Efficiency
- In low-batch AI inference, FPGAs are the least efficient compared to GPUs
- Modern GPUs have customized hardware for AI inference
	- Tensor cores
	- Customized data types: FP16 INT8 INT4
- But is hardware optimization for matmul enough?
- Combine FPGA with tensor cores
	- AI engines
	- Versal FPGA + AI engine is significantly more efficient than GPU
# FPGA+AIE
- AI Engines provide high frequency 3D-SIMD vector processors
	- Reduced inst and control overhead
- Up to 100MB on-chip RAMs
- >20TB/s on-chip bandwidth at 250mhz
- Explicit dataflow and concurrency
	- Allows user customization to avoid cache misses and coherence overhead
	- From the FPGA's customizability

# Workloads
- Large MatMul
	- Large workload can be easily distributed
	- Data reuse allows computation to be sustained and communication overlapped
- Small matmul
	- Require padding 
	- Heavily underutilizes resources
	- One-size-for-all data reuse/parallelism is not optimal
## Diverse Non-Linear Kernels
### Layer Norm
- Require 3 traversals of memory
-  