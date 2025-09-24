Related to [[The Memory Hierarchy]]
# ARM Cortex M0 Core
- The lowest power, smallest ARM processor
- Ultra low power
	- Consumes $3\mu\text{W/MHz}$
- Simplicity
	- Only 56 instructions
## Cortex-M0 meaning
- M stands for microcontroller
	- A series devices can run a full OS
	- Higher numbers correspond to more powerful processors

|          |                    |                                                                                                                               |                                                  |
| -------- | ------------------ | ----------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------ |
| Core     | Performance        | Features                                                                                                                      | Common Use Case                                  |
| M0       | 🟢 Lowest          | Basic Thumb instruction set, no hardware divide, no NVIC priority levels (“Thumb” is a 16-bit compressed ARM instruction set) | Low-cost MCUs like STM32F0                       |
| M0+      | 🟢 Slightly better | Even lower power, two-stage pipeline                                                                                          | Energy-efficient MCUs (e.g. NXP, newer ST chips) |
| M3       | 🟡 Medium          | More instructions, better performance, full NVIC                                                                              | General-purpose MCUs (e.g. STM32F1)              |
| M4       | 🟡 + DSP           | M3 + DSP instructions + optional FPU                                                                                          | Signal processing on MCUs (e.g. STM32F4)         |
| M7       | 🔴 High            | High performance, cache, dual-issue                                                                                           | Complex real-time control (e.g. STM32H7)         |
| M33, M55 | 🔴 Secure          | TrustZone, Helium SIMD, secure IoT                                                                                            | Advanced embedded applications                   |
# Internal I/O
![](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUcbsZnNq6C2eos5MlLGCPhp5ymRzIssIhLq-Ax5t0UIgL6uOjL334coYZvuNl8HxhOVTqPW2_w-GrEpcs-cMPrOtdnrcy9WVXOzcWuJ4LbzjL8E0LNVDz9ysbxTh6fhKPHvyvnm9Q=s2048?key=yG271hTcZpEWC1VUiGUliw)
## Bus Matrix
![[Pasted image 20250827163429.png]]
- The **System Bus** connects the M0 core system bus to the Bus Matrix, which manages arbitration between the core and the DMA
	- The arbitration uses a round-robin algorithm
	- This simply cycles priority access between the requestors
	- Access to and from the CPU is arbitrated entirely through this Bus Matrix
- The **DMA Bus** connects the AHB master interface of the DMA to the AHB slave interface of the Bus matrix
	- This manages access of CPU and DMA to SRAM, flash, and the peripherals
- The **Bus Matrix** is composed of:
	- 3 **MASTERS**
		- CPU
		- DMA1 and DMA2
	- 4 **SLAVES**
		- FLTIF
		- SRAM
		- AHB1 with AHB to APB bridge
		- AHB2
- AHB peripherals are connected on system bus through the Bus Matrix to allow DMA access
## AHB to APB Bridge
- **AHB (Advanced High-performance Bus*
	- Used for high speed memory and DMA access
- **APB (Advanced Peripheral Bus**
	- Simpler and optimized for low-power, low-latency comms with peripherals
- The **AHB to APB** bridge
	- Provides full synchronous connections between the AHB and APB buses
	- After each device reset, all peripheral clocks are disabled (Except for SRAM and flash)
	- Before using a peripheral, its clock must be enabled in the RCC_AHBENR, RCC_APB2ENR, or RCC_APB1ENR register
# Memory Organization
- Program memory, data memory, registers and I/O ports are organized within the same linear 4GB address space
	- 32-bit address space
- The bytes are coded in memory in **Little Endian format**
	- ![[Big-endian-and-Little-endian.png]]
	- The lowest numbered byte in a word is the word's least significant byte
	- Backwards format
	- Little endian example
		- Word: "race"
		- Byte address 0 is e, 1 is c
		- Opposite of string slicing
- Addressable memory space is divided into **8 main blocks** of **512 MB** each
- ![](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUcT_315dghhQVQ8nOQaPeRt9gBKEFDMjBZ9AXyoGDJAq_OklwQrL8vlKnrInawkDTRxLD4iNi6Roif1pNIWw2IK-pZFmyWZUZyNbamMRtQTEb_8EOLhdGbjsmlClLnlbEW-J48azQ=s2048?key=yG271hTcZpEWC1VUiGUliw)
	- This map is generic to all STM32F0x1 MCUs
	- Some boundaries aren't notated because they could be different for different mcus in the family
## Calculating Memory Alignment
- Notice that the memory map diagram indicates the main flash memory begins at address 0x0800 0000, but does not indicate the upper bound
- If the STM32F091 has 256KB of main flash, what is the upper boundary?
	- 256KB = $256 * 2^{10}$ bytes = 0x0004_0000
	- 0x0800_0000 + 0x0004_0000 = 0x0804_0000
	- 0x0804_0000 is not the upper limit, however, because 0x0800_0000 is itself a valid address. We must subtract 1 to account for this
- Thus, the range of the main flash address space is **0x0800_0000 - 0x0803_FFFF**
- This is confirmed by the documentation:![](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUerRk9PsP3q2NPsHHDVu1Xfv6DYtZb9kYDCPxl19UkcdYnWB-w33aG2F9QmqKOkNWgfRDPBjM4HdG5vuMM02zssc29dFvthj7SIcp2I0nRE7NM2WKOeAxz8YVUNDBMXYfEaU6jvHw=s2048?key=yG271hTcZpEWC1VUiGUliw)

For class #embedded
