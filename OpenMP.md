# Overview
- API that supports C, C++, Fortran, etc
- Explicit parallelism through
	- Directives
	- API
	- Environment variables
- Fork-join model,
	- A master thread spawns parallel threads that must then be joined
	- ![[Pasted image 20260212140225.png]]
	- When a thread completes its work, it joins with the master thread
	- Parallel regions may be nested
## Basic Example
![[Pasted image 20260212141207.png]]
- Must allocate number of threads
	- This creates a pool of threads that will be reused
	- Cost of spawning threads is minimized
- Use the `omp parallel` pragma directive
- Enclose parallel region in curly braces
- End curly creates an implicit synchronization barrier that waits for all threads to join
- Code after the region is executed only by the master thread
# Computing Pi (Riemann Sum) Example
![[Pasted image 20260212141609.png]]
## Serial Version
```c
#include <stdio.h>
#incude <omp.h>

int main() {
	int i;
	double x, pi, sum = 0.0;
	long num_steps = 100000000;
	double step = 1.0 / (double) num_steps;
	double start = omp_get_wtime();
	
	for (i = 1; i <= num_steps; i++) {
		x = (i - 0.5) * step;
		sum = sum + 4.0 / (1.0 + x * x);
	}
	
	pi = step * sum;
	double run_time = omp_get_wtime() - start_time;
	
	printf("\n pi with %ld million steps is %lf in %lf seconds\n", num_steps / 1000000, pi, run_time);
}
```
- Takes 375ms
## Parallel Version 1
```c
#define MAX_THREADS 4
int main() {
double pi, full_sum = 0.0;
double start_time, run_time;
double sum[MAX_THREADS];
long num_steps = 100000000;
double step = 1.0 / (double) num_steps;
#pragma omp parallel
{
	int i;
	int id = omp_get_thread_num();
	int numthreads = omp_get_num_threads();
	double x;
	sum[id] = 0.0;
	if (id == 0) printf(" num_threads = %d",numthreads);
	for (i = id; i < num_steps; i += numthreads) {
		x = (i + 0.5) * step;
		sum[id] = sum[id] + 4.0 / (1.0 + x * x);
	}
}
for (int i = 0; i < j; i++) full_sum += sum[i];
pi = step * full_sum;
run_time = omp_get_wtime() - start_time;
printf("\n pi is %f in %f seconds %d thrds \n", pi, run_time, j);
}
```
- Create an array of sums where one thread gets one entry in the array
	- This array is global (shared) between threads
	- Divide steps evenly among threads
- Master thread performs final sum
- ![[Pasted image 20260212142647.png]]
	- Speedup is chaotic and mostly insignificant
### False Sharing
- ![[Pasted image 20260212142929.png]]
- Threads on different cores read and write words within the same cache line
	- The array is contiguous and takes up one cache line
- When one thread writes to the sum array, its cache line is marked as dirty
- It is flushed back to RAM and reread before another thread can access it
- The threads compete with each other to read the cache line
- This is called **False Sharing**
## Version 2: Padding Arrays
![[Pasted image 20260212143308.png]]
- `double sum[MAX_THREADS][PADDING]`
- The padding value is dependent on how many doubles fit in a cache line for this machine
- Allocate rows of the sum array for each thread
- Kind of stupid, you waste a lot of memory space
- ![[Pasted image 20260212143402.png]]
- You get incremental, almost linear speedup as more threads are added
## Version 3: Critical Section
```c
#define MAX_THREADS 4
int main() {
double pi, full_sum = 0.0;
double start_time, run_time;
double sum[MAX_THREADS];
long num_steps = 100000000;
double step = 1.0 / (double) num_steps;
#pragma omp parallel
{
	int id = omp_get_thread_num();
	int numthreads = omp_get_num_threads();
	double x;
	double sum = 0.0;
	if (id == 0) printf(" num_threads = %d",numthreads);
	for (int i = id; i < num_steps; i += numthreads) {
		x = (i + 0.5) * step;
		sum += 4.0 / (1.0 + x * x);
	}
	#pragma omp critical
	pi += sum * step;
}
run_time = omp_get_wtime() - start_time;
printf("\n pi is %f in %f seconds %d thrds \n", pi, run_time, j);
}
```
- Create a critical region within the parallel code to access the global pi variable and increment it
- Eliminates the final sum step for the master thread
- Eliminates memory overhead of padding'
	- And programmer difficulty of knowing the cache scheme and array ordering
- Speedup is just as fast
- ![[Pasted image 20260212143908.png]]
### Version 3.5: Atomic Operations
- A block or statement can sometimes be marked as atomic
- The compiler can enforce atomicity either using a lock or an atomic instruction
- Atomic instruction like fetch and add
- Critical section is more general, atomic may be more efficient if applicable
```c
#define MAX_THREADS 4
int main() {
double pi, full_sum = 0.0;
double start_time, run_time;
double sum[MAX_THREADS];
long num_steps = 100000000;
double step = 1.0 / (double) num_steps;
#pragma omp parallel
{
	int id = omp_get_thread_num();
	int numthreads = omp_get_num_threads();
	double x;
	double sum = 0.0;
	if (id == 0) printf(" num_threads = %d",numthreads);
	for (int i = id; i < num_steps; i += numthreads) {
		x = (i + 0.5) * step;
		sum += 4.0 / (1.0 + x * x);
	}
	#pragma omp atomic
	pi += sum * step;
}
run_time = omp_get_wtime() - start_time;
printf("\n pi is %f in %f seconds %d thrds \n", pi, run_time, j);
}
```

# Types of Synchronization
## Mutual Exclusion (Critical Section)
- `#pragma omp critical`
- `#pragma omp atomic`
- Reduction in loops
- Also have API for explicit lock/unlock function calls
## Barrier
- Global synch, all threads must reach barrier before any continues
- OpenMP: Implicit barrier at the end of any parallel region
	- Can avoid with `nowait` clause
- ![[Pasted image 20260212144517.png]]
## Point-To-Point
- Also called flag, event, or eureka synchronization
- ![[Pasted image 20260212144712.png]]
- Task $n+1$ must ensure task $n$ has completed some amount of work before continuing
- Task $n$ will post that it is done, and task $n+1$ will wait until that post flag has been raised
- Not explicitly supported by openmp
- ![[Pasted image 20260212144913.png]]
- We need understanding of memory consistency to get this right
- Can use atomic and flush directives for memory consistency
# Loop-Based Parallelism
- Loops are good places to look for concurrency
- OpenMP loop constructs allow programmer to easily transform a sequential loop to a parallel one
	- Loop body is a structured block
	- It is a task, but be careful of loop-carried dependencies
	- Automates assignment of tasks to threads, allows easy experimentation
	- Supports nesting of parallel loops
- ![[Pasted image 20260212145340.png]]
- The `#pragma omp for` directive is more concise and declarative
## Default variable scoping
- ![[Pasted image 20260212145642.png]]
- Loop indices are private, even if declared outside the loop
	- This includes loop variables for nested loops within the loop body
- Vars declared inside the loop are private
- Everything else is shared
## Default Scheduling
- Scheduling is the assignment of loop iterations fo threads
- Default is to statically group equal sized chunks of iterations, based on loop index
	- ![[Pasted image 20260212145843.png]]

# Variable Scoping Options

| `shared`       | All threads access the global var                                                                                              |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| `private`      | Separate uninitialized variable is allocated for each thread                                                                   |
| `firstprivate` | Separate variable is allocated for each thread, init with global value                                                         |
| `lastprivate`  | Separate variable is allocated for each thread. The global variable is updated with the value of the sequentially last thread. |

# Pi Code Version 4
```c
#pragma parallel for
for (i = 1; i <= num_steps; i++) {
	x = (i - 0.5) * step;
	sum = sum + 4.0 / (1.0 + x * x)
}
```
- Problems:
	- i is private so there is no problem
	- x is shared and is read and written to, there are dependencies 
	- step is shared but only read from, no problem
	- sum is shared and r/w, so there is a dependence
```c
#pragma parallel for private(x)
for (i = 1; i <= num_steps; i++) {
	x = (i - 0.5) * step;
	sum = sum + 4.0 / (1.0 + x * x)
}
```
- OpenMP allows x to be explicitly declared as private
	- You can also declare x within the for loop
## Reduction Variable
- Combining values into a single shared accumulation variable is a pattern called reduction
- If the combining operations is commutative and associative, it is straightforward to compute partial results or combine them
	- Commutative: Order of operands does not matter
	- Associative: Order of operations does not matter
- The OpenMP `reduction` clause specifies a reduction operation and variable
```c
#pragma parallel for private(x) reduction(+:sum)
for (i = 1; i <= num_steps; i++) {
	x = (i - 0.5) * step;
	sum = sum + 4.0 / (1.0 + x * x)
}
pi = sum * step
```
![[Pasted image 20260212151105.png]]
![[Pasted image 20260212151215.png]]
- `#pragma omp single` 
	- Specify the debug statement of how many threads are being used as an operation to be performed only once

# Scheduling Options
## Static
- `schedule(static[,chunk])`
- Assigns blocks of size chunk to threads
- Default chunk is approximately equal subdivision of total iterations
## Dynamic
- `schedule(dynamic[,chunk])`
- Each thread pulls chunk iterations from queue until empty
- Default chunk is 1
- Used when amount of work is unpredictable per iteration
	- 100 iterations may take a lot of time or none at all
	- We want to equally divide work not iterations
## Guided
- `schedule(guided[,chunk])`
- Each thread pulls iterations from a queue until empty
- Size of block starts large and decreases to chunk
- Default chunk is 1
- 
## Auto
- `schedule(auto)`
- Allow runtime to choose
## How to choose
![[Pasted image 20260212151954.png]]

# Nested Loops
- 
- Both i and j will both be private for each thread
- The work will only be split along the loop dimension associated with the pragma directive
- ![[Pasted image 20260212152039.png]]
	- In this example, each thread will iterate over the j dimension M times
- ![[Pasted image 20260212152230.png]]
	- The parallel region is only the j loop
	- There are N barriers for synchronization
	- Synch overhead is too large here
## Collapse Clause
- ![[Pasted image 20260212152422.png]]
- Creates a single NxM iteration loop
- Useful when N is close to the number of threads, which could make balanced scheduling of inner loops more difficulty
	- If there are 4 threads, and i is 6, 2 threads will have 2 iterations and 2 will have only 1
	- Better to unroll the i loop and parallelize the resulting loop
## Nested Parallel Loops
- ![[Pasted image 20260212152720.png]]
- Use 16 threads, where each of the 4 i threads spawns 4 more j loop threads
- May be safe to add the nowait clause on the inner loop
	- Prevent synch overhead

For class #parallel-arch