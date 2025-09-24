# PLB Processor Local Bus
- 64-bit data, 100MHz full-featured bus
- 1600MB/s peak bandwidth, 533 typical
- Multiple masters/slaves
- Complex interface
- Requires a relatively large amount of CLBs
# LMB Local Memory Bus
- 32-bit data, 125MHz processor/memory bus
- 500MB/s peal 333MB typical
- One master, one slave
# OPB On-Chip Peripheral Bus
- 32-bit data, 100MHz compromise bus
- 500MB/s 167 typical
- Simple interface
# FSL Fast Simplex Link Bus
- 32-bit ddata, 100MHz point-to-point bus
- Fast, FIFO interace
- Direct connection to microblaze
# DCR Device Control Register
- 32 bit data but 10-bit address special purpose bus
- Simple low bandwidth communication with very high connectivity
- Avoids taking cycles from high-speed busses like PLB
# OCM On-Chip Memory Bus
- 32-bit data
- Either instruction or data requests
- +500M/s typical bandwidth
- Very low latency, directly connects processor to BRAM
- Predictable memory performance for a range of address spaces

For class #reconfig 