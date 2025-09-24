Continues [[2D Linear Regression and the Loss Function]]
# Feature Scaling
- Example: House price prediction
	- Different variables have different ranges:
		- \\# of bedrooms: 0-5
		- \\# of garages 0-2
	- Certain variables will be weighted or prioritized higher than others simply because of their ranges
		- Larger range means bigger weight assigned to that variable
- ![[Pasted image 20240917133145.png]]
## Min MAX Normalization
- Scaling technique in which values are shifted and rescaled to range between 0 and 1 with the following formula $$X'=\frac{x-\text{min}(x)}{\text{max}(x)-\text{min}(x)}$$
- This means that each input to the model is now stored in 32-bit floating point numbers
	- There are pushes by Nvidia and other groups to create and use 8 or even 4 bit floating point standards
## Standardization
- Rescales features to have zero mean and unit variance
	- Let $\mu_{j} = \frac{1}{n}\sum_{i=1}^{n}x_{j}^{(i)}$ be the mean of feature $j$
	- Replace each value with $$x_{j}^{(i)} = \frac{x_{j}^{(i)}-\mu_{j}}{s_{j}}$$
		- $s_{j}$ is the standard deviation of feature $j$
		- Could also use the range of $j$
- Must apply this transformation both for training and prediction
- **Normalize and Standardize data before splitting**
# Training Vs. Validation Set
- During training, the model is trained to fit the training data points.
- During prediction however, the loss in between or away from the training data may be much higher than expected
- To solve this, reserve some data points (typically 20%) to make up the validation set and then fit the model to the remaining (80%) of data as the training set
- The model can then be evaluated on training and validation loss
## Training Rules
- If the training loss is not decreasing, the model may be too simple for the data.
	- Or, the data doesn't contain meaningful info that can explain the output
- If the training and validation losses diverge, overfit is occurring
	- The model is getting better at fitting to the training set, but it is not generalizing to samples outside the training set
# Training Regularization
- Training a model involves two critical steps
	- **Optimization:** When we need the loss to decrease on the training set
	- **Generalization:** The model has to work on data it has not seen before, like the validation set
## Parameter Penalties (Regularization)
- Add a regularization term to the loss
- **Used to combat overfit**
	- Loosens the fit of the model on the training data
- The parameters (weights) of the model tend to be small with this technique, which limits how much training makes them grow out of control
	- The value of the parameters should stay small relative to training loss
- **Essentially, this is a penalty on larger parameter values**
	- Smooths out the loss topography
- $$J(\theta) = \frac{1}{2m}\left[ \sum_{i=1}^{m}(h_{\theta}(x^{(i)})-y^{(i)})^{2} + \lambda \sum_{j=1}^{n}\theta_{j}^{2} \right]$$
	- Note that there is no regularization on $\theta_{0}$
	- $\lambda \geq 0$ is the regularization parameter
	- $n$: Dimensionality of the data
	- $m:$ Number of samples
- $$\frac{dJ}{d\theta_{j}}=\frac{1}{m}\sum_{i=1}^{m} \left(h_{\theta}(x^{(i)})-Y^{(i)}\right )x_{j}^{(i)} + \frac{\lambda}{m}\theta_{j}$$
	- Notice that the parameter penalty here is constant with respect to the iteration variable $i$
	- Thus:
$$\large \frac{dJ}{d\theta_{j}}=\lambda\theta_{j} + \frac{1}{m}\sum_{i=1}^{m} \left(h_{\theta}(x^{(i)})-Y^{(i)}\right )x_{j}^{(i)}$$
$$\theta_{j}=\theta_{j}-\alpha\left(\lambda\theta_{j} + \frac{1}{m}\sum_{i=1}^{m} \left(h_{\theta}(x^{(i)})-Y^{(i)}\right )x_{j}^{(i)}\right)$$
### Regularization Parameter Lambda
- This is a hyperparameter, like $\alpha$(learning rate).
- It defines the rate of penalization for large parameters
For class #intro-ML
