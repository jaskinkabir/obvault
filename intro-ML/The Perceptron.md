Continues [[Types of Machine Learning]]
Continued by [[Feature Mapping and Kernelization]]
# The Perceptron Model
- Takes a series of inputs and has one binary output
- Consists of three parts
	- A series of inputs
	- A weighted sum of these input plus a bias
		- $w_{0},\,w_{1}\dots ,w_{n}$
	- A nonlinear activation function
		- If this activation function results in a positive value, the answer is yes
		- Otherwise no
- A logistic classifier is a perceptron
	- But the perceptron only has a binary output, whereas a logistic classifier predicts continuous probabilities
	- 
# Perceptron Learning
- Set $t=1$, $w_{1}=\text{zeros}(n)$
- Given point $x$, predict positive iff $w_{t} * x \geq 0$
- On a mistake, update as follows
	- False negative: $w_{t+1}=w_{t}+x$
	- False positive: $w_{t+1} = w_{t}-x$
![[Pasted image 20241022133135.png]]
- $w_{1}=(0,\,0)$
	- $P(-1,\,2)=0$ WRONG
- $w_{2}=w_{1}-(-1,\, 2)=(1,\,-2)$
	- $P(1,\,1)=-1$ WRONG
- $w_{3}=w_{2}+(1,\,1)=(2,\,-1)$
	- $P(-1,\,-2)=0$ WRONG
- $w_{4}=w_{3}-(-1,\,-2)=(3,\,1)$
	- Correctly classifies all points


For class #intro-ML
