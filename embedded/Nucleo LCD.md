[[SPI]]

| Signal       | Pin  | Type                   |
| ------------ | ---- | ---------------------- |
| Reset        | PA1  | Active low             |
| MOSI         | PA7  | -                      |
| SCK          | PA5  | Rising edge            |
| Command Mode | PB10 | Active low             |
| Chip Select  | PA9  | Active high (From STM) |
- Command should have DC/x low, parameters and rgb data high
- Driver datasheet says CSX falling edge enables SPI and indicates TX start
	- Driver and STM datasheets conflict
# MADCTRL
- The Memory address control register does stuff
- The 3 most significant bits control mcu to memory write direction
- ![[Pasted image 20251023180517.png]]
	- Data from the MCU is written to the memory top to bottom left to right
	- Bits 5,6,7 of the MADCTL register control the physical addresses that the mcu should write to
	- This allows flipping or mirroring certain axes when translating from memory to the display
![[Pasted image 20251023180700.png]]

For class #embedded