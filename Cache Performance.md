Continues [[Caching]]
Continued by [[Associative Cache Mapping]]

# Measuring Cache Performance
- CPU time can be split into the time spent executing instructions and the time spent waiting for memory accesses
	- $\text{CPU Time} = (\text{CPU Execution Cycles} + \text{Memory-stall cycles}) \times \text{Clock Period}$
- Memory stalls come mostly from cache misses
- Measuring stalls caused by reads is simple
	- $$\text{Read-Stall Cycles} = \frac{\text{Reads}}{\text{Program}} \times \text{Read miss rate} \times \text{Read Miss Penalty}$$
- It is more complicated for writes
	- For write-through, there are two sources of stalls:
		- Write misses, which require fetching the whole block and then writing to memory
		- Write buffer stalls, which requires waiting for a write buffer slot to open before writing to memory
	- Write buffer stalls should, in a sufficiently designed system, become insignificant when compared to the write-miss stalls
	- $$\text{Write-Stall Cycles} = \left( \frac{\text{Writes}}{\text{Program}} \times \frac{\text{Write Miss Rate}}{\text{Write Miss Penalty}} \right) + \text{Write Buffer Stalls}$$
- If write buffer stalls are negligible, the read and write stalls can be combined by using a single miss rate and miss penalty
	- $$\text{Memory-stall cycles} = \frac{\text{Memory Accesses}}{\text{Program}} \times \text{Miss Rate} \times \text{ Miss Penalty}$$
	- $$\text{Memory-stall cycles =  }\frac{\text{Misses}}{Program} \times \text{Miss Penalty} $$
## Example

- Miss rate for instructions is 0.02
- Miss rate for data is 0.04
- Base CPI is 2
- Miss penalty is 100 cycles
- .36 memory accesses per instruction
- How much faster would a processor run with 0 miss rate?
	- $\frac{\text{Instruction Stalls}}{\text{Instruction}} = 0.02 \ \frac{\text{Misses}}{\text{Instruction}} * 100 \frac{\text{Cycles}}{\text{Miss}}=2$
	- $\frac{\text{Memory Stalls}}{Instruction} = 0.36 \text\ \frac{{\text{Mem Access}}}{\text{Ins}} * .04 \frac{\text{Miss}}{\text{Mem Access}} * 100 \frac{\text{Cycles}}{\text{ Miss}} =1.44$
	- $3.44\ \frac{\text{Stalls}}{\text{Instruction}}$
	- CPI with stalls = 5.44
	- Speedup = 5.44/2 = 2.72%
For class #comporg