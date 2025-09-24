Continues [[Explanation of Convolution]]
Continued by [[Properties of LTI]]

- ## Sum of Weighted Delays
	- ![[Pasted image 20240123101627.png]]
	- Shift $h[n]$ across $x[n]$
	- Create lines of brackets
	- Sum vertically
- ## Convolution as Product of Two Functions of $\Large k$
	- ![[Pasted image 20240123101924.png]]
	- Classic flip and shift
		- Choose 1 function to flip and shift across the other
		- Choose different values of $n$ and multiply two functions, summing the values at each $n$
- ## Comparison of Approaches 
	- ### Sum of Weighted Delays
		- Horizontal axes on plot are n
		- Final result created by adding all functions
		- Solution for $y[n]$ is computed simultaneously for all n
		- Can be parallelized in hardware
	- ### Sum of Product of Functions
		- Plots' horizontal axes are in terms of $k$
		- Sum is computed for each value of $n$ one at a time
		- Easier to program for a CPU
- ## Geometric Series Sum
	- **Particularly useful for DSP**
		- Useful for sine waves where $\alpha=e$
			- Everything is a sine wave
	- $S_{N}=\sum _{k=0}^{N}\alpha^k=1+\alpha+\alpha^{2}+\dots+\alpha^N$
	- $S_{N}-\alpha S_{N}=(1+\alpha+\dots+\alpha^N)-(\alpha+\alpha^2+\dots+\alpha^{N+1})$
	- $S_{N}(1-\alpha)=1-\alpha^{N+1}$
	- $$S_{N}=\sum_{k=0}^{N}\alpha^{k}= \frac{1-\alpha^{N+1}}{1-\alpha}; N>0$$
	- $$\sum_{k=N_{1}}^{N_{2}}\alpha^{k}=\frac{\alpha^{N_{1}}-\alpha^{N_{2}+1}}{1-\alpha}; N_{2}>N_{1}$$
- $\frac{1+2e^{-j\omega}-e^{-j_{2}\omega}}{1-0.5e^{-j\omega}}$
For class #digital-signal-processing 