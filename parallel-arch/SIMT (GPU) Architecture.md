Continues [[Parallelism and Concurrency]]
Continued by [[Cerebras Wafer Scale Engine]]
# Difference From SIMD?
- The unit of execution is a sequential thread
- A group of threads executes in lockstep (SI) fashion
	- The same statement will be executed on all the processors at the same time
- Flexibility in grouping threads to maximize parallelism
- Size of problem exposed by number of threads
- SIMD uses a single thread and exposes the width of the data stream to the programmer
# GPU Programming
## Kernel Function
- ![[Pasted image 20260504173047.png]]
- A kernel function specifies the action of a *single* thread
- Multiple threads will execute concurrently
- Most sequential operations are available: math, loops, conditionals, etc
- Vars can be local, shared within a group of threads, global to all threads
- Built-in variables like tid to distinguish among threads
- ![[Pasted image 20260504173226.png]]
## Terminology
- **Thread:** Sequential execution
- **Thread Block:** Group of threads that execute concurrently
	- Runs on a single SM
	- Access to fast shared memory, synchronization
- **Grid:** Collection of thread blocks
	- Executes across SMs
	- Do not synch with each other
	- Communication is expensive
## Scale of SMs and CUDA Cores on Blackwell
![[Pasted image 20260504182302.png]]
## Calling a CUDA Kernel
`kernel<<num_blocks,threads_per_block>>(args);`
## CUDA Multiple Thread Blocks
- ![[Pasted image 20260504173415.png]]
	- One thread per block
	- The host code creates N blocks that each perform the add of one element of the array
## CUDA Multiple Threads within a block
![[Pasted image 20260504173641.png]]
- Give the whole add to a single SM
- Instead of N blocks with 1 thread, do 1 block with N threads
## CUDA Multiple Blocks Multiple Threads
![[Pasted image 20260504173744.png]]
- There are 1024 threads within a thread block
- There are N threads running across N/k blocks with each block running k threads
- The kernel code must now compute the array index based on ThreadId and BlockId
- ![[Pasted image 20260504173931.png]]
	- blockDim is threads/block
- Must write kernel to anticipate that there may be multiple blocks
## Blocks and Threads
![[Pasted image 20260504174146.png]]
![[Pasted image 20260504174252.png]]
![[Pasted image 20260504174635.png]]
![[Pasted image 20260504174655.png]]

## SIMT Hardware
- ![[Pasted image 20260504174709.png]]
- Registers are private to the cores
- The shared memory can be shared between threads executing in the SIMT core
## Matrix Multiply Example
![[Pasted image 20260504174937.png|687]]
- 64x64 square matrix
- Split the matrix into a 4x4 array of blocks, where each block has a 16x16 array of threads
- ![[Pasted image 20260504175408.png]]
	- Assuming row major organization of 2d arrays
- Kernel program
- ![[Pasted image 20260504180134.png]]
# CUDA Execution
![[Pasted image 20260504181304.png]]
- Thread blocks given to scheduler
- Dispatcher gives blocks to SMs
- The SM has many CUDA cores inside of it that all execute threads concurrently
# CUDA Warps
- The unit of execution in NVIDIA is a **warp**
- A warp is a bundle of threads with consecutive Ids executed in lockstep
	- They have one program counter
	- There is no need for control logic for each core, they're all doing the same stuff at the same time
	- The CUDA core is just an execution unit
- ![[Pasted image 20260504181639.png]]
- Aka wavefront, simdgroup
- In CUDA, a warp is 32 threads
![[Pasted image 20260504181834.png]]
## Warp Scheduling
![[Pasted image 20260504182202.png]]
- Fine-grained multithreading: For each execution cycle, the scheduler chooses a new executable warp
- Instruction executes in pipelined fashion within a CUDA core
- **Warps are interleaved in time** but not round-robin
	- The warp scheduler makes decisions based on which warps can be executed at what time
	- If it was just round robin, no scheduler needed
- If a warp encounters a long-latency event (i.e. cache miss), other warps can execute
- What if cores/SM > warp size?
- You need multiple warp schedulers: multiple warp instructions issued per cycle

## Intra-Warp Divergence (Branching)
- ![[Pasted image 20260504182711.png]]
- There is only one PC for all threads in a warp, so what happens when different threads take different paths?
- Conditional expression sets **taken/not-taken flag** for each thread
- Both paths are executed sequentially with bits controlling which threads executes and which do nothing
- This is known as *lane masking* in SIMD terminology
- Do the threads who take the branch and then the ones that don't
- ![[Pasted image 20260504182908.png]]

## Warp Vote Functions
![[Pasted image 20260504183454.png]]
- All sync:
	- Evaluate predicate in all threads specified by mask, return non-zero if all are non-zero
- any_sync
	- Evaluate predicate in all masked threads, return non-zero if any is non-zero
- Ballot
	- Evaluate predicate in all masked threads, return value has bit N == 1 if thread N's predicate is non-zero (and thread N is active)
- activemask
	- Return value has bit N == 1 if thread N is active
### Warp Vote Example
- ![[Pasted image 20260504183508.png|666]]
## Warp Match Functions
![[Pasted image 20260504183821.png]]
- Match any sync
	- Return a mask of all specified threads whose values are equal to each other
- Match all sync
	- Returns mask if all specified threads have the same value, otherwise 0
	- Pred is set to true (non-zero) if all specified threads have the same value, otherwise false (0)
## Warp Reduce Functions
![[Pasted image 20260504185243.png]]
- The reductions is produced and then broadcast to all threads in the warp

# SIMT Memory
![[Pasted image 20260504185627.png]]
- L1 cache and shared memory use the same chunk of memory
	- The software can configure what % is used for each
	- The L1 region is managed by hardware, shmem by software
- L2 is the coherence point, no hardware coherence between L1 and L2
## Shared Memory Organization
- Kernel code explicitly declares variables are shared
- ![[Pasted image 20260504190536.png]]
- Shared memory is banked, one read port and one write port per bank
### Shared Memory and Synchronization Example (1D Stencil)
- ![[Pasted image 20260504190636.png]]
- Similar to ocean, apply a 1D stencil to a 1D array
- Cache data in shared memory
	- Read (blockDim.x + 2 * radius) input elements from global memory to shared memory
		- The 2* radius is because each block needs a read-only halo of `radius` elements at each boundary
		- Compute Blockdim.x output elements
		- Write blockdim/x output elements to global memory
- ![[Pasted image 20260504191351.png]]
- ![[Pasted image 20260504191407.png]]
- There is a data race with this code
- ![[Pasted image 20260504191729.png]]
- Suppose a thread in a different warp reads the halo before thread 0 has fetched it
- Add a call to syncthreads (a barrier)`
- ![[Pasted image 20260504192005.png]]
## Global Memory: Coalesced Access
![[Pasted image 20260504192212.png]]
- Hardware tries to coalesce multiple writes into a single write to one cache line
## Thread Memory Hierarchy
![[Pasted image 20260504192337.png]]
- Threads have private registers
- They also have shared memory per block
- After that there is shared memory of all thread blocks in a cluster, which form a Distributed Shared Memory
	- **Thread Block Cluster** Spans multiple SMs and create distributed shared memory
- Finally there is global Memory shared between all GPU kernels
## Weak Memory Ordering
- No hardware ordering between loads and stores by default
- ![[Pasted image 20260504192721.png]]
## Memory Fence Functions
![[Pasted image 20260504193044.png]]
- Thread Fence Block
	- All writes before this call have been pushed out to all threads in the block before any other writes can occur 
- Thread fence (device)
	- Write ordering applies to every thread in the device instead of just the thread block
- Thread fence system
	- Write ordering applies to every thread in the device, every host thread, and every thread on peer devices
![[Pasted image 20260504193518.png]]

## Synchronization Functions
![[Pasted image 20260504193821.png]]
- syncthreads
	- Waits until all threads in the thread block have reached this point and all global and shared memory accesses made by these threads prior to syncthreads are visible to all threads in the block
- syncthreads_(reduction)
	- Combines a barrier with a reduction
- Sync warp
	- Will cause the executing thread to wait until all warp lanes named in a mask have executed a syncwarp (with the same mask) before resuming execution. Also guarantees memory ordering
	- For example: Need to sync within a conditional, but not for every thread in the warp because not all threads are executing that branch.
- Sync functions also act as fences

### Sync Example
![[Pasted image 20260504194033.png]]
- result is volatile so it must go to L2
![[Pasted image 20260504194305.png]]
- Second arg to atomic inc sets limit of incremented var. If goes over limit, set back to 0
	- Returns old value
![[Pasted image 20260504194712.png]]

## Cooperative Groups
- User can specify granularity at which threads communicate
- C++ classes with member functions for synchronization, memory copies, reduction, etc
- ![[Pasted image 20260504195155.png]]
- Can partition existing groups into new groups arbitrarily
- 
# Memory Enhancement: Unified Memory![[Pasted image 20260504195519.png]]


For class #parallel-arch