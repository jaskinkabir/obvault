Continues [[Clock Skew and Path Constraints]]

- # Phase Locked Loop (PLL)
	- Takes external clock signal and generates global chip clock synced with ext clk
	- ![[Pasted image 20240408103226.png]]
	- ![[Pasted image 20240408103339.png]]
	- ![[Pasted image 20240408103352.png]]
	- ![[Pasted image 20240408103402.png]]
	- ![[Pasted image 20240408103535.png]]
	- ![[Pasted image 20240408103542.png]]
- # Delay Locked Loop (DLL)
	- Uses voltage-controlled delay line rather than oscillator
	- Adjusts phase only, frequency multiplication is impossible
	- Simpler than PLL
- # Clock Distribution Network Design
	- Goal is to minimize variance between clocked elements
		- Variance given by
		- ![[Pasted image 20240408105359.png]]
	- ![[Pasted image 20240408103729.png]]
		- Grid
			- Low skew, high power
			- ![[Pasted image 20240408105446.png]]
				- Can put the drivers on the perimeter or add H's onto the grid
				- If the drivers are on the perimeter, there will be more delay at the center where there is the most distance from the driver
		- H-tree
			- All clock points the skew must be equal
			- Add zigzag or buffer to equalize delays
		- X-Tree
			- Theoretical
		- Tapered H-Tree
			- Starts with thick wire and thin as they get to clocked components
			- Use thick wire for more current
			- There are constraints with wire where if a certain $J=\frac{I}{A}$ is violated, the wire melts
	- ![[Pasted image 20240408110127.png]]

For class #vlsi 