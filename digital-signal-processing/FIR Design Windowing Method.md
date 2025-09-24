Continues [[Digital Filter Design]]

- The purpose of windowing is to convert a discrete IIR that was designed with any method to an FIR
- ## Windowing:
	- Add a delay to $h_{d}[n]$ to create a causal function
	- Truncate to M points by multiplying by a window function w[n]
	- $h[n]=h_{d}[n]w[n]$
	- ![[Pasted image 20240409181008.png]]
- ## Windowing Functions
	- Windowing causes distortion because of the frequency convolution. This distortion can be described in terms of two quantities
	- ![[Pasted image 20240409183336.png]]
		- Peak sidelobe and main lobe width
		- A narrower main lobe will create a more accurate frequency response
	- ![[Pasted image 20240409183350.png]]
		- Rectangular window
			- Main Lobe Width: $\frac{4\pi}{M}$ peak sidelobe: -13dB
		- Triangular(Bartlett)
			- Main Lobe Width: $\frac{8\pi}{M}$ peak sidelobe: -26dB
		- Hamming
			- Main Lobe Width: $\frac{8\pi}{M}$ peak sidelobe: -43dB
		- 
For class #digital-signal-processing