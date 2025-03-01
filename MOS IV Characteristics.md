Continues [[CMOS Logic Design]]
Expands [[MOSFET Transistors]]
Continued by 
- ## Ideal transistor
	- So far, transistors have been treated as ideal switches
	- ON transistor passes a finite current
		- Dependent on terminal voltages
	- Transistor gate, source, and drain in real life all have capacitance
		- $I=C\left( \frac{\Delta V}{\Delta t} \right)$
		- $\Delta t=\frac{C}{I}\Delta V$
	- Capacitance and current determine speed
	- MOS Gate and body form a capacitor
	- ![[Pasted image 20240214105720.png]]
		- Accumulation
		- Depletion
			- Channel is empty
		- Inversion
			- Channel attracts electrons
- ## nMOS Regions
	- ### nMOS Cutoff
		- No channel
		- $I_{ds}\approx_{0}$
		- $V_{gs}<V_{t}$
		- ![[Pasted image 20240226102944.png]]
		- The depletion region is growing, but has not yet turned into a conduction channel
	- ### nMOS Linear
		- Channel is forming
			- Current flows from d to s
			- $I_{ds}$ increases linearly with $V_{ds}$
				- Like a linear resistor
		- $0<V_{ds}<V_{gs}-V_{t}$
		- ![[Pasted image 20240214110054.png]]
		- $V_{gs}$ has surpassed the threshold, and the depletion region has become a conduction channel
			- The gate voltage attracts negative charge carriers to the gate terminal and forms a channel
		- $V_{DS}$ is creating a depletion region at the drain terminal by pushing away positive charge carriers, but this voltage is not large enough to affect the conduction channel yet
		- Current in this region is dependent on gate voltage and Drain-Source voltage. Gate source voltage affects strength of conductance band, ie resistance and Drain-source voltage is like the V in V=IR
			- Due to fucked up physics, the current is not exactly Ohmic
			- V=IR is an analogy; the transistor is not truly acting like a resistor where its resistance is proportional to the gate-source voltage, but this is a useful approximation
	- ### nMOS Saturation
		- ![[Pasted image 20240226103004.png]]
		- $I_{ds}$ is now independent of $V_{ds}$ and current saturates; the transistor behaves like a current source
			- This is because $V_{DS}$ creates a larger depletion region at the drain, as the positive voltage pushes the positive carriers in the p body further away from D, than the force pushes them away at S
			- At the critical point where $V_{DS}=V_{gs}-V_{t}$, the depletion region at the drain becomes so large that the conduction channel is no longer the mechanism by which current flows from D to S
		- Channel pinches off
			- The potential between gate and body is so high, electrons in the depletion region move to their conductance band and generate current
			- The electrons jump from the pinch-off point to the drain because of the strong field at the drain.
			- Lattice restructuring of the silicon
			- If VDS rises too high, this restructuring becomes permanent
		- $V_{gs}>V_{gs}-V_{t}>0$
			- Pinch off voltage: $V_{ds}=V_{gs}-V_{t}$
				- Depends on $V_{gs}$
	- 
	- ### Cutoff: $V_{gs}<V_{t}$
	- ### Linear: $V_{ds}<V_{gs}-V_{t}$
	- ### Pinch-Off: $V_{ds} = V_{gs}-V_{t}$
	- ### Saturation: $V_{ds}>V_{gs}-V_{t}$
- ## Channel Charge
	- MOS Structure looks like parallel plate capacitor
		- ![[Pasted image 20240226103247.png]]
	- $Q_{channel}=CV$
	- $C=C_{g}=\large\frac{\epsilon_{ox}WL}{t_{ox}}=C_{ox}WL$
		- We can simplify $\frac{\epsilon_{ox}}{t_{ox}}=C_{ox}$
	- L is dependent on $V_{DS}$
	- Width is fixed for the technology
	- $V_{GC}=V_{gc}-V_{t}=\left( V_{gs}-\frac{V_{ds}}{2} \right)-V_{t}$
		- $V_{gc}$ approximates the voltage from the gate to the midpoint of the channel to understand the capacitor voltage
- ## Carrier Velocity
	- Electrons are propelled by lateral electric field between source and drain
		- $E=\frac{V_{ds}}{L}$
			- Average voltage across channel, because lateral field is orthogonal to source-drain field
	- Carrier velocity $v$ proportional to lateral E-Field
		- $v=\mu E,\  \mu$ called mobility
	- Time for carrier to cross channel 
		- $t=\frac{L}{v}$
- ## Derivation of Linear $\Large I_{DS}$ Formula
	- $I_{DS}=\frac{Q}{t}$
		- Charge of capacitor divided by time it takes for charge to travel across channel, current
	- #### Derivation of $t$
		- $t = \frac{L}{v}=\frac{L}{\mu E}=\frac{L}{\mu  \frac{V_{ds}}{L}}=\frac{L^{2}}{\mu V_{ds}}$
			- Length of channel divided by carrier velocity
		- $I_{DS}=\frac{Q*\mu V_{ds}}{L^{2}}$
			- This resembles an Inverse-Square Law, where the current decreases with the square of the channel length.
			- Current is proportional to voltage, like Ohm's law; and to mobility
	- #### Derivation of Q
		- $Q=CV$
			- $C=C_{ox}WL$
			- $V=V_{gs}-\frac{V_{ds}}{2}-V_{t}$
		- $Q=C_{ox}WL\left( V_{gs}-\frac{V_{ds}}{2}-V_{t} \right)$
			- Capacitance times approximate (midpoint) gate to channel voltage
	- ### Full Equation
		- $I_{DS}=\frac{\mu C_{ox}WL\left( V_{gs}-\frac{V_{ds}}{2}-V_{t} \right)V_{ds}}{L^2}$
		- $$I_{DS}=\mu C_{ox} \frac{W}{L}\left( V_{gs}-V_{t}-\frac{V_{ds}}{2} \right)V_{ds}$$
- ## nMOS Linear I-V
	- $I_{ds}=\frac{Q_{channel}}{t}$
	- $\large \mu C_{ox} \frac{W}{L} \left( V_{gs}-V_{t}-\frac{V_{ds}}{2} \right)V_{ds}$
	- We can say $\mu C_{ox} \frac{W}{L}$ is constant and equal to $\beta$
		- $\beta=\mu C_{ox} \frac{W}{L}$
	- $\beta\left( V_{gs}-v_{t}-\frac{v_{ds}}{2} \right)V_{ds}$
	- Linear operation happens for small $V_{ds}$
	- In the linear region, $\frac{v_{ds}}{2} \ll V_{gs}-V_{t}$, so it can be ignored to create a first order approximation
- ## nMOS Saturation I-V
	- If $V_{gd}<v_t$
	- $V_{ds}=V_{gs}-V_{t}$ at the pinchoff point
	- Drain voltage no longer increases current
		- $I_{ds}=\beta\left( V_{gs}-V_{t}-\frac{V_{dsat}}{2} \right)V_{dsat}, \  \,V_{dsat}=V_{gs}-V_{t}$
			- $I_{dsat}=\beta\left( V_{gs}-V_{t}- \frac{V_{gs}-V_{t}}{2} \right)(V_{gs}-V_{t)}$
			- $I_{dsat}=\beta\left( \frac{V_{gs}-V_{t}}{2} \right)V_{gs}-V_{t}$
		- $$I_{dsat}=\frac{\beta}{2}(V_{gs}-V_{t})^2$$
	- This assumes that $V_{DS}$ no longer affects $I_{DS}$ after pinchoff
		- This is because $V_{DS}$ no longer affects the amount of charge carriers available in the channel, although it can decrease the length of the channel and very slightly increase the current
			- This is considered negligible, because the mechanism for conduction is electrons jumping across the depletion region
			- The length of the conduction channel only affects the speed of charge transfer once the charge carriers jump across the depletion region
			- Their ability to jump depends **entirely** on $V_{gs}$
	- 
- ## Shockley First Order Transistor Models
	- ![[Pasted image 20240226105618.png]]
- ## pMOS I-V
	- ### Characteristics
		- All dopings and voltages are inverted
		- Mobility $\mu_{p}$ is determined by holes
			- Mobility 2-3x lower than electrons
		- pMOS must be wider to provide samecurrent
			- Assume $\mu_{n}=2\mu_{p}$
	- ### Capacitance
		- Gate to channel capacitor is very important
		- Source and drain have capacitance to body
			- Diffusion capacitance
		- #### Gate Capacitance
			- $C_{gs}=\epsilon_{ox}\frac{WL}{t_{ox}}=C_{ox}WL=C_{permicron}W$
		- #### Diffusion Capacitance
			- Called parasitic
			- ![[Pasted image 20240311103814.png]]
	- ![[Pasted image 20240311104230.png]]
		- Same conditions as nMOS, but reversed
For class #Electronics-Semiconductors