# Difference Between ANN and Classical ML
- A neural network has no fixed model
	- A neural network is **Model-Free**
- Classical ML assumes that there is some sort of linear relationship in the data that can be found with the right parameters, features, etc
	- Example: Logistic regression assumes that the sigmoid function can be fit to the data
- ANN only needs a definition of the boundaries of learning, but can learn any arbitrary pattern within the data
## Activation Function
- A neuron within a NN is just a perceptron
- In order for the neural network to recognize nonlinearities in the data, the neurons need nonlinear activation functions
- ReLU is used the most because it is easy to compute
- Sigmoid preserves the most information but is harder to compute
## Model-Free
- Deep neural networks give us the ability to approximate highly nonlinear phenomena without an explicit model for them
- The DNN does not worry about the exact function that represents the data (linear, quadratic, piecewise, etc)
	- A DNN has a **universal** approximator and a method to estimate its parameters
	- The approximator can be customized to the needs of the problem just by composing simple building blocks

For class #intro-ML