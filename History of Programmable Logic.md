# PAL


- Programmable array of logic
- Several and and or gates whose connections can be burned in by burning through fuses in between the inputs and the gates
- Can add D-flip flops to the PAL
	- A MUX is added to disable the flip flop
- Add switch boxes in between several PLAs
- This can allow for arbitrary routing between the blocks to create more complex systems
# LUTs and Logic Cells
- An $n-$input LUT has $2^{n}$ SRAM cells connected to a $2^{n}\to1$ mux
- Can generate any $n-$input function
	- Also called a function generator
- A logic cell contains a LUT and a flip flop
# Logic Blocks
- A logic block combines several logic cells
- With special purpose circuitry like add/sub carry chains
- Routing circuitry
# Special Purpose FN Blocks
- Block RAM
- DSP Blocks
- Processors
- Digital Clock Manager
- Gigabit Transceivers

# HDL to Bitstream
## Synthesis
- NGD Build
	- From
		- User constraints
		- Standard netlists
		- Xilinx netlist
		- Relatively placed (hard) macros
	- Generates
		- Xilinx Database netlist 
		- Build report .bld
- Map
	- What this does is associate the logic from the netlist to chip primitives like LUTs
	- From
		- Xilinx Database netlist 
	- Generates
		- Native circuit description
- Place and Route (par)
	- From ncd
	- Generates \_map.ngd
	- Most efficient algorithm was once to randomly place components and try to route until a placement configuration is possible to route
- 