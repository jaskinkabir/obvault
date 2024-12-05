Continues [[Cache Performance]]
# Associative Caching
## Fully Associative
- Any block may be placed anywhere in the cache
- To find a given block, all entries must be searched
- To make this search practical, it is done in parallel with a comparator placed at each cache entry
- These comparators are expensive, making fully associative caches only practical for caches with only a few blocks
## Set-Associative Cache
- There are fixed number of locations where each block could be placed
	- An $n$-way set-associative cache has a number of sets, each of which contains $n$ blocks
	- A memory block will map to one and only one set of $n$ cache blocks, but may be placed anywhere in the block
	- Finding a block in cache means:
		- Address the set based on cache index
		- Check every block in the set for a cache hit
For class #comporg
