Continued by [[PV Cell Characteristics]]
Uses [[Phasors in Active Circuit Analysis]]

- ![[Pasted image 20230112162742.png]]
	- These 3 layouts are defined from left to right
	- ### Central Inverter
		- Several PV cells in parallel, series, or both, like a battery pack, feeding into one inverter
		- Power output: 50kW-2MW
		- Can be either 3 or 1 phase
		- Generally used in very large scale operations where the variation between the multitude of panels is less frequent
			- This means power conditioners are not required
				- Cheaper not to use them, which is important at scale
	- ### String Inverter
		- Several chains of PV cells are placed in series with DC-DC power conditioners 
			- These power conditioners optimize the performance and ensure the reliability of the PV chains
			- Smooth out variations between the panels
		- Each chain is linked in parallel to one inverter
		- Power output: 1kW-50kW
		- Can be either 3 or 1 phase
	- ### Micro Inverter
		- Usually in smaller scale applications like homes
		- One PV cell into one inverter
		- Power output: 100W-350W
		- Typically 1 phase
- ## Characteristics of Power Electronics:
	- Try to use no resistive elements to minimize power loss
	- Controlling the frequency is very important
		- If the frequency of the AC power is controlled by a motor whose rotation is kept at 60Hz:
			- If this is connected to a load that does not use all the power that is generated, the energy has to go somewhere. The energy goes into spinning the motor faster and ruining the 60Hz conditioning.
			- Smart power electronics are required to ensure the stability of the system.
	- PV Inverters and their interconnection requirements are stated in IEE 1547 and UL 1741 standards.
		- No real central body that handles these topics
	- There is a tradeoff between creating an accurate sinusoidal signal and minimizing power loss by using a lower resolution DAC
	- Isolation is required in inverter systems so that DC current is not injected into the grid
		- If this happens, the transformers on the line can be damaged
	- This isolation is done through Galvanic Isolation (HF Isolation)
		- Shift the signal up to a very high frequency such that a lower inductance value is required to obtain the same impedance
			- $Z_{l}=j\omega L$
				- $\omega \land,L\lor$

For class #Junior-Design 