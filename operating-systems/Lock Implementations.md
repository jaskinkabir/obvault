# Producer-Consumer Problem
- Producers and consumers can compete for shared resources which hold the produced/consumed data
- Race conditions
## Example
- Producer tries to increment counter after production
	- Counter is idx into shared array
- Consumer tries to decrement counter after consumption
# Race Condition Definition
- Two conditions
	- Multiple processes/threads read and write shared data concurrently
	- The final result depends on the order of execution
- Operating system scheduling is non-deterministic and opaque to user programs
- For correct operation. execution result must be independent of scheduling/interleaving
- OS must provide some synchronization primitives
## Concurrent Linked List Example
- 2 threads:
	- T1
		- a `n->next=p->next`
		- b `p->next=n`
	- T2
		- c `m->next=p->next`
		- d `p->next=m`
- Order: abcd
	- T1 Inserts n between p and its next element
	- T2 inserts inserts m before n and moves p behind m
# Critical Section Problem
- A **Critical Section** is a piece of code that has a race condition
	- Accesses shared resources
	- Must not be concurrently executed by more than one thread
- Critical design problem
	- OS must provide a protocol to allow thread cooperation
## Required Properties of Solutions
- A solution to the critical section problem should include ALL the following 3 properties
### Mutual Exclusion
- No two processes/threads can be executing in their critical sections at the same time
### Progress
- If no process/thread is in its critical section and some processes/threads are ready to enter their critical sections, the selection of the next process to enter critical section next cannot be postponed indefinitely
### Bounded Waiting
- A bound must exist on the number of times that other processes/threads rare allowed to enter their critical sections after one has requested critical mode
## CritsSec Handling in OS

- Preemptive kernels allow preemption of process when running in kernel mode
	- May be more responsive
	- More suitable to real-time programming
- Non-preemptive kernels do not
	- A kernel-mode process will run until it exits kernel mode, blocks. or voluntarily yields control.
	- No race conditions on kernel data structures
# Mutex Lock Implementations
## Interrupt Disabling
- OS provides `lock()` and `unlock()` primitives
	- lock() disables scheduler by masking all interrupts
	- unlock() re-enables scheduler
### Pros and Cons
- Pros
	- Very simple
- Cons
	- Doesn't work on multicore processor
	- Critical sections that depend on I/O interrupts are not supported
	- Other threads cannot be scheduled even if they don't have critical sections
	- Too much power to the application/user
## Spinning Compare and Swap
### Compare and Swap Atomic Instruction
```c
int compare_and_swap(int *value, int expected, int new_val){
	int old_value = *value;
	if (old value == expected)
		*value = new value;
	retrun old value;
}
```
- This function is implemented as a single atomic hardware instruction on x86 processors
- Can implement lock and unlock
```c
lock(bool *lockvar) {
	compare_and_swap(lockvar, true, false);
}
unlock(bool *lockvar) {
	compare_and_swap(lockvar, false, true);
}
```
-	Two threads
	-	T1:
		-	`y=c&s(&x, 0, 1);`  
	-	T2:
		-	`y=c&s(&x, 0, 2);`
	-	If T1 comes first, x=1, y=1
	-	IF T2 comes first, x=2, y=2
	-	Order of interleaving changes result, but in both cases the threads always know whether their c&s took place or did not
### Spinning C&S Lock Code Example
```c
typedef struct {
	int flag; // if flag == 0, lock is available
} lock_t;

void lock(lock_t *lock) {
	while(compare_and_swap(lockv, 0, 1)==1);
}
void unlock(lock_t *lock) {
	lock->flag = 0;
}
```
#### Pros and Cons
- Pros
	- Simple
	- Threads outside critical section can still be scheduled
	- Supports multicore CPUs
	- Different threads with different critical sections can execute concurrently so long as they use different locks
- Cons
	- OS must schedule waiting jobs only for them to just spin and waste CPU time/sched resources (called **Busy Wait**)
	- Prone to **starvation**: 
		- 3 Threads all executing:
```c
while(1) {
	lock(lockvar);
	critical_section();
	unlock();
}
```
- Theoretically, the OS can choose to schedule T1 over and over again. T2 and T3 will never receive the lock
- **Deadlock**
	- Priority Scheduling
	- T1 has low priority, T2 has high priority
	- T1 acquires lock
	- T2 enters system
	- T2 starts spinning on T1's lock
	- OS schedules T2 instead of T1 because of its higher priority, but it can only spin because T1's lock hasn't been released yet
## Yielding Spin Lock
```c
void lock(lock_t &lockvar) {
	while (compare_and_wap(lockvar.flag, 0, 1)) {
		yield();
	}
}
```
### Solves:
- Somewhat solves **busy wait**
	- Thread does not consume entire time slice while waiting
	- However, threads should not even be in the ready list unless the lock is available
	- When the CPU ctxsw's into a thread only for that thread to just yield after checking the lock, the CPU just wasted time on the ctxsw overhead and the test
- Does not solve **Starvation**
	- Within one time slice, a thread can unlock and relock the mutex
	- Even when the thread unlocks the mutex, it will lock it again within the same time slice
	- The other threads starve
- Does not solve **Deadlock**
	- Low priority thread ($T_L$) holds lock
	- High priority thread ($T_H$) needs lock
	- $T_H$ has same high priority after yielding, and can be scheduled again immediately after it yields
	- $T_{L}$ is never scheduled; deadlock
## Waiting List
- Introduce new list alongside ready list which holds threads that are waiting on a lock (WAIT_STATE
### Park and Unpark
- Introduce new primitives
	- park() puts thread in wait state
	- unpark() wakes up a thread in wait state (puts in READY state)
```c
typedef struct {
	bool flag; // Is lock taken?
	bool guard; // Ensures no 2 threads can lock/unlock concurrently
	queue_t * waiting; // Processes waiting for lock 
} lock_t

void lock(lock_t * l) {
	while (c&s(l->guard, 0, 1));
	if (l->flag == 0) {
		l->flag = 1;
		l->guard = 0;
	}
	else {
		enqueue(l->queue, get_tid());
		set_park();
		l->guard = 0;
		park();
	}
}

void unlock(lock_t * l) {
	while (c&s(l->guard, 0, 1));
	if (queue_empty(l->queue)) {
		l->flag = 0;	
	}
	else {
		unpark(dequeue(l->queue));
	}
	l->guard = 0;
}
```
- Does not work because of park() unpark() synchronization
### Set Park/ About To Park
#### Lost Wakeup Problem
- Notice that the guard must be released before calling `park()`, because any thread that the waiter yields to must be able to acquire the guard
- This creates a problem.
- Imagine scenario
	- Thread A tries to acquire lock held by Thread B
	- It blocks and calls `park()`
	- Context Switch Occurs right before TA executes `park()`
	- Thread B releases the lock and calls `unpark(A)`
	- Thread A hasn't called `park()` yet; TB's `unpark()` does nothing
	- Context switch: Thread A resumes and calls `park()`
	- Thread A sleeps forever. The wakeup signal has been lost
#### The About to Park Flag
- Before calling `park()` Thread A calls `set_park()` and sets its `about_to_park` flag
- Thread A puts itself into the lock's queue and releases the guard
- Thread B context switches in and tries to unpark A
- It sees that the `about_to_park` flag is set, so rather than moving TA into the ready list it just clears the flag
- Thread A wakes up and executes `park()`
- `park()` sees the flag has been cleared and does nothing
```c
typedef struct {
	bool flag;
	bool guard;
	queue_t * waiting;
} lockvar_t;

void lock(lockvar_t * l) {
	while (c&s(l->guard, 0, 1));
	if (l->flag == 0) {
		l->flag = 1; // acquired
		lock->guard = 0;
		return;
	}
	enque(l->queue, get_tid());
	set_park();
	l->guard = 0;
	park();
}
void unlock(lockvar_t * l) {
	while (c&s(l->guard, 0, 1));
	if (queue_empty(l->queue)) {
		l->flag = 0;	
	}
	else {
		int tid = dequeue(l->queue);
		if (proctab[tid].state = PR_READY) {
			proctab[tid].about_to_park = 0;
		}
		else {
			unpark(tid);
		}
	}
	l->guard = 0;
}
```
- The about_to_park flag should be process-specific and stored in the PCB
### Spinning?
- We still have a spin lock within our new lock
	- On the guard `while (c&s(l->guard, 0, 1));` 
- However, this spin is only for the duration of the `lock()` and `unlock()` functions
- This has a bounded, small amount of time
- In the Spin Lock, the waiting threads spin for the entire duration of the critical section
- This time is unbounded and could be very long
### Solves:
#### Busy Wait
- **Busy wait** is almost completely solved
- Shorter, bounded spin on acquiring the guard
- In a spin lock, waiting threads must spin for the entire duration of the critical section
- In the park/unpark lock the waiting thread only spins for the duration of the lock() function
#### Starvation
- Starvation is solved
- A thread cannot unlock and lock in the same time slice
	- T1 calls unlock(), which dequeues waiting T2 and doesn't reset the lock flag
	- Then T1 calls lock() in the same time slice, but sees the flag=1 and parks itself
	- Then T2 starts executing as it has acquired the lock
##### Barging
- Serving the lock queue in strict FIFO order is required
- Scenario
	- Thread A blocks, waiting for lock
	- While Thread B releases the lock, Thread C is spawned
	- Thread C acquires lock before A
- Park/unpark lock solves this
	- Thread B directly hands off the lock to A because it never resets the lock flag
	- No matter how many threads are spawned, only A is in the guarded section and able to acquire the lock
- **Deadlock:**
	- Deadlock is almost solved because a high priority thread who waits on a low priority thread's lock will go into the wait state and stop being scheduled
	- There is still deadlock risk on the guard's spin lock
		- We can solve this by adding a small `sleep()` call while spinning on the guard
#operating-systems 