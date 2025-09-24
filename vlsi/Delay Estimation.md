Continues [[Clock Skew and Path Constraints]]
- ## Transient Response
	- a
- ## Inverter Step Response
	- $V_{in}(t)=u(t-t_{0})V_{DD}$
	- $V_{out}(t<t_{0})=V_{DD}$
	- $\frac{dV_{out}(t)}{dt}=- \frac{I_{dsn}(t)}{C_{load}}$
	- $I_{dsn}=\begin{cases} 0 & t \leq t_{0}\\ \frac{\beta}{2}(V_{DD}-V_{t})^{2} & V_{out} > V_{DD}-V_{t} \\ \beta\left( V_{DD}-V_{t}-\frac{V_{out(t)}}{2} \right)V_{out(t)} & V_{out} < V_{DD}-V_{t} \end{cases}$
- ## Delay Definitions
	- These are mostly arbitrary, this class defines them as follows
		- $t_{pdr}$: rising propagation delay
			- From input to rising output crossing $\frac{V_{DD}}{2}$
		- $t_{pdf}$
			- From input to falling output crossing $\frac{V_{DD}}{2}$
			- Worst case
		- $t_{pd}$: average of last two
		- $t_{r}$: Rise Time
			- From output crossing 0.2$V_{DD}$ to $0.8V_{DD}$
		- $t_{f}$: Fall time
			- From output crossing 0.8$V_{DD}$ to $0.2V_{DD}$
		- $t_{cdr}$: Rising Contamination Delay
			- From input to rising output crossing $\frac{V_{DD}}{2}$
		- $t_{cdf}$: Falling Contamination Delay
			- From input to falling output crossing $\frac{V_{DD}}{2}$
		- $t_{cd}$: average
	- ### Contamination
		- 
- ## RC Delay Model
	- Use equivalent circuits for MOS transistors
		- Ideal switch + capacitance and ON resistance
		- Unit nMOS has resistance R, capaciatance C
		- Unit pMOS has resistance 2R, capacitance C
		- Unit width is $4\lambda$ Unit height is $2\lambda$
	- Capacitance proprtional to width
	- Resistance inversely proportional to width
	- ![[Pasted image 20240318105153.png]]
		- Three capacitors per pin
	- ### RC Values
	- #### Capacitance
		- $C=\frac{2fF}{\mu m}$ of gate width in 0.6 $\mu m$
			- Gradually decline to $\frac{1fF}{\mu m}$ in 65nm
	- #### Resistance
		- $R \approx 10K\Omega * \mu m$ for 0.6 $\mu m$
			- 1.25K for 65nm
	- #### Unit Transistor
		- Either minimum contacted device $(4/2)\lambda$
			- 4 wide 2 long
		- 
		- Or 1 $\mu m$ wide
	- ### Estimating Inverter Delay
		- ![[Pasted image 20240320103600.png]]
		- Falling: ![[Pasted image 20240320103549.png]]
	- ### NAND3 GATE
		- ![[Pasted image 20240320104036.png]]
			- The pMOS side has a combined Resistance of $\frac{R}{3}$, when all three inputs are high
			- Meaning the worst case scenario, just one input is high, has a resistance of $R$
			- The pMOS resistance is set to R, nMOS set to $\frac{R}{3}$ such that both worst case resistances are $R$
			- ![[Pasted image 20240320104905.png]]
				- The 2 or 3 without a C is the width of the channel
			- Combine gate capacitances and source/drains separately
				- ![[Pasted image 20240320105035.png]]
			- Use Elmore Delay estimation of a RC ladder
- ## Elmore Delay Analysis
	- # FULLY UNDERSTAND THIS FOR THE FINAL
	- ON Transistors look like resistors
	- Pull-up pull-down network modeled as RC ladder
	- $$t_{pd} \approx \sum_{i}^{Nodes}R_{i\to source}C_{i}$$
	- ![[Pasted image 20240320105311.png]]
	- ![[Pasted image 20240320105841.png]]
		- You must find the worst possible scenario; the scenario with the highest delay
- ## Contamination Delay
	- Best case scenario
- ## Diffusion Capacitance
	- Good layour inimizes diffusion area
	- $V_{DD}$ does not contribute to capacitance
		- Minimize switching contacts
- ## 3-Input NOR Example



$$R_{n}=\frac{R}{W}$$
$$R_{p}=\frac{2R}{W}$$


For class #vlsi 