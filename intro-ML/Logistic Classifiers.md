Continues [[2D Linear Regression and the Loss Function]]
Continued by [[Multi-Class Logistic Classifier]]
Continued by [[Classifier Evaluation]]
Continued by [[Naive Bayes Classifier]]
# Logistic Classifier
- Instead of predicting class, predict the probability of the instance being that class
	- Learn $p(y|x)$
	- Convert problem to a statistics, to predict probability
- **The linear regression predicts probability that a data point is of class 1**
## How To Predict Class
- Piecewise y=1 if h geq threshold
$$ y =
\begin{cases}
1 & h_{\theta}(x) \geq t \\
0 & h_{\theta} < t
\end{cases}
$$
## Sigmoid Function
- If $h_{\theta}(x)$ was a simple line, it would not generate probabilities
	- A function must be applied to the linear regression $\theta^{T}x$ to map it to a probability between 0 and 1
- The sigmoid function maps the range $(-\infty,\infty) \to (0,1)$
	- $g(z)=\frac{1}{1+e^{-z}}$
	- It is a smooth, nonlinear mapping
	- Differentiable
- $z=\overline{y}(x)=\theta^{T}x$
- $h_{\theta}(x)=g(\overline{y}(x))$
- $$h_{\theta}(x)=\frac{1}{1+e^{-\theta^{T}x}}$$
## How to Calculate Cost Function
- Apply prediction algorithm to each sample of training data
- What if the error value is a simple count of each sample classified in error
	- This doesn't take into account how far away the sample classified in error is from the decision boundary
### Logarithmic Error Function
- Use logarithmic piecewise function $$
Cost(h_{\theta}(x),y)=
\begin{cases}
- \log(h_{\theta}(x)) & y = 1 \\
-\log(1-h_{\theta}(x))) & y = 0
\end{cases}
$$
	- This function is convex and thus differentiable
	- Applying this function to each data point will generate a cost value that is convex and related to the distance between the error point and the decision boundary
- This function can be simplified as follows: $$Cost(h_{\theta}(x),y)=-y\log(h_{\theta}(x))-(1-y)\log(1-h_{\theta}(x)))$$
#### Intuition
- ![[Pasted image 20240924135725.png]]
	- If y is supposed to be 1, classifying it as 0 should result in infinite error
	- The lower the probability, or 'confidence', that the model calculates for y being 1, the greater the cost
## Gradient of Cost Function
- $g(z)=\frac{1}{1-e^{-z}}$
	- $g'(z)=g(z)(1-g(z))$
- Do some fucked up math
- $$\theta_{j} = \theta_{j} - \frac{\alpha}{m} \sum_{i=1}(h_{\theta}(x^{(i)})-y^{(i)})x_{j}^{(i)}$$
	- It's the same as the linear regression cost function
# How to Split Data into >2 Classes?
- Consider the case of 10 classes
	- Create 10 logistic regression models $h_{\theta_{1}}-h_{\theta_{10}}$
	- Each model is trained to determine if the data point is either class $n$ or not class $n$
- Train these three regressions in parallel
- Prediction requires running 10 prediction steps and picking the class that returned the highest probability value
# The Problem of Overfit
- The more variables considered by the model, the greater risk of overfit
- Logistic regression is more susceptible to overfit
For class #intro-ML