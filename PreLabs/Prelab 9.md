The prelab was done with the following matlab script to sum harmonic cosine waves
```MATLAB
f1=10;

w1=2*pi*f1;

t=[0:(1/(20*f1)):2];

a = [1 2 3 5 4 -5 -1 -3 -4 -2 ];

b=zeros(1,10);

%a=ones(1,10);

w=[1:10]*w1;

cosines = {};

sines={};

signal = zeros(size(t));

for i=1:10

cosines{i}=a(i)*cos(w(i).*t);

sines{i}=b(i)*sin(w(i).*t);

signal = signal + cosines{i}+sines{i};

%figure()

%plot(t,signal)

end

plot(t,signal)
```
# Question 1: How would you expect the summation of to look if you could add up many more harmonics?
Infinitely summing harmonics with the same amplitude of 1 can be represented by this equation
$x(t)=\sum_{n=1}^{\infty}\cos(n\omega t)$
What this would eventually become is a pulse train with a frequency equal to the fundamental frequency with a DC value of -1
$x(t)=\sum_{n=-\infty}^{\infty}\delta\left( t-\frac{n}{f_{1}} \right)$-1
# Question 2: What is its peak amplitude and is this as expected?
The peak amplitude is 10. This is expected as 10 harmonic signals were summed, each with an amplitude of 1.
# Question 3: Is the fundamental an odd or even function? Is the summation odd or even?
The fundamental and the summation are both even, as it is the sum of a cosine.
# Question 4: Write the equation for the summation of the 10 signals? Is it symmetrical about the X axis?
$$x(t)=\sum_{n=1}^{10}\cos(n\omega t)$$
This is theoretically symmetric about the X axis

# Question 5: Vary the amplitudes and notice how the signal changes. You may set the amplitude of certain components to 0 as you see fit. Can you create a wave form which starts at a zero value? Write the equation for your new varied amplitude signal? Does it start at a zero value?

By creating a set of amplitudes with a sum of 0, the value of $x(0)$ will be 0. The amplitudes used for this function are as follows: `a = [1 2 3 5 4 -5 -1 -3 -4 -2 ];`
This equation would then be $x(t)=\cos(\omega_{1} t)+2\cos(2\omega_{1}t)+3\cos(3\omega_{1}t)+5\cos(4\omega_{1}t)$$+4\cos(5\omega_{1}t)-\cos(6\omega_{1}t)-3\cos(7\omega_{1}t)-4\cos(8\omega_{1}t)-2\cos(9\omega_{1}t)-2\cos(10\omega_{1}t)$
This does start at a zero value as can be seen in the graph below
![[Pasted image 20240409133748.png]]
Since the fundamental period is 0.1s, the function is 0 at each multiple of 0.1 seconds.

# Question 6: How would you expect the sine summation of to look if you could add up many more harmonics?
Since the sine function starts at zero, and adding more harmonics only works to cancel out all the variations from this initial value, the sum of all sine waves should simply be a flat line at y=0
$x(t)=0$
# Question 7: What is its peak amplitude and is this as expected? Is this an odd or even function?
$a$
![[Pasted image 20240409135852.png]]
As the sine wave is an odd function, this sum is also an odd function. The peak amplitude seems to equal $\tan(0.45\pi)$ which wasn't expected.

# Question 8: Vary the amplitudes and notice how the signal changes. You may set the amplitude of certain components to 0 as you see fit. Can you create a wave form which starts at a non-zero value? Write the equation for your new varied-amplitude signal? Does it start at a non-zero value? Is it symmetrical about X axis?
Using the same amplitudes as in question 5, the following summation was generated
$x(t)=\sin(\omega_{1} t)+2\sin(2\omega_{1}t)+3\sin(3\omega_{1}t)+5\sin(4\omega_{1}t)$$+4\sin(5\omega_{1}t)-\sin(6\omega_{1}t)-3\sin(7\omega_{1}t)-4\sin(8\omega_{1}t)-2\sin(9\omega_{1}t)-2\sin(10\omega_{1}t)$
This function starts at zero, and no set of amplitudes can allow a summation of harmonic sine waves to start at a non-zero value, as sin(0)=0. This waveform should theoretically not be symmetric about the X axis

# Question 9: Write the equation for the summation of these 2 waves? Write the equation for the summation in terms of the sine wave with a nonzero phase shift.

$x(t)=a_{1}\sin\left( \omega_{1}t+\frac{\pi}{2} \right)+b_{1}\sin(\omega_{1}t)$

# Question 10: Describe how the summation changes as you vary the respective amplitudes?
The shape of the waveform is mostly unaffected by the varying amplitudes, however the size of the peaks does change. The amplitude of the cosine determines the 0 value.

# . Question 11: For a particular pair of amplitudes you have set, write the equation for the summation in terms of sine and cosine as well as its equivalent polar representation?

$x(t)=a\cos(\omega_{1}t+b\sin(\omega_{1}t))$
$Ce^{j\omega t}=a\cos(\omega_{1}t)+jb\sin(\omega_{1}t)$
Phasor representation:
![[Pasted image 20240409142410.png]]

$A\cos(\omega t)A\cos(\omega t)=A^2\cos^{2}(\omega t)=\frac{A^{2}}{2}(1+\cos(2\omega t))$
