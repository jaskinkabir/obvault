# Smart DMA
## Buffering
- Need to pass over all program headers to figure out where the start address is, and if the program will fit in the bram
- We must do one pass of DMAs to get the header info
- After that we can either:
	- 1. Buffer all program headers (128 bits per header), then loop through the buffer to copy the data (uses more space)
	- 2. Do another pass of DMAs to get the addresses back (takes more time, uses more DDR bandwidth)
for topic #thesis