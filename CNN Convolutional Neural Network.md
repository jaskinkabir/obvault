Continues [[Image Classification With ANN]]
Continued by [[Building Very Deep Networks]]
# Weakness of Fully Connected Image Processing
- Sees image as just one dimension
	- Lose information
- Insanely computationally expensive
	- Feature explosion due to resolution of images
# CNN
## Basic Idea
- Rather than a fully connected network where every feature goes through each neuron, have a structural feature that can understand the features of the image
- Consider 32x32 image
	- Arranged from $P_{1,\,1}\dots P_{32^{2},\,32^{2}}$
	- Assume convolutional filter matrix is 5x5
		- This is a matrix of 25 weights
		- Organized from $w_{1}\dots w_{25}$
	- The 5x5 filter is placed onto the top 25 pixels of the image
		- Take the sum of dot products
		- $w_{1}P_{1,\,1}+w_{2}P_{1,\,2}+w_{3}P_{1,\,3}+w_{4}P_{1,\,4}+w_{5}P_{1,\,5}+w_{6}P_{2,\,1}+w_{7}P_{2,\,2}\dots w_{25}P_{5,\,5}$
	- Move this filter across by $n$ pixels and repeat until the end of the image is reached
		- If the original image was $h\times w$ resolution, the new image formed by the convolution has resolution $\frac{h}{n} \times \frac{w}{n}$
		- Reduction in input features by a factor of $n^{2}$
- One layer of the network contains some number of convolutional filter networks
	- Convolve the image into a lower dimension, then apply ReLU to the image and pass it to the next convolutional filter
	- Through convolution you can represent abstract features of the image
## Pooling
- Every few layers, add a pooling layer to pick out the most important features to pass to the next stage of the network
- ![[Pasted image 20241126133901.png]]
### Max Pooling
- Provided by `nn.MaxPool2d`
- Takes as input the size of the neighborhood over which to operate the pooling
- Divide convolution output into sections, take the max of each section
	- ![[Pasted image 20241126133853.png]]


## Building Model (Forward/Inference Direction)
- Consider a model with 1 hidden layer of 4 neurons followed by a second layer of 3 neurons
- ![[Pasted image 20241126140147.png|1000]]
- Start with 3 channel RGB image
	- 3 channel, 32x32 into 4 neurons
	- Each neuron has i-1 convolutional kernels in it and produces i-1 images
	- Sum the images, output of 1 neuron sum is 1 32x32 image
	- output of 1 layer is l_1 32x32 images
- Pass through hidden layer of 4 neurons
	- Pass through 4 3-channel convolutional filters
		- Each neuron has 3 internal filters, and outputs 3 'images'
	- Sum up the channels
	- Pass through nonlinear activation
	- Pass through max pooling
	- 4 output 'images' (abstract 2x2 matrices)
- Pass through hidden layer of 3 neurons
	- Pass through 3 4-channel convolutional filters
		- Each neuron has 4 internal filters
	- Sum
	- Activation
	- Pooling
	- Outputs 3 matrices
- Unroll these matrices into a 1-dimensional vector
- Pass the vector into a fully connected logistic classifier ANN
## Training Model
- In terms of PyTorch, it's the exact same method as a fully connected classifier
- Use some loss function, and then `loss.backward()`
# Building a CNN in PyTorch
- 