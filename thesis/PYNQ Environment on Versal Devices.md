https://ieeexplore.ieee.org/document/10372596
- Ported **much** of the PYNQ functionality to the platform
- This paper runs linux on the CIPS of the Versal
- The OS they make starts from MLAIR
	- MLIR-AIR is a way to program the AI engines
	- It used the PYNQ 2.7 image as a starting point
	- Includes installed PYNQ library that is nonfunctional
- They had to modify the PYNQ Library to work on Versal
	- Versal uses a .pdi file to program the board instead of a bitstream
	- 