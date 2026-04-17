# Why Aries
Existing AI engine programming tools suffered in these ways
1. Limited support for multilayer applications
	1. Past studies focus on accelerating specific kernels like matmuls
	2. Extending designs to support more complex applications is difficult
	3. No attention given to workload partitioning between heterogenous components or inter-layer communication
2. Fragmented Abstraction for Multi-Level Parallelism
	1. Existing frameworks abstract AIE arch with dataflow model
	2. Exploits task-level parallelism but not tile-level within the task
	3. Must assign kernels manually to tiles
	4. Manually coordinate data transfer
3. Limited support for automation and optimization
	1. Rely on users to provicde optimized dataflow, inter-tile data movement scheme, and vectorization
	2. Manual config is required to establish connections between PL and AIE
4. Portability
	1. Existing works focus on either Ryzen NPU or Versal style architectures, but not both
	2. No portable solution exists yet
# Major ARIES Contributions
- Tile level programing
- Mpa task tiles across cores without code restructuring
- Declarative scheduling primitives
- Unified MLIR for AIE core, AIE graph, and PL
- By extending lightweight code generator backends, the same source code can be used for both Versal ACAP and Ryzen NPU
