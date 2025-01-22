The task of ml is to find a function $\phi$ such that $\phi(a_{j})\approx y_{j}$ 
$\phi$ is parametrized by a set of parameters $x$
The task of training is to find $x$ such that phi works

For training we must define a loss function $l(a_{j}, y_{j, x})$
Average this loss over the training dataset to find the total loss
The optimization problem is to minimize $\frac{l}{x}$ 
 Outcomes of solving optimization are
 1. Find a subset of features that are relevant/important for the model (feature selection)
 2. There could be a low-dimensional (sparse) subspace of data that are decisive 

Examples of labels $y_j$ 
1. Real numbers (regression)
2. Elements of a finite set (classification)
3. Null (unsupervised/semi-supervised)
4. Figure out labels during problems

Another goal is to avoid overfit
Make $\phi$ not too sensitive to $D$

Regularization
Add a regularizer $\lambda x$ to the loss function to reduce the complexity of the model 

Double bar (norm) operator
$||x||_{k}= (\sum x)^{1/k}$


Examples 
1. Least Squares
     $$\frac{1}{2m}\sum_{j=1}^{m} \left(a_{j}^{T}x-y_{j}\right)^2$$
     $$=\frac{1}{2m}||Ax-y||^{2}_{2}+\lambda pen(x)$$
     Ridge regression, penalty is 2-norm x squared ($||x||_{2}^2$)
     Lasso is 1-norm x squared $||x||_{1}^2$
     Lasso creates sparse solutions
2. Matrix factorization problems 
     $$\frac{1}{2m}\sum_{j=1}^{m} \left(<A_{j},X>-y_{j}\right)^2$$
3. A
4. LR
	
All machine learning problems share
1. Real variables
2. Objective functions are continuous and mostly smooth
3. Summations of many terms
4. "Loss" + "regularization"