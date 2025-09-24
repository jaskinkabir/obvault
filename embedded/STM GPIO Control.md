
- Set mode with GPIOx_MODER
	- Mode register
	- Address offset: 0x00
	- Modes:
		- 00 Input
		- 01 GPIO output
		- 10 Alt (passthrough)
		- 11 Analog
- Write to GPIOx_ODR
	- Output data register
	- Read only
- Read to GPIOx_IDR
For class #embedded 