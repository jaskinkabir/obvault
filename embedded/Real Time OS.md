[[Bootloaders]]

# RTOSes
## FreeRTOS
- Open source and lightweight
- Widely supported
## Zephyr RTOS
- Open source, supported by linux
- New
- Scalable for IoT and multi-core systems
## RTX
- Developed by ARM
- Optimized for Cortex-M mcus
- Supported within Keil MDK and STM32
## ThreadX
- Commercial grade
# Underlying Concepts
- In bare-metal applications, execution is linear.
- Blocking function calls may deadlock the processor
## Cooperative Scheduling
- Each function passes CPU execution time to the next function
- Scheduling is done by functions themselves
## Threads
- A thread is essentially a function
- When threads are created, they are allocated a block of memory n SRAM to store their own stack
- The allocation is made dynamically on the heap
- These sections of memory each include a section called the **Thread Control Block** (TCB)
- The TCB backs up important registers during context switching
# What is an RTOS
- An RTOS offers the notion of multitasking (or multithreading) while ensuring response within specified time constraints
- These time constraints are known as **Deadlines**

# General Purpose OS and Timing
- Linux and windows cannot be real time because of
	- Pagination and Swapping
## Pagination
- Pagination allows segmentation of task memory into small chunks named pages
- Pages can be scattered in RAM and aliased from the MMU
- Swapping allows to swap in and out unused pages on a slower memory device (like a hard drive)
- Swapping and pagination are non-deterministic and prevent the OS from servicing requests in short and countable time
- When a program accesses a page not in memory, a page fault occurs.
- Resolving this fault is slow and indeterminate

# Context Switching
- What if a task wants to take more time than the scheduler will allow before switching context?
- For example, an LED blinking task will want to wait for 500ms, but the RTOS wants to perform a context switch after 1ms
- A context switch needs substantial help from the hardware
- An interrupt will pry away control from a function that refuses to release it
- A dedicated hardware timer like systick will use the periodic overflow event to perform the context switch
- The ISR will back up the current execution context into the TCB, then restore the register contents with the next task's TCB
# SuperVisor Calls
- If a task wants to voluntarily release control, it can make a supervisor call which executes an ARM instruction for this purpose
# The CMSIS-RTOS v2 Wrapper
- Many RTOSes have shared features but different implementations.
- The wrapper exposes a standardized API to interface with these OSes
# Threads in CMSIS-RTOS2
## Thread Creation in CMSIS-RTOS2
- A thread is a function that contains a loop of code
- It is created by calling the new thread function. This is its prototype

```c
isThreadId_t osThreadNew(osThreadFunc_t func, void *argument, const osThreadAttr_t *attr)` function
```
- The `osThreadAttr_t` struct contains the attributes of the thread
- ![[Pasted image 20251201204309.png]]
![[Pasted image 20251201204504.png]]
## Thread States
- Threads can either be running or not running
- The not running state can be characterized by several sub-states
- A not running thread can only resume its execution in the ready state.
- A not running thread can be ready
	- Indicates that the thread can be scheduled for execution by the RTOS kernel
	- Default state of new threads
- A running thread can voluntary suspend execution by moving into the suspended state
	- Once in this state, it can only be resumed back into the ready state.
- A running thread can block itself by starting to wait for an external event
## Thread Priorities
- ![[Pasted image 20251201204546.png]]
## Scheduling
- There are 3 scheduling algorithms used by RTOS
	- Prioritized preemptive with time slicing
	- Prioritized preemptive without time slicing
	- Cooperative
- ![[Pasted image 20251201204806.png]]
### Time Slicing
- Each task is given a portion of time to run
- Once that time is up, it is preempted by the next task
- Without time slicing, each task would run to completion before passing control to the next task
- ![[Pasted image 20251201204643.png]]
### Prioritized Preemptive Scheduling
- Allows higher priority tasks to preempt running tasks of a lower priority
![[Pasted image 20251201204920.png]]

### Cooperative Scheduling
- The programmer has all scheduling responsibility
- When a task yields while multiple other tasks are in the ready state, the highest priority one will start first.
![[Pasted image 20251201205100.png]]
## The Idle Thread
- A continuous task with the lowest priority that consumes CPU cycles while no other task is running
## Thread Deletion
- In FreeRTOS<10, thread memory can only be freed by the idle thread
- In FreeRTOS>=10, thread memory is immediately freed upon deletion
- If a thread deletes itself, its memory is freed by the idle thread
- Note that only the stack and TCB allocated to the thread is freed. Any memory allocated on the heap must be properly managed by the thread
# Synchronization Primitives
- Threads must synchronize while accessing shared resources or transferring data between execution streams
## Message Queues
- FIFO buffer that threads/ISRs can write to and read from linearly
	- Have an ID, queue size, and message size
	- ![[Pasted image 20251201205900.png]]
- If a producer tries to place data into a full queue, it is placed into the blocked mode until space in the queue is freed
- If a consumer tries to read from an empty queue, it is also blocked
### Enqueueing new elements
- ![[Pasted image 20251201210249.png]]
- Priority is ignored by STM CMSIS-RTOS2 
- Timeout indicates amount of ticks we are willing to wait if the queue is full
	- If sufficient room is not made available before timeout, the function times out
	- We can wait forever
### Dequeuing, Deleting, and Resetting
- Dequeuing follows the same argument list as queueing
- Deletion and resetting have separate functions, both returning a status
For class #embedded