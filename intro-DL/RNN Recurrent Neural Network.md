Continues [[CNN Convolutional Neural Network]]
Continued by [[Modern RNNs]]
# RNN
- Countless learning tasks involve learning from sequential data
- RNNs are deep learning models that capture the dynamics of sequences via reccurent connections
	- These can be thought of as cycles within the network of nodes
![[Pasted image 20250213173144.png]]
- State at any time step $t$ can be computed based on the current input $x_{t}$ and the previous state $h_{t-1}$ $$h_{t}=f(x_{t},\, h_{t-1})$$
## Key Insight:
- While the inputs and targets for many fundamental ml tasks cannot be easily represented as fixed length vectors, they can be as varying-length sequnces of fixed-length vectors
	- Like a video as a varying length sequence of images
![[Pasted image 20250213173503.png]]

# Mathematical Model
- Within the model is some hidden state $H_{t}$
	- This is simply the activations
- Upon each input, the current activations are computed as the current input concatenated with the previous activations. This output is then stored and used to calculate the next activations
- At any time step $t$. the computation of the hidden state can be treated as
	- 1. Concatenating the input $X_{t}$ and the hidden state $H_{t-1}$
	- 2. Feeding the concatenation result into a fully connected layer with the activation function $\phi$
- The output of this FC layer is the hidden state $H_{t}$
$H(I+H+B+O)+BO$
- The model parameters are the concatenation of 
![[Pasted image 20250213173741.png]]
## Example 
![[Pasted image 20250213174618.png]]
- At time step 3, the output depends on the previous 2 hidden states as well as the current input
- In other words it depends on the string of inputs "m" "a" "c"

# Building an RNN
- Pass the input sequence to the RNN layer
- The output of the RNN has an extra dimension for time step
	- Output Size (hidden state) x time step x batch
- Pass the activations from the current time step to the fc layer
For class #intro-DL 
