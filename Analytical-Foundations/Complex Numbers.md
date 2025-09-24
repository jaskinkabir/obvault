Continued by [[Complex Phasors]]
- Can greatly reduce the number of operations in a calculation
-  Specifically in digital processing of analog sinusoidal signals 
- Represent 2 different variables as a real constant $a$ and a coefficient $b$ of imaginary number $j=\sqrt{-1}$
- Combine the variables into one complex number $r=a+jb$
- ## Cartesian form
	- Very good for addition
	- ![[Complex Number Vectors Diagram.excalidraw]]
	- Create a vector using the real and imaginary components of r
		- An angle $\theta$ can be defined as $tan^-1(\frac{imag}{real})$
		-  Either component can be extracted from R with $\theta$
			- $Imag = |r|sin(\theta)$
			- $Real = |r|cos(\theta)$
	- Converting a complex number in form $r=a+jb$ to polar form $(r,\theta)$
	- $r=\sqrt{a^2+b^2}$
	-  $\theta = \arctan{\frac{b}{a}} \pm 180^\circ$
	- Addition just involves adding the real and complex components together
		- $r_1 = a_1 +b_1j$
		-  $r_2 = a_2 +b_2j$
		- $$r_{1+2} = (a_1 + a_2) + (b_1 + b_2)j$$
- ## Euler's Identity/Polar Form
	- Good for multiplication
	- ### $e^{jx} = \cos{(x)} + jsin{(x)}$
	- $r = a+bj = |r|e^{j\theta}$
	- Multipication is simply adding the angles and multiplying the maginitudes
		- $r_1 = |r_1|e^{j\theta_1}$
		- $r_2 = |r_2|e^{j\theta_2}$
		- $$r_1r_2 = |r_1||r_2|e^{j(\theta_1 + \theta_2)}$$
		- $e^{j\theta} = \cos(\theta) + j\sin(\theta)$
		- - $e^{-j\theta} = \cos(\theta) - j\sin(\theta)$
		- $e^{j\theta} - e^{-j\theta} = 2cos(\theta)$
			- $sin(\theta) = \frac{1}{2j}(e^{j\theta} - e^{-j\theta})$
			- $\cos{\theta} = \frac{1}{2}(e^{j\theta}+e^{-j\theta})$
- ## Conjugates
	-  If r = a + jb = $|r|e^{j\phi}$ 
		- r* = a - jb = $|r|e^{-j\phi}$ 

# Examples:
![[Complex Numbers 2022-08-31 14.09.31.excalidraw]]
![[Complex Numbers 2022-08-31 13.38.57.excalidraw]]
![[Complex Number Operations Examples 2022-08-31 14.02.04.excalidraw]]

For class #Analytical-Foundations