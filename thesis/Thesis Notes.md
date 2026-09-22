# Task Overview
- Program for green core to run is compiled into an input ELF containing code and input data
- This ELF must be objcopy'd before the GC can execute it.
- The question is whether the white core does this or the DMA core
## Task
1. Parse ELF
2. Objcopy ELF
3. DMA ELF into BRAM


DMA for GPU programming? 
# The Output ELF
- The program could create an output ELF in BRAM containing the return values
- The addresses in the program header fields of this ELF could be used in one of two ways
1. The addresses could be meaningless and all set to 0
	1. This would let the WC decide where it wants to place each return value into its memory (for dynamic memory allocation)
	2. The logic for DMA'ing the data out of the BRAM then becomes more complex.
	3. Someone, either the WC or some hardware core, must figure out where to place the return values in DDR
	4. This must somehow be communicated to the DMA core
2. The addresses could be set relative to the beginning of a buffer the WC has already allocated for the result
- This ELF must then also be Obcopy'd somehow


## BRAM Controller or AXI Master?
- If the ELF DMA core is a bram controller it can be directly connected to the BRAM, saving the resources that would otherwise go to an AXI BRAM controller?
	- We should probably verify the resource thing with a raw lut count comparison
	- However, if there is a circumstance where one of the BRAMs is never being used, its ELF parsing logic is being wasted
- If the ELF DMA core instead has one (or two) AXI master(s), we can have a pool of DMA cores
- 


# Prelim Results
## Timing
- The HLS core is significantly faster
- The bulk of the time is spent on the objcopy, so it is the biggest bottleneck
No cold start:
![[Pasted image 20260623205502.png]]

Cold start:
![[Pasted image 20260623205533.png]]
- I suspected that the cpu was caching the objcopy which isn't realistic
- I made the script clear caches before each objcopy to eliminate that variable
- The CDMA transfer takes longer because the flat file must be put into a PYNQ buffer before it can be DMA'd
## Resources

| **Name**              | **CLB LUTs** | **CLB Registers** | **CARRY8** | **F7 Muxes** | **CLB** | **LUT as Logic** | **LUT as Memory** | **Block RAM Tile** | **BUFG_PS** | **PS8** |
| --------------------- | ------------ | ----------------- | ---------- | ------------ | ------- | ---------------- | ----------------- | ------------------ | ----------- | ------- |
| **dma_platform_i**    | 15340        | 20738             | 79         | 39           | 2939    | 11971            | 3369              | 17                 | 1           | 1       |
| **objcopy_0**         | 1619         | 2078              | 61         | 24           | 403     | 1551             | 68                | 1                  | 0           | 0       |
|  **axi_smc**         | 12613        | 17003             | 4          | 4            | 2433    | 9398             | 3215              | 0                  | 0           | 0       |
|  **axi_intc_0**      | 74           | 77                | 0          | 0            | 20      | 74               | 0                 | 0                  | 0           | 0       |
|  **axi_cdma_0**      | 859          | 1268              | 14         | 10           | 180     | 776              | 83                | 0                  | 0           | 0       |
|  **axi_bram_ctrl_0** | 166          | 269               | 0          | 1            | 79      | 166              | 0                 | 0                  | 0           | 0       |
- Comparing the HLS core to CDMA + AXI BRAM Controller:
- CDMA + BRAM Controller uses significantly fewer resources
	- 36% LUTs
	- 26% Registers
	- 35% Area
	- Saves a BRAM Tile (For header buffer)

# TODO
- Find resource numbers with a riscv
- Analyze why core is so large
- Read barrel paper
	- Compare costs
- Back of envelope, 1vs10vx1000vsmillion cores resource values and timing

# Back of Envelope
- The LUT count for the ELF DMA HLS core is slightly larger than the RISC-V core itself
- Why should I spend resources on a single function when I could use it on an entire CPU core?
- Because of this
- ![[Pasted image 20260626165710.png]]
- This is the best case scenario for a 1000 core system with a 96 core host CPU
- There is only one ELF that needs to be transferred to all 1000 cores
- The objcopy to generate the flat image takes 24 milliseconds
- We make these assumptions
	- 8 Active DDR->PL transfers can occur at once, since DDR only has so many channels
	- There are as many CDMAs/ELF DMAs as there are cores
- By offloading the objcopy to the PL, and interleaving the ELF parsing with the DMA, we save a huge amount of time
- For the worst case, assume each of the 1000 cores needs a separate ELF
- ![[Pasted image 20260626165927.png]]
- Assume we have 16 cores to parallelize the objcopies across
- The programming time for MMIO and CDMA becomes over a second and a half due to the objcopies
- This is unacceptable for a dynamically reprogrammable system
- However, the HLS approach eliminates this overhead and stays at 50ms to program the entire system




for topic #thesis