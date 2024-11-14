Continues [[Types of Machine Learning]]
Continued by [[N-Dimensional Linear Regression]]
Continued by [[Improving Learning]]
# The Loss Function
- The goal of a linear regression model is to, out of all possible lines, find the line that best fits (predicts) the training data
- The line is evaluated by applying the **Loss function**
	- Also called loss or cost function
	- Classic technique is to find average error between the line and all data points
- $$L=\frac{1}{m}\sum_{i=1}^m|Y_{i}-\overline{y}_{i}|$$
	- $L$ is the loss
	- $m$ is the number of training data points
	- $Y$ is the ground truth, or training data
	- $\overline{y}$ is the prediction (y prime)
- The problem is that this function may not be convex, may not have a minimum
	- The loss scales up and down linearly
	- This is why we must take the square of the error
- $$L=\frac{1}{2m}\sum_{i=1}^m(Y_{i}-\overline{y}_{i})^{2}$$
	- multiply by 1/2 for mathematical convenience
	- This function has a curve at its minimum. There are many points very close to 0 loss when compared to the linear function because it is quadratic
		- ![[Pasted image 20240829133250.png]]
	- This function is also differentiable, which means the minimum can be found where the derivative is 0
		- For the linear loss function, the slope of the line is constant across either side of the y-axis; the only information is whether the slope is negative or positive
		- But for the curved loss function, the derivative also includes information about how far the regression model is from a perfect 0 loss
## Differentiating the Loss Function
- Consider a case where the model must predict a simple two variable line in the form $\overline{y}=wx+b$
- In this case, the loss function contains the function $\overline{y}$, which depends on two independent variables $w$ and $b$
- This means taking the derivative of the loss function requires taking two derivatives with respect to $w$ and $b$ independently
	- This is called taking the gradient
## Applying The Loss Function
- Find the derivative of the loss function at some value of $w$
- Invert the derivative's sign and multiply the magnitude by some value $\alpha$
	- Defined as learning rate, which determines the impact of the magnitude of the loss function on the parameters
	- A lower learning rate would decrease the 'ping pong' fluctuation from one side of the curve to the other
	- A lower learning rate takes longer to reach the optimal model, but will reach a better model than a higher rate
- Add this value to $w$ and repeat until the loss is minimized
- $$w_{t+1}=w_{t}-\alpha\frac{dL}{dw}$$
	- At the same time run this calculation independently $b_{t+1}=b_{t}-\alpha\frac{dL}{db}$
## What is done during each iteration
- Calculate $\overline{y}=wx+b$
- Calculate $L=\frac{1}{2m}\sum_{i=1}^m(Y_{i}-\overline{y}_{i})^{2}$
- Take derivative $\frac{dL}{dw}$ and $\frac{dL}{db}$
- Calculate $w_{t+1}=w_{t}-\alpha\frac{dL}{dw}$ and $b_{t+1}=b_{t}-\alpha\frac{dL}{db}$
- Repeat
# How to Differentiate Loss Function
- $L=\frac{1}{2m}\sum_{i=1}^m(Y_{i}-\overline{y}_{i})^{2}$
- $L=\frac{1}{2m}\sum_{i=1}^m(Y_{i}+(wx_{i}-b))^{2}$
- $L=\frac{1}{2m}\sum_{i=1}^m(Y^{2}+(wx_{i}+b)^{2} - 2Y(wx_{i}+b))$
- $L=\frac{1}{2m}\sum_{i=1}^m(Y^{2}+(w^{2}x_{i}^2+b^{2}+2wbx_{i}) - 2Y(wx_{i}-b))$
- $L=\frac{1}{2m}\sum_{i=1}^m(Y^{2}+w^{2}x_{i}^2+b^{2}+2wbx_{i} - 2Ywx_{i}-2Yb)$
- $\frac{dL}{dw}=\frac{1}{m}\sum_{i=1}^m(2wx_{i}^2+2bx_{i} - 2Yx_{i})$
- $$\frac{dL}{dw}=\frac{1}{m}\sum_{i=1}^{m} (\overline{y}-Y)x_{i}$$
- $L=\frac{1}{2m}\sum_{i=1}^m(Y^{2}+w^{2}x_{i}^2+b^{2}+2wbx_{i} - 2Ywx_{i}-2Yb)$
- $\frac{dL}{db}=\frac{1}{2m}\sum_{i=1}^m(2b+2wx_{i}-2Y)$
- $$\frac{dL}{db}=\frac{1}{m}\sum_{i=1}^m(\overline{y}-Y)$$
## New Procedure
Calculate $\overline{y}=wx+b$
- Calculate $L=\frac{1}{2m}\sum_{i=1}^m(Y_{i}-\overline{y}_{i})^{2}$
- Take derivative $\frac{dL}{dw}=\frac{1}{m}\sum_{i=1}^{m} (\overline{y}-Y)x_{i}$ and $\frac{dL}{db}=\frac{1}{m}\sum_{i=1}^m(\overline{y}-Y)$
- Calculate $w_{t+1}=w_{t}-\alpha\frac{dL}{dw}$ and $b_{t+1}=b_{t}-\alpha\frac{dL}{db}$
- Repeat

For class #intro-ML