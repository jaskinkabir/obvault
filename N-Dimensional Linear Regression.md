continues [[2D Linear Regression and the Loss Function]]

# Increasing Dimensionality
- Adding hidden dimensionality to a non-linear function can expose linearity in those higher dimensions
	- Adding more variables
- Example: Quantum mechanics
	- From human 4D perception, quantum particle behavior appears non-linear
	- String theory attempts to explain this behavior in 11 dimensions, and can reconcile these nonlinearities
# New Y Prime
- $$\overline{y}=w_{n}x_{n} + w_{n-1}x_{n-1} + w_{n-2}x_{n-2} + \dots + w_{1}x_{1}+b$$
	- Note that this is a linear combination
	- You can create an $m \times n$ matrix where the columns are the data vectors $x_{0}\dots x_{n}$ 
	- Then create an $n \times 1$ matrix which is a vector of all $w$ values
	- You can then multiply these arrays to create an $m \times 1$ matrix that contains $\overline{y}$ vertically
- $$\frac{dL}{dw_{n}}=\frac{1}{m}\sum(\overline{y}-Y)x_{n}$$
- Notice that this is a linear combination