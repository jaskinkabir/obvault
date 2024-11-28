Continues [[Artificial Neural Networks (ANN)]]

# Preprocessing
- A color image is an $M \times N$ pixel image, where each pixel contains 3 RGB values
- A color image must be inputted into a neural network as a single tensor of $1 \times (M*N*3)$
	- Constructing this 1 dimensional matrix is called unrolling
	- A 32x32 image has 3072 input features
# Parameter Explosion
- For a stupid 10 neuron model for 32x32 images, there are already 30730 parameters
- For more detailed images, the number of parameters can explode
# Softmax
- The output of the multi-class network should be a list of probabilities
	- The probability that the input is an instance of each class
- These outputs should sum to 1, 
- The softmax function maps inputs of an arbitrary distribution to a distribution whose sum is 1
- $$\sigma(z)_{i} = \frac{e^{z_{i}}}{\sum_{j=1}^Ke^{z_{j}}} $$
	- Function takes a vector of $K$ real numbers and outputs $K$ numbers between 0 and 1 that sum to 1
	- The denominator is the sum of all exp(input)
# Negative Log Likelihood (NLL)
- $NLL = -\sum\log(out_{i}[c_{i}])$
	- Sum is taken over the correct class for each sample in the batch ($c_{i}$)
	- 
For class #intro-ML