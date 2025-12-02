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
- If a task wants to voluntarily
# The CMSIS-RTOS v2 Wrapper
- Many RTOSes have shared features but different implementations.
- The wrapper exposes a standardized API to interface with these OSes


For class #embedded