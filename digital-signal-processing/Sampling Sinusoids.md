Continued by [[Sampling and The Nyquist-Shannon Theorem]]
- ## Discrete-Time Sampled Sinusoid
	- $T_{S}$ = Sampling period
	- $T_{c} =$ Continuous carrier period
	- $x[n]=x(t|_{t=nT_{S}})$
	- $x[n]=\sin\left(\frac{2\pi (nT_{S})}{T_{c}}\right)= \sin(\Omega_{c}T_{S}n)=\sin(\omega_{c}n)$
		- $\Omega_{c}$ continuous-time carrier frequency = $\frac{2\pi}{T_{c}}$ rad/s
		- $f_{c}$ Continuous-time carrier frequency = $\frac{1}{T_{c}}$ Hz
		- $\Omega_{S}$ Sampling frequency = $\frac{2\pi}{T_{S}}$ rad/s
		- $f_{S}$ = Sampling Frequency  = $\frac{1}{T_{S}}$ Hz
		- $\omega_{S}=\Omega_{c}T_{S}$ discrete-time carrier frequency, rad/sample 
	- Example![[Pasted image 20240118102610.png]]
		- $\Omega_{c} = \frac{2\pi}{T_{c}}=\frac{2\pi}{2}=\pi$ rad/sec
		- $\omega_{S} = \Omega_{c}T_{S} = \frac{\pi}{2} \frac{rad}{sample}$
	- ### Aliasing
		- ![[Pasted image 20240118103034.png]]
			- An ADC can output the same samples when given two different signals
				- Affects calculated frequency and wreak havoc on a system
			- Make sure sampling frequency is twice the highest continuous frequency, and low-pass any unneeded noise

For class #digital-signal-processing