Continues [[Channel Capacity, Nyquist, Shannon, and EbN0]]
Related to [[The Decibel Scale]]
- ## Signal Strength Attenuation
	- As a signal propagates across a medium, there will be some loss called attenuation. It is customary to express loss in terms of decibels because
		- Signal strength often falls of exponentially
		- The net gain or loss in a cascaded transmission path can be calculated with simple addition and subtraction when using a decibel scale
- ## Decibel Loss and Gain
	- The decibel ratio of power between two signal levels is called gain, which is given by: $$G_{dB}=10\log_{10}\left( \frac{P_{out}}{P_{in}} \right)$$
	- Decibel loss is the opposite of gain:$$L_{db}=-G_{db}=10\log \left( \frac{P_{in}}{P_{out}} \right)$$
- ## Power vs. Voltage Gain
	- Since $P=\frac{V^{2}}{R}$, we can define voltage gain as follows $$G_{dB}=10\log  \frac{P_{out}}{P_{in}}=10\log \frac{V_{out}^2/R}{V^{2}_{in}/R}$$
	- Through a property of logarithms, this means that $$G_{{dB}}=20\log \frac{V_{out}}{V_{in}}$$
	- Note that these two quantities **are equivalent**
		- Voltage and Power gain are the same value
		- They are just calculated with different constant multipliers
- ## Changing The Reference Point
	- Recall that decibels are used to measure **Ratios**, or changes in magnitude not absolute units or differences
	- This means that when speaking about decibels, some reference point must be selected to equal 0dB
	- The **decibel-watt or dBW** is used very often. It selects the value of 1W to be the 0dB reference point $$P_{dBW}=10\log\left( \frac{P_{w}}{1W} \right)$$
	- Another common unit, the **Decibel-milliwatt (dBm)**, selects 1mW as the 0dB reference point. $$P_{dBm}=10\log\left( \frac{P_{mW}}{1mW} \right)$$
		- Note that $$P_{dBm}=P_{dBW}+30$$
			- Multiplying by 1000 in decibel scale is addition by 30
	- Another common unit is the **decibel-millivolt (dBmV**$$V_{dBmV}=20\log \frac{V_{mV}}{1mV}$$
		- This is assumed to be across a $75\Omega$ resistance


For class #data-comm