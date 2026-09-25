Jaskin Kabir
jakabir@ncsu.edu
200378487

# Questions

## Q1: Max Processes

The maximum number of processes is 100, defined on line 71 of `conf.h`

## Q2: Bad PID

A bad PID is one that is less than 0 or greater than or equal to the
maximum number of processes. If the state of the process table entry for
a given PID is PR_FREE, that pid is also illegal This is defined on line
33 of `process.h`

## Q3: Default Stack

The default stack size is 65536 bytes, defined on line 27 of `process.h`

## Q4: Process State Diagram

![[Pasted image 20260912001313.png|600]]

## Q5: Shell Process Creation

The shell process is created in `main.c` on line 18. The shell process is created by the main process, which recreates it whenever it is killed (`main.c`). The main process is created at the end of the startup process (`initialize.c`). The startup process is created near the end of the `nulluser` function (`initialize.c`), which is called from the start procedure in `start.S`.

## Q6: Process Tree

![[Pasted image 20260912001202.png]]

By the time the shell process is created, the startup process (PID 3)
has already exited, so it is not a live process. It is kept in the tree
diagram for visualization purposes.

## Q7: Effect Of `receive()` Call In Test Cases

The `receive()` system call yields control to the next process in the
ready queue if no message is present. In each of the three test cases,
`receive()` is called by each parent process after it has created its
children. If this function call was not present, the child processes
would not begin execution until the parent process hits its return
statement. This would cause the instructions to execute out of the
intended order. Additionally, the main function's receive call could be
triggered by the parent process exiting before its children finish. The
`receive()` call is used to explicitly schedule the child processes to
execute in the intended order.

# Coding Part 1: Cascading termination
## Files Changed
| File | Changes |
|------|---------|
| `include/process.h` | Added `user_process` field to `procent` struct |
| `system/create.c` | Set default value of `user_process` to `FALSE` |
| `system/kill.c` | Implemented cascading termination for user processes |
| `system/main.c` | Added test case for cascading termination |
| `include/prototypes.h` | Declared `debug_printf` function |
| `system/debug_printf.c` | Implemented `debug_printf` function |

## Brief Implementation Explanation

I first added a new field to the `procent` struct called `user_process`.
This field is set to `FALSE` by default in `create.c`. To create a user
process, call `create()` normally, then manually set its `user_process`
field in the process table to `TRUE`. 

To implement cascading termination for user processes, I added a small
piece of code to the `kill()` function, seen below. If the process to be
killed is a user process, iterate through the process table and
recursively kill all processes whose parent is the process to be killed.

I initially considered storing a Left-Child Right-Sibling (LCRS) binary
tree for each process in the process table. This would eliminate the
need to iterate through the entire process table for every recursive
call to `kill()`. However, the memory overhead of this approach would be
far too great–especially for an OS like Xinu, which is designed for
embedded devices.

```c
	if (prptr->user_process) {
		for (i = 0; i < NPROC; i++) {
			if (proctab[i].prparent == pid) {
				kill(i);
			}
		}
	}
```

## Test Case

To comprehensively test the cascading termination functionality, I built
a tree of dummy processes. The processes are all created in the
`big_test()` function in a single process. The `prparent` field of each
process is set manually to construct the tree for simplicity's sake. 

The first test is to kill a process with no children (should kill one process). Next, kill one child of a process with many children (should kill one process). Next, kill the root process of the children (should kill all children and sibling parent). Next, kill the root process of a linear chain of children (should kill all children and parent). Next, kill a process from the second-lowest level of a binary tree of processes (should only kill three processes). Finally, kill the root process of the entire tree (should kill all processes in the tree). 

### Test Case Tree

![[Pasted image 20260912001231.png]]
# Coding Part 2: Fork


## Files Changed
| File                   | Changes                     |
| ---------------------- | --------------------------- |
| `include/prototypes.h` | Declared `fork` function    |
| `system/fork.c`        | Implemented `fork` function |

## Brief Implementation Explanation

The `fork()` function first disables interrupts to ensure some atomicity
of the fork operation. It then saves the general purpose registers to be
later written to the child process's stack frame. I then creates a new
process, allocates a stack for it, and sets the fields of its process
table entry--mostly to those of its parent. Next, the function calls
`memcpy()` to copy the parent's stack to the child's stack.

This is not enough, however. Firstly, every saved stack base pointer in
the child's stack points to a location in the parent's stack, and must
therefor be updated to point into the child's stack. Secondly, when
ctxsw.S runs on the child process, it won't find the saved values it is
looking for to restore program state. Therefore, the `fork()` function must first walk the chain of saved stack base pointers to update them to point into the child's stack. Then, it must create a fake stack frame ctxsw.S can pick up and 'restore' to restore program state.

Updating the chain of base pointers first calculates the byte offset
from the parent's stack to the child's stack. It declares variables
`cur_ebp` and `next_ebp` to point to the current and next base pointers
in the chain, and `child_ebp` to point to the current base pointer in the child's stack. It sets `cur_ebp` to the parent's base pointer and then
executes the following algorithm:

1. Set `next_ebp` to the location pointed to by `cur_ebp`
2. Set `child_ebp` to the current base pointer plus the stack delta 
3. Set `cur_ebp` to `next_ebp`
4. Increment the location pointed to by `child_ebp` by the stack delta
5. If the location pointed to by `cur_ebp` is `STACKMAGIC`, stop

`create()` places the magic number `STACKMAGIC` at the end of the parent's stack. This is used to determine when the end of the chain is reached.

The `fork()` function then creates a fake stack frame ctxsw.S can pick up and 'restore' to restore program state. This is done in much of the same way as the `create()` function. The value that ctxsw.S will pick up for the `eax` register is set to `NPROC`, so that the child process will see `NPROC` as the return value from the `fork()` function. 

Finally, the `fork()` function increments the process count and inserts the child process into the ready queue.