Continues [[CMOS Fabrication]]
Continued by [[Stick Diagrams]]
- ## Standard Cell Design Methodology
	- $V_{DD}$ and $GND$ should be abut (standard height)
	- adjacent gates should satisfy design rules
	- nMOS at bottom, pMOS on top
	- All gates include well and substrate contacts
- ## Examples
	- ### Inverter
		- ![[Pasted image 20240207105620.png]]
			- Make sure there are well and substrate taps into the bodies
				- a
	- ### NAND3
		- ![[Pasted image 20240207110329.png]]
		- ![[Pasted image 20240207110031.png]]
			- Share as many components as you can
				- The bottom nMOSFETs are in series
					- $N_{1}$'s drain is shared with $N_{2}$'s source
				- Top pMOSFETs are in parallel
					- Sources and drains are shared
					- 
		- 
For class #vlsi 
