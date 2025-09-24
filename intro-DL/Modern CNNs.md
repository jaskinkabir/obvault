Continues [[CNN Convolutional Neural Network]]
Continued by [[RNN Recurrent Neural Network]]
# VGG

# GoogLeNet
- Uses a 3-step design
	- Stem: First 2-3 convolutions
		- Extracts low-level features from underlying images
	- Body: Several convolutional blocks
	- Head:
		- Maps features to the required problem
## Inception Block
- ![[Pasted image 20250203170144.png]]
- Uses 1x1 convolution to reduce number of output channels
	- Linear combination of input channels into one output channel
- The concatenation occurs along the channel dimension
	- Output is 4 channels of images of different dimensions

For class #intro-DL
