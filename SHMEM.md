Expands topic in [[Ultra Ethernet]]

# Overview
- Family of parallel programming libraries providing **one-sided**, RDMA, parallel processing interfaces for low-latency **distributed-memory** supercomputers
- Generates a Partitioned Global Address space (PGA), where memory addresses can access local or remote memory
- Provides primitives like, get and put
- P2P operations are one sided
	- No active cooperation is needed to complete the action
	- Local memory can be polled for changes using `shmem_wait`
- For short datatypes, SHMEM can do atomic operations in remote memory

For topic #thesis/ultraethernet

