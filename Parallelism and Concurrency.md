Continued by [[Memory Technologies]]
# Amdahl's Law
- Speedup due to parallelization is limited by the serial tasks$$S_{p}=\frac{1}{s+\frac{1-s}{P}}$$
	- $s$ Proportion of task that must be done in serial
	- $P$ Number of processors
	- $S_{p}$ Speedup due to paralellism
- As the number of processors reaches infinity, the speedup reaches a maximum value based on the serial processing time
- ![[Pasted image 20260210174922.png]]
	- Even with 1% serial code, diminishing returns

# Are Tasks Really Independent?
- Consider finding the max of a list
- You could parallelize by assigning finding the max of small sections of a list to many processors
- But then you have to find the max of these sections
- Dependencies, synchronization and communication can cause real-world parallelism to lag behind Amdahl's law
## Imperfect Parallelization
- Parallelization requires some overhead
- Factor this into the equation
- $$S_{p}=\frac{1}{s+o(P)+\frac{1-s}{P}}$$
	- $o(P)$ is overhead per processor
- ![[Pasted image 20260210175156.png]]
	- Sometimes, parallelization overhead overtakes the speedup
	- An optimal number of cores arises
# Gustafson's law (Scaled Speedup)
- $$S=s+pP$$
- Gustafson's law says that with each processor, you also get more resources
	- Cache, memory, etc
- You can solve a bigger problem with a more parallel computer
- Scaling is more linear
# Superlinear Speed up
![[Pasted image 20260210191304.png]]
- As more processors are added, so is more cache
	- Each processor is only accessing a portion of the data
	- Eventually, as processor count increases, the data each pu needs will fit inside the cache
	- Memory accesses will become much faster

# Flynn Taxonomy
- ![[Pasted image 20260114200552.png]]
- SISD: One instruction works with 1 data stream
- SIMD: One instruction tells multiple processing units to work on multiple data units
	- GPGPU uses SIMD architecture
- MISD: Multiple instructions tell multiple processors to work on one data stream
- MIMD: Each processor has its own instructions and its own data stream
	- The multicore era, what this class focuses on
# Communication/Synchronization
## Shared Memory
- Typically in a multiprocessor
- PUs communicate with a shared memory space through some interconnection layer
## Message Passing
- Typically in a cluster
- Each PU has its own memory, they communicate by sending messages across an interconnect
![[Pasted image 20260114201452.png]]

For class #comporg