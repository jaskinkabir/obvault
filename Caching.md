Continues [[The Memory Hierarchy]]
Continued by [[Cache Performance]]
# Direct Mapped Cache
- Map the large address space of the data memory to the much smaller address space of the cache through a direct mapping where each memory location points to just one cache location
	- $\text{Block Address = }\text{(Mem Address)}\ \% \ \text{(\# of Blocks in Cache)}$
- If the number of cache locations is a power of 2, the modulo can be calculated simply by masking the lower order bits of the memory address
	- For an $N$-block cache:
		- $BA=$ Block Address
		- $CI$ = Cache Index
		- $CI = BA[0:\log_{2}N]$
	- If the number of blocks is 8, 
		- $CI = BA[0:3]$
		- Lower 3 bits
## Tags
- Each cache block could point to a number of different memory locations
	- Some mechanism must be in place to ensure that the data in the cache is the data that the CPU requested
	- Add a set of tags to the cache
		- Each tag is simply the $N-\log_{2}N$ bits not used to index the cache
			- If memory addresses are 5 bits, and there are 8 cache blocks, the tags would be 5-3=2 bits wide
- If a cache block has not been written to yet, its data is invalid and should not be used
	- The CPU must be able to recognize this
	- Add a valid bit to the block that is high when there is valid data within that block
- This scheme utilizes temporal locality
## Leverage Memory Alignment
- If bytes are aligned in memory, each address points to a single byte within a word.
	- If each word is 4 bytes, then the lower 2 bits of the address represent a byte within the word
	- This means that if the cache stores 4 byte words, the lower two bits of the address can be ignored.
- ![[Pasted image 20241203190320.png]]
	- The 64-bit address points to a byte in memory
	- The lower two bits are the byte offset
		- Bye = Address[0:1]
	- The upper 62 bits point to a word in memory
	- The lower 10 bits of this address point to a cache block
		- Index = Address[2:11]
	- The upper 52 bits are the tag field
		- Tag = Address[12:63]
## Cache Specifications
- $a=$ Address width
	- Assume $a=64$
- $n=$Width of cache index
	- Cache size is $2^{n}$ blocks
- $m=$Width of word address within a block
	- $2^m=$ Words per block
	- $2^{m+2}$ Bytes per block
	- $2^{m+5}$ Bits per block
- $v=$Width of valid field
	- Typically just 1
- Width of Tag Field = $a-n-m-2$
- Total number of bits in cache
	- $2^{n} \times [\ 2^{m+5}+(a-n-m-2)+v\ ]$
		- Number of blocks in cache * (number of bits per block + tag size + valid size)
		- Data plus metadata
	- While this is the true size in bits, the convention is to only count the size of the data
	- Thus cache size is typically just listed as $2^{n+m+5}$ bits
		- number of cache blocks * bits per block
### Example Problem
- Consider a cache with 16 KiB of total data, with a 4 word block size and a 64-bit address. What is the cache size in bits?
	- Data = $16*2^{10}$ bytes = $2^{12}$ Words
		- 4 words per block
			- $m=\log_{2}4=2$
			-  $\frac{2^{12}}{4}$ blocks = $2^{10}$ blocks
			- $n=10$
	- $m=2$
	- $n=10$
	- $v=1$
	- Cache size = $2^{10}  \times [2^{7} + (64-10-2-2)+1]$
	- $= 2^{10} \times [2^{7}+51]$
	- =$179*2^{10}$= 179 Kibibits
- New problem. $a=64$, data = $2*2^{10}$ bytes, block size = 2 words
	- Data = $2*2^{10}$ bytes
		- $2^{9}$ Words
		- 2 words per block
		- $2^{8}$ blocks
	- $a=64$
	- $m=1$
	- $n=8$
	- tag = $64-8-1-2=53$
	- cache size = $2^{8} \times [2^{6}+ 54]$
	- $2^{8} \times 118$
### Mapping an address to a multi-word cache block
- Consider a cache with 64 blocks and 16 bytes (4 words) in each block
- From byte address
	- Block address = $\text{Byte Address} / \frac{\text{Bytes}}{\text{Block}}$
- In what block does byte address 1200 map?
	- block address = $1200 * \frac{1}{16}=75$
- Block number = block address % # of blocks
	- Byte address 1200 lies within 75 % 64 = block # 11
	- Block #11 contains all byte addresses between 12000 and 1215
### Why not just increase block size
- Miss rate goes down with increased block size because of the spatial locality
- However, past a certain point the miss rate actually increases
	- This is because the number of blocks that can be held in the cache decreases
	- Desk analogy
		- You pick up a bunch of small pamphlets and put them on your desk
			- The pamphlets don't have a lot of information in them, you may need to constantly go back to the shelves to get more
		- Get bigger books
			- Now each book has more info, you don't need to get more books
		- Get 2 or 3 massive encyclopedias that take up your whole desk
			- If you need a bit of info from another book, you have to put the entire encyclopedia back onto the shelf to get another book, before you even need the entire encyclopedia
- The miss penalty also increases, as you need to access more data from memory to fill the block
	- Need to go grab a bigger book
# Handling Cache Misses
## Data Miss
- The control unit will initiate a pipeline stall when the cache control unit detects a miss
	- Out of order CPUs may execute other instructions while waiting for the cache miss to be resolved
## Instruction Miss
1. Zero out IF/ID register to initiate stall
2. Send original PC value to the memory
	1. PC-4
3. Instruct main memory to read from this address
4. Write the cache entry
5. Restart instruction fetch
	1. This time, the instruction will be found in cache
# Handling Writes
## Write-Through
- Suppose a memory write instruction is executed
- It writes this data into the data cache but not the system memory
- In this case, the cache and memory are inconsistent
- The simplest way to solve this is called **Write-Through**, in which memory write instructions write to both the system memory and the cache
## Write Buffering
- Memory writes are very slow, oftentimes on the order of hundreds of CPU clock cycles
- A simple way to handle this is to write all changes in the cache to the memory (write-through)
	- Read value from the cache
	- Modify value
	- Write modified value to cache and memory
- However, if the CPU has to wait for a memory write on every single store instruction. the performance will be heavily impacted
- One solution is using a **Write Buffer**
	- A queue that holds data while it is waiting to be written to system memory
- Whenever a piece of data from the write buffer is written to the data memory, that position in the write buffer is freed and can now accept another write from the CPU
	- If the write buffer is full when the CPU needs to store data, a stall must be initiated to wait for a new slot to be freed
## Write-Back
- In a **Write-Back** scheme, whenever a write occurs, the new value is written only to the block in the cache. The modified block is written to the lower level memory whenever it is replaced upon a cache miss
For class #comporg$$