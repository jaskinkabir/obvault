e[[Embedded Startup Process]]
# Bootloaders in General Computing
- On a typical PC, the power button first begins execution of firmware stored in non-volatile memory
	- Historically the BIOS 
	- In modern systems, UEFI (Unified Extensible Firmware Interface)
- Role is to initialize basic hw
	- Mem controller
	- detect disks
	- Perform self tests
- Firmware then hands control to program on storage device; this is the bootloader
- Bootloaders on PCs (Like GRUB or Windows Boot Manager) are complex because they must load the OS kernel from a disk partition into RAM
- Reside in a small, well-known location (Master Boot Record on BIOS systems)
- Once loaded, bootloader reads a filesystem, finds OS kernel, loads to memory, and jumps to the entry point
- Kernel takes over and continues startup
- A bootloader's **main purpose** is to act as a **bridge between the hw power-on state and an executable program**
- Its tasks are
	- Setup execution environment
	- Transfer control to the main software image
# Bootloaders in Embedded Systes
- Embedded systems are different from GP computers
	- No disk/filesystem
	- Run a single dedicated app
	- Resource constrained
## Example Application
- Imagine an industrial sensor node deployed in a remote location
- It may need to receive firmware updates after deployment
- Without a bootloader, updating that firmware would require physical access and a hardware programmer
- With a bootloader, the device can receive firmware updates over a network connection
- The main purpose of bootloaders on an embedded system is to flash new code over an interface other than the hardware programming interface (JTAG, UART, etc)
# STMF091RC Boot Process
- When the chip is reset, the core performs two memory reads
	- It reads the 32 bit value at address `0x0800 0000` and loads it into the main stack pointer
	- Reads the 32-bit value stored at address `0x0800 0004` and loads it into the program counter
- The second value points to the reset handler, which begins your firmware
# Boot Modes
- The STM32F0 family determines its boot mode through the level of its BOOT0 pin
	- 0: flash
	- 1: ST factory bootloader
# ST System Bootloader
- Held in a small, protected region of ROM
- Process:
1. Peripheral Initialization: 
	1. ROM bootloader configures peripherals with predefined settings so it can listen for commands
2. Communication Detection: 
	1. Waits for synch bye (typically `0x7F`) on one of the interfaces
	2. When communication is detected, establish protocol session with the host
3. Command handling:
	1. Bootloader accepts commands such as
		1. Read mem
		2. Write mem
		3. Erase mem
		4. Jump to user app
	2. Simple-byte oriented protocol defined by ST
4. Flash Programming
	1. Bootloader receives binary data and writes into Flash memory starting at `0x0800 0000`
	2. Handles flash erase and program operations internally
5. Application Launch
	1. After programming is complete, host can send a "Go" command, telling the bootloader to jump to the application code's reset vector
# Custom Bootloaders
- A custom bootloader resides at the beginning of flash memory 
- The main application is then placed higher in flash
- The split is managed by the linker script
- On reset, the MCU will start executing from the bootloader
- The bootloader will then decide whether to stay in bootloader mode (if it detects a new firmware image for example)
- Or jump to the main application
# Jumping to the Application
- The bootloader must
	- Read the application's vector table
		- First word contains new Stack pointer, second the reset handler address
	- Reconfigure the vector table offset register
	- Set MSP and PC registers
- ![[Pasted image 20251106162356.png]]

# Why Create Custom Bootloader?
- Control and flexibility
	- The built-in ST bootloader is fixed in ROM and cannot be edited
	- The peripherals it uses, its baud rate, or protocol cannot be modified
	- A custom bootloader can implement exactly the communication and update logic the application requires
	- For example: firmware updates over CAN or USB
- Field updates
	- In remote deployments, firmware updates must be possible without direct physical access
	- Custom bootloader can check for a new firmware update and load it into flash
- Security
	- Custom bootloaders can include cryptographic checks to ensure only authenticated firmware is executed. The bootloader can verify some sort of digital signature before jumping to main code
- Fail-Safe Operation:
	- If something goes wrong with the main application, the bootloader can detect this and revert to a known-good backup image
# Bootloader Memory Organization
- A custom bootloader occupies the beginning of flash, and the user application is placed at a higher address
- ![[Pasted image 20251106163250.png]]
- The linker script must be adjusted to reflect this offset so that its vector table is placed at `0x0800 4000` instead of `0x0800 0000`
## Why Update the Vector Table Offset Register
- The interrupt vector table of the main application now resides at a different location than the bootloader's
- Before jumping to the main application, the CPU must be told that it should look in a new location for ISRs
# How Bootloader Decides To Update Or Jump
- Timed Detection Window:
	- After power-on, bootloader waits a short period to see if any communication activity occurs
	- If there is activity, flash new firmware. Else run main app
- GPIO Trigger:
	- Bootloader checks a specific input pin or jumper to see if firmware must be updated
- Software flag: 
	- Main application can request the bootloader to run next time by setting a flag in non-volatile memory
	- Bootloader checks this flag at startup
- Checksum or Signature Verification:
	- Bootloader validates integrity of main image. If checksum is invalid, it assumes the firmware is corrupted and stays in update mode
# What if the Bootloader Misses the Firmware Update Signal
- In ST's factory Bootloader, the ROM bootloader waits indefinitely for a valid synch sequence from a peripheral. 
	- Continually polls comm interfaces for firmware
	- To exit, the mcu must be reset
- In a custom bootloader, there is typically a timeout
# Changing How MCU Boots
## BOOT0 pin
- Jumper control
- Controlled by software through option byte
## Option Bytes (software config)
- STM32 includes option bytes: special Flash regions that control
	- Startup behavior
	- Watchdog config
	- Readout protection
	- Other system-level parameters
- By modifying these, you can define custom boot addresses, enabling dual-bank memory config or alt boot modes
## Software Bootloaders (Jump from Code)
- Custom firmware can deiberately invoke the system bootloader, or jump to another program in memory
- A firmware update command in the application could look like this
- ![[Pasted image 20251106165432.png]]



For class #embedded