Continues [[8 Great Ideas in Computer Architecture]]
Continued by [[Caching]]
# Locality Principles
## Temporal Locality
- If a data location is referenced, it will tend to be referenced again soon
## Spatial Locality
- If a data location is referenced, locations with nearby addresses will tend to be addressed soon
# Memory Hierarchy
- Speed is inversely related to size and related to cost
- Have a hierarchy of memory technologies organized from cheap, large, slow memory at the bottom and expensive, small, fast memory at the top
	- Processor Registers
	- CPU Cache (SRAM)
	- System Memory (DRAM)
	- Persistent drives
		- May be further split into flash and Magnetic disk drives
- The data itself is also hierarchical in this way
	- Any data on any given level is a subset of the data stored on every lower level
	- All data is stored at the lowest level
- Data is only copied between two levels at a time
## Block/Line
- The minimum unit of information that can either be present or not present in a cache
# Hits and Misses
- If the data requested by the processor appears in some block in the upper level of memory that it is searching within, this is called a **Hit**
	- If not, this is a **Miss**
- **Hit Rate:** Is the fraction of memory accesses found in a level of the memory hierarchy
- **Miss rate**: Inverse of Hit rate
- **Hit Time:** The time it takes to access a block in some level of memory
	- Including the amount of time required to determine if the block is present or not (hit or miss)
- **Miss Penalty**: The time required to fetch (copy) a block into a level of the hierarchy from a lower level
	- Includes block access time, transmission time, insertion time, and time to pass data to requestor
	- This should be called miss time what the fuck
# Memory Technologies

## SRAM: Static RAM
- ICs with (usually) a single access port that can provide either a read or a write
- Have a fixed read time and a fixed write time no matter what data is accessed
- Don't need to refresh, so access time is close to cycle time
- Uses 6-8 transistors per bit for redundancy/stability
- Typically 3 levels of sram cache
## DRAM: Dynamic RAM
- In SRAM, values persist so long as power is applied
- DRAM can hold values as long as charge remains in the capacitor
	- A single transistor is used to access this stored charge, either to read or write
- DRAMs store data as charge on capacitors, and so the data must be periodically refreshed
	- This is why this tech is called **Dynamic** RAM
	- Refreshing just means reading the data and writing it back
	- Typically, the two-level decoding structure allows for every 3 cycles to be refresh-read-write
		- Refresh an entire row at once
### DRAM Organization
- DRAMs are organized in banks
	- Each bank consists of a series of rows
	- Sending a PRE (precharge) command opens or closes a bank
	- A row address is sent with an ACT(activate), which causes the row to transfer to a buffer
	- From this buffer, the data can be transferred by column
	- Each command, as well as block transfers, is  synchronized with a clock
### SDRAM
- By adding a clock input onto the DRAM, the time for the CPU and RAM to synchronize is eliminated.
- The bits can be transferred in bursts without having to specify additional address bits
	- The clock transfers successive bits in a burst
	- In Double Data Rate or **DDR**, data is transferred on both the rising and falling edges of the clock
	- In the specification: DDR-3200, the 3200 represents millions of transfers per second. As such, the clock for such a DRAM would have to be 1600MHz
## Flash Memory
- A type of Electrically Erasable programmable read only memory (EEPROM) 
- Writes can wear out flash memory bits
- Flash memory devices contain a controller that spreads writes evenly
	- Remap blocks that have been written to many times to less used blocks
	- This is called wear leveling
## Disk Memory
### Disk Organization
- Each disk surface is divided into concentric circles called tracks
- Each track is divided into sectors, which are typically 512 to 4096 bytes in size
- The sequence recorded onto the disk is the sector number, the information for that sector including the error correction code, a gap, the next sector number and so on
- Sequential blocks may not be placed sequentially on the same track
	- To reduce seek time
### Disk Access
- The disk heads are connected and move together
	- The term cylinder is used to refer to all tracks under the heads
- To access data, the following 3 step process must occur
	- Position the head over the proper track. This is called **Seek**
		- Disk manufacturers report min, max, and avg seek times
	- Once the sector has been found, the sector must rotate under the head
		- This time is called **Rotational Latency/Delay**
		- Average latency is half a rotation
		- Average Latency = $\frac{1}{2} * \frac{60}{RPM}=\frac{30}{RPM}$
	- The data from the sector must then be transferred to the requestor
		- **Transfer Time** is this time
For class #comporg