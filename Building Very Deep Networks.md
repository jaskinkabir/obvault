Continues [[CNN Convolutional Neural Network]]

# Skip Connections
- For very deep networks, a long chain of multiplications will tend to make the contribution of a parameter to the gradient *vanish*
	- That layer will not be properly updated, which makes training impossible past a certain network depth
	- The solution to this problem was presented in a paper about ResNets that uses skip connection to solve this problem
- A skip connection is formed by adding the inputs of one layer to the output of that layer
	- Also called identity mapping
	- ![[Pasted image 20241208132502.png]]
	- This creates a direct path from deeper parameters to the los
	- THis makes their contributions to the gradient more direct
# Fighting Overfit With Regularization
## Dropout
- Add a layer to the network that is only active during training
- During each training epoch, select some random fraction of outputs from the previous layer and set their activations to 0 before passing the activations to the next layer
## Batch Normalization
- This is only possible because of GPU architecture
	- Parallelism
- Instead of only applying normalization to the inputs of the network, apply normalization to the outputs of a hidden layer before it is passed onto the next layer
- This can prevent the outputs from moving too far into the saturated portion of the activation function, which ensures more information is passed through the network
- Just like with input feature scaling, the normalization should behave differently during training versus inference
	- During inference, the mean and standard deviation used for normalization should not be recalculated
	- This is so that the outputs for a specific input do not depend on the statistics of the other inputs
- We do not have to compute this normalization at each epoch, because that is not enough granularity
	- Compute the normalization at each training batch
- Process is
	- Compute outputs of layer for entire batch at once
	- Normalize 
	- Pass to next layer
- 
# Building a ResNet
- Residual networks can be very deep
## ResBlocks
- A resblock consists of
	- convolution 
	- batch normalization
	- activation
	- Skip connection
- Note that the resblock does not include a pooling step
	
For class #intro-ML