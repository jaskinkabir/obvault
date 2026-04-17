Continues [[Parallelism and Concurrency]]
Continued by [[Dependence]]
Continued by [[OpenMP]]

# Primary Models
![[Pasted image 20260210191610.png]]
## Shared Memory
- Different tasks store and load data into unprotected, shared memory in user space
## Message Passing
- Tasks send data into a channel through sockets
- The channel lives in kernel space
- Accessed through system calls

# MatMul
![[Pasted image 20260210191900.png]]
### Two Task parallelization scheme
- ![[Pasted image 20260210192346.png]]
- Two threads iterate over the multiply accumulate operations
- One thread takes the lower half of indices, the other takes the upper half
#### Problem 1
- ![[Pasted image 20260210192736.png]]
- The problem in this pseudocode is that both threads use the var k to iterate, but they both have separate values of k
##### Privatization
- Create two private copies of k
- Increases memory usage
- ![[Pasted image 20260210192942.png]]
#### Problem 2
- Both threads increment $y[i][j]$
##### Critical Section
- Designate the increment section as critical
- Only one thread can execute it as a time
- Implemented with locks or atomic operations
- Forces serial execution of the code (reduces parallelism)
- ### Final Code
- ![[Pasted image 20260210193803.png]]
#### Results
- Adding the second thread made the code 164 times faster


![[Pasted image 20260210195241.png]]

For class #parallel-arch