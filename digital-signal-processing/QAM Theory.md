## Why QAM?
### Antenna Length
Antenna Length to transmit and receive signal must be orders of magnitude larger than wavelength of signal 

For this napkin math, let's choose a factor of $3 \times 10^{8}$. For transmitting the highest frequency signal a human can hear, the size of the antenna would have to be:
$$L=\frac{C}{F}=\frac{3\times 10^{8}}{20\times 10^{3}}=15km$$
Shift frequency up to 100MHz:

$$L=\frac{3\times 10^{8}}{100\times 10^{6}}=3m$$
### INTERFERENCE
If several signals are being transmitted in the same frequency range, they will collide. Being able to select a certain frequency range for certain signals prevents this.

### Orthogonality: 
Will become clear later, but if cosines and sines are summed, they do not affect each other. They are 90 degrees apart, aka orthogonal. This means two datastreams, $m_{c}[n]$ and $m_{s}[n]$ can be sent over the same signal

$qam[n]=\cos[\omega_{c}n]m_{c}[n] + \sin[\omega_{c}n]m_{s}[n]$

### How to shift?

$$\cos(\omega)\cos(\omega_{shift})=\frac{\cos(\omega+\omega_{shift})+\cos(\omega-\omega_{shift})}{2}$$


## Demodulation:

Receiver sees the following signal:
$qam[n]=\cos[\omega_{c}n]m_{c}[n] + \sin[\omega_{c}n]m_{s}[n]$
To extract the datastream $m_{c}[n]$, first multiply by cosine carrier

$$qam[n]\cos[\omega_{c}n]=\cos[\omega_{c}n]\cos[\omega_{c}n]m_{c}[n] + \cos[\omega_{c}n]\sin[\omega_{c}n]m_{s}[n]$$

Two Trig identities can be utilized

$$\cos(x)\cos(x)=\frac{1+\cos(2x)}{2}$$
$$\sin(x)\cos(x)=\frac{\sin(2x)}{2}$$
$$qam[n]\cos[\omega_{c}n]= \left( \frac{1+\cos[2\omega_{c}n]}{2} \right)m_{c}[n] + \frac{\sin[2\omega_{c}n]}{2}m_{s}[n]$$
$qam[n]\cos[\omega_{c}n]=\frac{1}{2}m_{c}[n]+\frac{1}{2}\cos[2\omega _{c}n]m_{c}[n] + \frac{1}{2}\sin[2\omega_{c}n]m_{s}[n]$
$$qam[n]\cos[\omega_{c}n]=\frac{1}{2}(m_{c}[n]+\cos[2\omega _{c}n]m_{c}[n] + \sin[2\omega_{c}n]m_{s}[n])$$
Send this through a lowpass, and you're left with
$$\frac{1}{2}m_{c}[n]$$



For class #digital-signal-processing