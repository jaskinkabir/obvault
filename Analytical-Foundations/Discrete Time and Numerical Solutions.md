Continues [[Dynamic Systems]]
Continued by [[Second Order Discretization]]
- # Discrete Vs. Continuous Time
	- A function can be defined in terms of continous time t
	- It can also be defined as a function of n, where n is some integer
	- x(t) = x(n*$\Delta t$)
		- Pick some value $\Delta t$ for each discrete integer step of n
- ## Discretizing a Differential Equation
	- Depends on this key realization:
	- $$\frac{dy}{dt}\approx \frac{y(t+\Delta t)-y(t)}{{\Delta t}}$$
		- For a small enough $\Delta t$
	- For a series RC circuit:
		- $\tau \frac{dy}{dt} + y(t) = x(t)$
		- $\tau \frac{y(t+\Delta t)-y(t)}{{\Delta t}} + y(t) = x(t)$
		- Knowing some initial condition for x(t) and y(t)
			- $\tau \frac{y(\Delta t)-y(0)}{{\Delta t}} + y(0) = x(0)$
			- $y(\Delta t)$ can be solved for algebraically
		- $$y(\Delta t) = x(0)(\frac{\Delta t}{\tau})+ (1-\frac{\Delta t}{\tau})y(0)$$
			- The two coefficients are constants
		- $y(n\Delta t) = a_{1}x((n-1)\Delta t) + a_{2}y((n-1)\Delta t)$ 
			- Where n is some integer
		- If the input function x is known, y can be approximated using a simple recursive function
			- $y((n+1)\Delta t) = a_{1}x(n\Delta t) + a_{2}y(n\Delta t)$ 
				- If we define discrete time $t = n\Delta t$
			- $y(t+1) = a_{1}x(t) + a_{2}y(t)$
- ### Discretization Example
	- $0.01\frac{dy}{dt} + y(t) = 4u(t)$ Given y(0) = 10
```MATLAB
t = [0:delta_t:7*tau];
% t = delta_t * n;

a1 = tau/delta_t
a2 = 1 - a2;

x = 4*ones(size(t))
y = zeros(size(t))

for n = 1:1:length(t)-1

	if n == 1
		y(1) = y_0;
	end

	y(n+1) = a_1*x(n)+a_2*y(n);
	
end
```
For class #Analytical-Foundations 