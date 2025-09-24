Continues [[The Transfer Function H]]
Continued by [[Filter Scaling]]
- ## Types of Filters
	- **Highpass**: Allows high frequencies through
	- **Lowpass**: Allows low frequencies through
	- **Bandpass**: Allows frequencies through within the passband
		- Passband is centered at center frequency $\omega_{0}$
		- Also called resonant frequency
	- **Bandreject**: Stops frequencies within the stopband
	- The qualifiers "high" and "low" are relative to the cutoff of corner frequency $\omega_{c}$
- ## The Gain Factor $\Large M_{0}$
	- The maximum magnitude, usually occurring within the passband
	- An $M_{0}$ that occurs at $\omega=0$, or at DC, is called the **DC Gain**
		- If it occurs at $w\to \infty$ it is the **High Frequency Gain**
- ## The Corner Frequency $\Large \omega_{c}$
	- Defined as the angular frequency at which $M(\omega)$ is equal to $\frac{1}{\sqrt{ 2 }}$ of the reference value $M(0)$
	- $$M(\omega_{c})=0.707M_{0}$$
	- Since the topic so far has been filter circuits, the function $M(\omega)$ has been referring to a voltage-voltage transfer function
	- This means $M^2(\omega)$ is a power transfer function.
		- $$M^2(\omega_{c})=\frac{M_{0}^2}{2}=\frac{P_{0}^2}{2}$$
	- Hence, $\omega_{c}$ is also called the **half-power frequency**.
- ## The Bandwidth B
	- For lowpass, bandpass, and bandreject filters, the bandwidth B is defined as the range of frequencies within the filter's idealized passband or stopband
		- $B=\omega_{c}$ For lowpass filters (range from 0 to cutoff)
		- $B = \omega_{c_{2}}-\omega_{c_{1}}$ For bandpass and bandreject filters
- ## The Resonant Frequency $\Large \omega_{0}$
	- Resonance occurs when the input impedance of a circuit containing reactive elements is purely real, and the frequency at which this occurs is the resonant frequency
	- Often, but not always, the transfer function is also purely real at this frequency and the magnitude is at a max or min
	- If the resonant frequency happens at 0 or infinity, the resonance is considered trivial because it is an extreme of the spectrum
	- ### For an RL Circuit:
		- ![[Pasted image 20221104132643.png|200]]
		- Resonance occurs when the imaginary part of the input impedance is 0, which occurs at $\omega=0$, since $Z_{in}=j\omega L$
	- ### For an RLC Circuit
		- ![[Pasted image 20221104132754.png|200]]
			- $\large Z_{in} = R + j\left( \omega L -\frac{1}{\omega C} \right)$
			- Resonance happens when $\omega L -\frac{1}{\omega C}=0$
				- $\large \omega_{0}=\sqrt{ \frac{1}{LC} }$
- ## The Gain Roll-off Rate $\Large S_{g}$
	- At the passband boundaries, the idealized shape has infinite slopes, but the real responses have finite slopes. These slopes are called the gain roll-off rate $s_{g}$


For class #Network-Theory-II 