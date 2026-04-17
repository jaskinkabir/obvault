Related to [[Caching]]
# Static RAM
- fast but not dense
- ![[Pasted image 20260120133436.png]]
![[Pasted image 20260120133523.png]]
- Cross coupled inverters
- ![[Pasted image 20260120133722.png]]
- Can set or reset by applying voltage to either side
- To write: set Word Line high and Bit Line high or low to set value
	- BL' is opposite of bit line
	- BL' creates voltage differential
- To read: set Word Line high and read Bit Line
- Output will be driven by one of two inverters even after set/reset signal is gone
- **Data held so long as power is available**
- **Requires 6 transistors**
# Dynamic RAM
- Dense but slower
- Only needs one capacitor and one transistor
- Much denser
- Leaky, requires periodic refresh
	- Period on the order of milliseconds
- ![[Pasted image 20260120134142.png]]
## Organization
-  ![[Pasted image 20260120134344.png]]
- DRAM has high latency
- Organized into banks and ranks to achieve parallelism
- Can access multiple data locations in a pipeline fashion
- Improves throughput
# Cache Misses
- Cold miss:
	- Address X has never been accessed before
- Capacity miss:
	- Address X was once in the cache, but was pushed out when a different block was fetched
- Conflict Miss
	- Address X has index A, but tag B
	- Address X was once in the cache, but a different block with index A but tag C was accessed, which pushed address X out
	- Address X, was pushed out even though the cache was not full



For class #parallel-arch 