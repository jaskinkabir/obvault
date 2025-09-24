# Execution Time
- Equivalent to response time/delay
- Time between the start and finish of a task
	- Cars travelling at 60kmh across a 1km bridge exit the bridge every minute. The response/execution time is 1 minute
# Throughput
- Also called bandwidth
- Tasks completed per second
	- If several cars are allowed on the bridge with a 100m separation between them, a car can enter and exit the bridge every 6 seconds. The throughput is 1/6 cars per second or 10 cars/minute

# Bottleneck Alleviation Car Example
- Fast cars travel across a 1000m bridge with some fixed speed and separation between them
- ## Case 1: Optimal Utilization
	- Assume the cars travel at 100m/s, and require 100m of separation between them. Cars appear at the entrance of the bridge every 2 seconds
	- ![[Pasted image 20240822203240.png]]
		- Car 1 takes 10 seconds to exit, just like every other car
		- The pipeline is perfectly utilized
	- Execution time: 10s
	- Throughput, 1 car per 2 seconds or 0.5Hz
- ## Case 2: Input Speed Bottleneck
	- Suppose now there is a car appearing every second
	- ![[Pasted image 20240822203335.png]]
		- Now cars queue up at the entrance
		- While the time each car takes the cross the bridge is the same, this queueing time must be accounted for in the execution time
		- The execution time of car 1 is the same 10s. 
			- But now car 6 appears a T4, enters at T10, and exits at T20.
			- Its execution time is 16s, 6s longer than before
	- Execution time: 10-16s
		- Without changing anything about the hardware, we have increased execution time by increasing input speed
	- Throughput: 0.5Hz 
		- Note that this is unchanged
- ## Case 3: Increase Pipeline Stage Speed
	- Suppose the cars now travel twice as fast, at 200m/s
	- ![[Pasted image 20240822203644.png]]
	- We have cut the execution time in half, and done so consistently across all cars
	- Note that the throughput has also been doubled
	- Execution time is 5s
	- Throughput is 1Hz
	- **Increasing the pipeline's execution time improves both overall execution time and throughput**
- ## Case 4: Decrease Pipeline Gap
	- Suppose the cars travel at 100m/s. but only need 100m of separation
	- ![[Pasted image 20240822204010.png]]
	- Execution time is still the same as case 1
		- It is consistent
	- Throughput is doubled (1Hz) compared to case 1 and 2
	- Improving the pipeline gap improves both overall execution time and throughput, thus
		- **Eliminating an input bottleneck improves both overall execution time and throughput!**
# Performance
- A measure equal to 1/execution time
	- Simple as that
## Measuring Performance
- **Wall clock/Response/Elapsed Time**
	- Total time to complete a task, including all sources of delay
- **CPU (Execution) Time**
	- Time the CPU spends completing the task, not including idle time
	- This can be further divided into the following categories
		- **User CPU Time**
			- CPU time spent executing the instructions defined by the task itself
		- **System CPU Time**
			- Time spent in the operating system performing tasks on behalf of the program
- Performance must be given two terms then:
	- **System performance
		- elapsed time
	- **CPU Performance**
		- CPU Time

5ms run
4ms call disk
2ms idle wait for disk
10ms run

For class #comporg