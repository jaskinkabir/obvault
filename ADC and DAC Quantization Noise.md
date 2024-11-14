Related to [[Sampling and The Nyquist-Shannon Theorem]]
- The effect of random quantization noise error $q(t)$ is a noise added to the analog signal before being digitized
	- $q(t)$ has a uniform pdf from $-\frac{\Delta v}{2}$ to $\frac{\Delta v}{2}$ where $\Delta v$ is the size of voltage steps of the ADC/DAC
		- $p_{q}(q)=\frac{1}{\Delta v} \Pi\left( \frac{q}{\frac{\Delta v}{2}} \right)$
	- $\mu_{q}=0, \sigma_{q}=\frac{\Delta v}{\sqrt{ 12 }}$
		- $\mu =$ Mean noise
		- $\sigma_{q}=$ RMS Noise Voltage
			- Remember that 
				- RMS = $\sqrt{\frac{1}{T_{2}-T_{1}} \int _{T_{1}}^{T_{2}} f(t)^2 \, dt }$
				- Standard deviation formula in this case is the RMS of noise
	- Max full-bandwidth signal-to-noise in ADC $\approx 1.8 + 6.02N dB$ where $N$ is number of bits
	- ![[Pasted image 20240125105459.png]]

For class #digital-signal-processing 