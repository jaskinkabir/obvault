# Designing Hardware
1. Start proj, load board info, choose design entry
2. Add clock/reset (clk_wiz)
3. Choose a processor and type of memory
	1. Microblaze
	2. Block automation
4. Add comm peripheral (axi_uartlite)
	1. Use connection automation
5. Generate HDL products, wrap in top level
6. Generate a bitstream
7. Generate xsa file for vitis
# Coding MCU Software
1. Choose "platform"
	1. Standalone (with Xil* calls)
	2. Linux
	3. Standalone(direct address manipulation)
		1. Also called baremetal
2. Software Application
	1. Choose platform, generate bsp from hardware
	2. create hello world
	3. Cross compile software components
3. Combine Hardware and Software
	1. BIT has hardware config
	2. ELF stored program instructions and initial data values
	3. BOOT.BIN
	4. Other things like linux's device tree and filesystem
		1. Device tree is a way for linux to know what hardware is connected to the system
# Programming Configurable Hardware
## Methods/Technologies
- JTAG
- SD Card
- QPI Flash
## Programming Vs. Flashing
- Programming is writing data into the volatile memory
- Flashing writes data (boot image) into the nonvolatile memory
For class #reconfig