Continued by [[CNN Complexity and Filtering Techniques]]
Related to [[Artificial Neural Networks (ANN)]]
# Single Dense Layer
## Params
- Each neuron in a layer has a number of weights equal to the input size, and a bias
- Thus the total number of parameters for each layer is $D_{in} * D_{out}+D_{out}$
## MACs
- Each neuron performs a number of MACs equal to the input size
- Thus the total number of MACs is $D_{in}*D_{out}$
## SRAM
- The activations of each layer must be stored in SRAM during the forward pass
- The activations is simply the output dimension
# Dense Model
## Params:
- Let $N_{i}$ be the number of neurons in layer $i$, and $I$ be the total number of layers
	- $N_{0}=D_{in}$
	- $N_{I}=D_{out}$
- The number of parameters is $$\#P=\sum_{i=1}^{I}N_{i-1}*N_{i}+N_{i}$$
## MACs:
- $$\#\text{MACs}=\sum_{i=1}^{I}N_{i-1}*N_{i}$$
## SRAM:
- The minimum amount of SRAM is simply the largest number of activations needed for a single operation
- $$\text{SRAM} = \frac{\text{STORAGE}}{\text{ACTIVATION}} * max(N_{i-1}*N,\, \forall i,\,  1 \leq i \leq I)$$

For class #IoT-ML 