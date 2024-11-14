Continues [[DSP Discrete-Time Fourier Transform]]
Continued by [[Comparison of DTFT and DFT]]
Continued by [[Circular Convolution]]
Continued by [[Matrix Form of DFT]]

- ## The Discrete Fourier Transform
	- Discrete in time AND Frequency
	- Assuming $x[n]$ and DFT $X[k]$ are $N$ elements in length:
	- $$X[k]=\sum_{n=0}^{N-1} x[n]e^{-j \frac{2\pi}{N}kn}$$
		- $X[k]$ is simply $X(\omega)$ sampled with $Fs=\frac{2\pi}{N}$ rad/sample 
			- $X[k]=X(\omega)|_{\omega=\frac{2\pi}{N}k}$
			- Takes $N$ samples of $X(\omega)$
		- This means that $X[k]$ is periodic where $T=N$
			- $X[k]=X[k+N]$
	- ### Comments
		- a
- ## Fast Fourier Transform
	- Result is **exactly the same** as DFT
		- Just a faster algorithm
	- DFT requires $N^2$ complex multiplications
		- Sums all values of function across all $n$ $N$ times
			- Total number of $n$ measured is $N$ so $N^2$
	- FFT requires $N\log_{2}(N)$ complex multiplications
	- Typically, FFT is done with $N$ as a power of 2
	- DTFT Formula: $$X[k]=\sum_{n=0}^{N-1}x[n]e^{-j \frac{2\pi}{N}nk}$$
		- The complex multiplication has 4 cases where the operation is trivial
			- $\frac{2\pi}{N}nk=1,-1,j,-j$
			- Recognize these cases and speed up algorithm that way
			- The true speed gain is much more complex
- ## Inverse DFT
	- Sampling in time creates periodic frequency domain
	- Sampling in frequency creates periodic time
	- IDFT causes $x[n]$ to have period $N$
	- $$x[n]=\frac{1}{N}\sum_{k=0}^{N-1}X[k]e^{j \frac{{2}\pi}{N}k}$$
	- 
- ## Periodic Extension
	- ![[Pasted image 20240208105044.png]]
	- #### Circular Shift
		- ![[Pasted image 20240208105100.png]]
		- ![[Pasted image 20240208105112.png]]
	- ### Modulo Arithmetic
		- n mod N denoted $((n))_{N}=\alpha$ such that
			- $\alpha+Kn=n$ and $0\leq \alpha \leq N$, $k$ is some int
		- Example
			- ![[Pasted image 20240208105447.png]]
			- $x[n]=\{1,2,3,4\}$
			- $x[n-1]=x[((n-1))_{4}]=\{x[0]\}$
For class #digital-signal-processing 