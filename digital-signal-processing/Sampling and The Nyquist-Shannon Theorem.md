Continues [[Sampling Sinusoids]]
Continued by [[Difference Equations]]
Related to [[ADC and DAC Quantization Noise]]
- ## ADC Sampling Example
	- ### The Smiley Face Approach
	- ![[Pasted image 20240125102302.png]]
		- Assume the FT of the input signal is some arbitrary shape
			- Could be a smiley face for all we care
			- $X(\Omega)=\ :)$
		- To sample the signal, convolve the signal with an impulse train
			- Distance between each impulse is $T_{s}$
		- This becomes multiplication in the frequency domain
		- Multiplication between some shape and an impulse train just repeats that shape centered on each impulse
			- Smiley faces separated by $T_{s}$ describes the FT of the sampled $X_{s}(\Omega)$
		- The $T_{s}$ wide square wave smooths out the impulse train into a continuous sampled signal
			- Describes/models the stepwise behavior of a real ADC
		- The convolution of the sampled $x_{s}(t)$ and the square is the multiplication of the FT of the sampled $x_{s}(t)$ and the parametrized sinc
			- $T_{s}sinc\left( \frac{\Omega T_{s}}{2} \right)$
	- $x[n]=x(nT_{s})$
	- $\Pi\left( \frac{t}{T_{s}}\right) \iff T_{s}sinc\left( \frac{\Omega T_{s}}{2} \right)$
- ## Nyquist Rate and Aliasing
	- If the sampling frequency $\Omega_{s}$ is too small, the spectra will overlap and information will be lost
		- Spectra means smiley face
	- This overlap is called aliasing
	- The minimum sampling rate to prevent aliasing is the Nyquist rate 2B, where B is the bandwidth in Hz of the signal $x(t)$
	- The signal reconstructed by a DAC must also be passed through a B low-pass filter to maintain the bandlimit
		- Vertical parts of stair signal are smoothed
	- ![[Pasted image 20240125103905.png]]
- ![[Pasted image 20240125104145.png]]
- ![[Pasted image 20240125104540.png]]
- ## Nyquist Shannon Sampling Theorem
	- https://www.youtube.com/watch?v=pWjdWCePgvA
	- If a signal is strictly bandlimited to B Hz, then it can be perfectly reconstructed from its samples, if the signal is sampled at a sampling rate greater than @B Hz
		- For example, humans can only hear sound waves less than $20KHz$ in frequency, so a lowpass filter is applied to any waveform to limit B to 20KHz
		- By bandlimiting the signal, we have ensured that the highest frequency Fourier component of the signal must be at most 20KHz, and so sampling at 2 samples per cycle results in 0 data loss
	- All time points between sample points can be exactly recovered
- 
For class #digital-signal-processing 