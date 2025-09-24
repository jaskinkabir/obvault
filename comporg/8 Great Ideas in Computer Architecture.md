Continued by [[Execution Time and Throughput]]
# Design for Moore's Law
- Architects must anticipate where the technology will be when their design is finished rather than where it is
	- Design architecture for hardware that hasn't been invented yet
	- 'Tick Tock'
# Abstraction
- Increase productivity by abstracting away lower-level details to offer a simpler model
# Speeding up the Common Case
- The **Common Case** is typically simpler than the rare case
	- It is thus usually easier to enhance
- Finding the common case requires careful experimentation and measurement
- Example:
	- The common case for a sports care is transporting one or two passengers, no need to optimize transport of 4 or 5

# Parallelism
- Do thing at same time
# Pipelining

# Prediction
# Hierarchy of Memories
- Registers->Cache->RAM->Storage
- Cache may have different levels
- Storage might split further into SSD, HDD, or virtual memory
- The highest level is the most expensive per bit and the fastest
	- Lowest is cheapest and slowest

# Redundancy

For class #comporg