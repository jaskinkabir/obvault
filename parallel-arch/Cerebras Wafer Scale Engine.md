# Architecture
- ![[Pasted image 20260504201525.png]]
- 2d grid of PEs
- Each PE is directly connected to up to 4 neighbors
- The PE includes a processor, 48kb memory, and a Fabric Router
- Cores
	- Arithmetic precisions (fp): FP32, FP16, BF16, FP8, mixed
	- Each core has SIMD capabilities
- Single cycle local memory access
- 1 cycle to move 32 bits of data between PEs
	- 2 cycle per hop across the grid (1 to router 1 to processor)
- There is no global memory and no caches, it is distributed system on a chip
# Comparison against GPU
![[Pasted image 20260504202023.png]]
![[Pasted image 20260504203752.png]]
## Synchronization Example
![[Pasted image 20260504203836.png]]

# Programming
## Host-Device Communication
- Two modes
	- GPU-like
		- Host invokes input DMA
		- Host invokes kernel
		- Host invokes output DMA
	- Tensor streaming
		- Host invokes host-device copies in streaming mode
		- Special tasks on device activated by incoming data
		- Data transfer and computation overlap
- First and last columns of PEs are dedicated to memory transfer between host and device
## What Code Goes on the Device
- Device configuration
	- Configure the program executed by each PE
		- Every PE can execute different code
	- Configures routers (virtual channels)
- Kernel code
	- Computation performed by PEs
- Compilation/device configuration can take minutes
## Device Configuration
- Layout file
- ![[Pasted image 20260504204651.png]]
- 

For class #parallel-arch 