Related to [[Digital Filter Design]]

- ## What is a Butterworth Filter
	- Approximation of continuous time filter
	- Typically expressed in terms of order $N$ and cutoff frequency $\omega_{c}$ such that $$|B(j\omega)|^{2}=\frac{1}{1+\left( \frac{j\omega}{j\omega_{c}} \right)^{2N}}$$
- MATLAB can generate butterworth transfer functions:
```MATLAB
s=tf('s');

fc=2*pi*300; %300Hz

fs=10; %10 samples/sec

n=4; %fourth order

[z,p,k]=butter(n,fc,'s');

[n,d]=zp2tf(z,p,k);

Hbutter=tf(n,d)
```

For class #digital-signal-processing