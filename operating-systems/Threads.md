Continues [[Processes]]
Related to [[OpenMP]]
Continues [[OS Scheduling]]
# Definition
- A thread is the smallest sequence of instructions that can be managed independently by a scheduler
- A process may contain multiple threads
- All the threads within a process share the same address space and resources
- Each thread has
	- An execution state: running/ready/etc
	- An execution context: registers/flags
	- A per-thread stack: local vars 
		- Different threads can execute different code, needs separate stacks
- ![[Pasted image 20260901112826.png]]
# Thread Context Switch
- Each thread has its own state
	- PC to track fetching of instructions
	- Private set of registers (including SP)
- Moving execution of one thread to another requires a context switch
	- Thread control block required to store thread state
	- But address space in use remains the same
- When?
	- Async events:
		- Hardware interrupts, time quota, etc
	- Synchronous calls
		- Thread performs blocking syscall
		- Thread voluntarily yields
# Thread Vs. Process
- Processes have different address spaces, threads share the same address space
- Threads within a process usually cooperate
## Thread Advantage: Matmul
- Imagine a 3-thread matmul
- Single threaded version must
	- 1. Read matrix from memory
	- 2. Compute
	- 3. Write result to memory
- A 3-threaded matmul can have the OS interleave these tasks
- We can pipeline the execution. After 3 memory reads in T1, 
	- T1 is fetching the third input chunk
	- T2 is operating on the second input chunk
	- T3 is storing the first output chunk 
## When To Use Threads

### Use Threads
- Server applications
- Multiprocessor machines
- Handling of slow devices
- Background operations
- Windowing systems
### Do Not Use Threads
- Each unit of execution requires different auth or userid (e.g. secure shell servier)
# Thread Implementation
## User-level threads
- management done in user space by user-level threading library
- Three primary thread libs
	- POSIX Pthreads
	- Windows threads
	- Java threads
- Kernel unaware of thread activities
- User-level library performs OS tasks
	- Owns thread creation and termination
	- Owns thread scheduling and context switching
	- Maintains control info
- The OS scheduler will only assign one CPU core to the process, so user-level threads cannot execute in parallel
## Kernel-level threads
- Management done by kernel
- Supported by all general-purpose OSes
## User Vs. Kernel Threads
### Scheduling
- For user-threads
- Imagine T1 issues a blocking disk read
- T2 could be started while T1 waits for the disk
- But the kernel has no idea about this, it just sees the entire process in the waiting state and doesn't schedule it until the disk generates an event
### User-level pros and cons
- Pros
	- Performance: low-cost thread creation and context switch
	- Flexibility: application-specific scheduling
	- Portability: No changes to kernel required
- Cons
	- Blocking system calls block all threads within a process
	- Multithreaded app cannot use multiple cores
### Kernel-level threads pros and cons
- Pros
	- Multiple threads can be scheduled concurrently onto different cores
	- If a thread is blocked on a blocking call, the kernel can schedule other threads belonging to the same process
- Cons
	- Transferring control to another thread requires mode switch to kernel
## Combined Approachess
![[Pasted image 20260903111745.png]]
- **Many-to-one:** Can map many user-level threads to a single kernel thread
	- Solaris Green threads
	- GNU Portable Threads
- **One-to-one:** Can map each user-level thread to a kernel thread
	- \# of threads/processes sometimes restricted due to overhead
	- Linux!
- **Many-to-many:** Many user-level threads mapped to many kernel threads
	- Allows OS to create a sufficient number of kernel threads
- **Two-level:** Similar to M:M, but allows a user thread to be bound to a kernel thread
# Semantics of fork() and Exec()
- Does fork() duplicate only the calling thread or all threads?
	- Only the calling thread is duplicated into the child
	- Some UNIX distros have two versions of fork
		- Solaris had forkall() and fork1()
- Exec replaces the running process including all threads
## Thread Cancellation
- Terminating a thread before completion
- Two approaches
	- Asynch: Terminates target thread immediately
	- Deferred: Target periodically checks if it should be cancelled
# Thread Libraries
- Two ways of implementing API
	- Library entirely in user space
	- Kernel-level library supported by OS
## Pthreads
- May be provided as either user or kernel level
- A POSIX standard API for thread creation and synchronization
	- It is a Specification, not an implementation
	- API specifies behavior of the thread library, implementation is up to dev
- Common in UNIX OSes
### Pthread API
- Thread management, creation, termination
- Synchronization: tthread join, mutexes, condition vars
### Pthread Creation
- `pthread_create(pthread_t* thread, pthread_attr_t attr, void * routine, void * args)`
- `void *` is just an address, with no type info
	- Must be cast to a type before dereferencing
### Pthread Arguments
- What if thread routine needs multiple parameters?
-  Create a struct to hold these arguments and pass to thread
### Pthread Synchronization
- join: Parent waits until child is done
- 
### Stack Management
- Programmer can explicitly allocate stack space per thread by calling setter `pthread_attr_setstacksize()`
### Implicit Threading
- Creation and management of threads done by compiler and run-time libraries rather than programmers
- OpenMP
	- Set of compiler directives and and API for C, C++, FORTRAN
	- Parallel programming in SHMEM environments
# Thread Scheduling
- Single core processor
	- Can two threads run on the same core at exactly the same time? No
	- When would you run a multithreaded program on a single core? When there are idle times (I/O)
	- What is the optimal number of threads to run on a single-core processor (depends on waiting times)
- Multi-core processor
	- Can two threads be in the running state at the same time? Yes
	- Optimal number of threads to run on an N-core processor? Not necessarily N. Still depends on waiting times
	- The more waiting time, the more threads we should spawn to hide the idle time