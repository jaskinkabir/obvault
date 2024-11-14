Continues [[Phasors in Active Circuit Analysis]]
Continued by [[Complex Power]]
- ## Instantaneous Power
	- If the instantaneous current flowing through a resistor is $i(t)$, then the instantaneous power $p(t) = i^{2}(t)R$ 
- ### Average Value
	- The current through a resistor is always in phase with the voltage across it
	- The average value of a periodic waveform is as follows
		- $\frac{1}{T}\int_{0}^{1}x(t)dt$
- ### Root Mean Square
	- #### Effective value
		- The current that a circuit would receive if it were a dc current
		- Defined such that average power delivered by i(t) to a resistor is equivalent to what a dc current of Ieff would deliver
	- The root mean square is then 
		- $$X_{eff} = X_{rms} = \sqrt{\frac{1}{T}\int_{0}^{1}x^{2}(t)dt}$$
		- For any sine or cosine wave, $V_{rms}= \frac{V_{m}}{\sqrt{2}}$
  - ### Average Power 
	- $p(t) = i(t)v(t)$
		- $p(t) = I_{m}cos(\omega t + \theta_{i}) +  V_{m}cos(2\omega t + \theta_{})$
	- $$p(t) = \frac{V_{M}I_{M}}{2}cos(\theta_{v}-\theta_{i}) + \frac{V_{M}I_{M}}{2}cos(\omega t +\theta{v} + \theta{i})$$
		- First term is constant
		- This is the new centerline for the sinusoid
		- The average power
	- **Average power** = $\frac{V_{M}I_{M}}{2}cos(\theta_{v}-\theta_{i})$
	- **Power Factor angle** Is $\theta_{v}- \theta_{i}$
		- For a purely resistive load, voltage and current are in phase, so the power factor angle is 0
			- $P_{av}= V_{rms}I_{rms} = \frac{V^{2}_{rms}}{R}$
		- For a purely reactive load (Capacitors/Inductors with no resistors), the power factor is always $\pm 90\degree$
			- $P_{av}= V_{rms}I_{rms}cos(90) = 0$
			- Reactive load can store and release power, but the net power is 0
For class #Network-Theory-II 