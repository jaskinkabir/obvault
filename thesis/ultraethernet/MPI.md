Expands topic in [[Ultra Ethernet]]
# Overview
- Message Passing Interface
- Standard specifies interfaces to the following functionality
	- Point-to-point comms
	- Datatypes
	- Collective operations
	- Process groups
	- Process topologies
	- One sided comms
	- Parallel file IO
## Basic Conventions
- MPI programs are sequential
- The basic worker unit is a **Process**
	- Assigned consecutive ranks (int)
	- A process can ask for its rank and total ranks within program
- Data exchange and synch are implemented by sending and receiving msgs using lib calls
- MPI uses the term **Communicator** for a group of ranks
- The predefined communicator `MPI_COMM_WORLD` includes all processes in a job
- Communicators can be created at runtime and are an argument to every MPI comm routine
## Point-to-point comms
- MPI comms routines consist of data and an envelope
	- Data is specified by a pointer to a mem buffer, datatype, and a count
		- Count may be 0 to indicate an empty buffer
	- Envelope is the source (implicitly specified by the sender), destination, tag and communicator
		- Destination is the id of the receiving process
		- Tag is an integer that distinguishes message types
		- 
- There are two basic flavors of p2p comms
	- Blocking
		- Comm buffer passed to the routine may be reused after the call returns
	- Non blocking
		- Comm buffer must not be used until completion test called
- Communications are **two sided**
	- Both sender and receiver must participate
	- A process can only post a send operation if the receiver posts a receive operation 
## Collective Operations
- Collective comms primitives are for cases where all ranks are involved in comms
- Does not interfere with point-to-point
- All ranks within a communicator have to call the routine
- Three types of collective comms
	- Synchronization (barrier)
	- Data movement (gather, scatter, broadcast)
	- Collective computation (reduction)

# MPI Machine Model
- ![[MPI-model.png]]
- All processors P do not share any topological entity with one another and are equal with every respect
- They are connected using one uniform network

For topic #thesis/ultraethernet