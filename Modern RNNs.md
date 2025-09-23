Continues [[RNN Recurrent Neural Network]]

# RNN Long-Term Information
- As the gap between the relevant information and the point where it is needed grows, the RNN becomes unable to learn to connect this information
	- Example: "I grew up in France...I speak fluent *French*"
	- The model should predict the word French, but to do so it must remember the context of France from earlier in the sentence
	- As the omitted part of the sentence grows, the RNN becomes less able to handle the task
# LSTM (Long Short-Term Memory)
- Explicitly designed to avoid the long term dependency problem
- In a traditional RNN, the repeating module that generates the hidden state is simple in structure. Like a single \tanh layer
- In an LSTM, the structure is more complex
- ![[Pasted image 20250227124840.png]]
- The key is the cell state, the horizontal line running through the top of the diagram
- As the information (previous cell state $C_{t-1}$) passes along this line, it passes through gates
## LSTM Gates
- These gates dynamically allow a certain amount of information through
	- Each gate is a neural net layer passed to a sigmoid activation and then a pointwise multiplication operation
	- The sigmoid outputs fractions, which represent the amount of information to let through that gate
- An LSTM has 3 Gates
	- **Forget Gate** Decides which information to discard from the block
		- Example: A woman is mentioned and so the cell state contains this gender info
		- A new subject is read, so the gender of the old subject should be forgotten
	- **Input Gate** Decides which values from the input should update the cell state
		- This is where new information is added to the cell state
	- **Output Gate** Decides what to output based on input and memory of the block
		- Decides what the output should be based on a filtered version of the cell state
		- The tanh on the cell state is used to map the values to -1 to 1 so that the output activations can be appropriately scaled by the output gate
		- Note that the output gate has no bearing on the current cell state
			- It only decides what the output should be
	- ![[Pasted image 20250227142823.png]]
## Math Description
$H_{t} = \tanh(C_{t}) \circledcirc O_{t}(H_{t-1}+X_{t})$

$C_{t} = C_{t-1} \circledcirc F_{t}(H_{t-1} + X_{t}) \oplus I_{t}(H_{t-1} + X_{t}) \circledcirc \overline{C}_{t}(H_{t-1} + X_{t})$
$H_{t} = \tanh[C_{t-1} \circledcirc F_{t}(H_{t-1} + X_{t}) \oplus I_{t}(H_{t-1} + X_{t}) \circledcirc \overline{C}_{t}(H_{t-1} + X_{t})] \circledcirc O_{t}(H_{t-1} + X_{t})$
## Intuition
- An LSTM is at a high level an RNN with a second mode of memory
- The hidden state uses the same mechanism and can maintain a short context window
- The cell state is changed using a much simpler process, just pointwise operations, so long term information can be stored in this vector
- But the forget gate allows it to choose which information is worth storing
## LSTM Complexity
### Parameters
- Each gate has $D_{x}+D_{h}$ inputs, $D_{n}$ outputs so
	- $D_{n}(D_{h}+D_{x})$ weights and $D_{n}$ biases
- With 4 gates: $4(D_{n}(D_{h}+D_{x})+D_{n})$
- $8D^{2}$ parameters if input and output dims are the same
### MACs
- Each weight is involved in one MAC
- Plus $3D_{h}$ multiplies for the gates and activations, but these tend to be negligible.
## Bi-Directional LSTM
- More surrounding context
- 2x params, 2x compute
	- Need different weights for each direction
- Higher latency, not good for real-time applications
## LSTM Challenges
- Sequential processing makes them difficult to parallelize
	- Don't fully utilize GPUs
	- Long training time
- Vanishing gradients, particularly over very long sequences
	- If forget gate = 0.99, over 500 steps, $0.99^{500}<0.01$
- Sensitive to quantization noise for the same reason
	- Quantization noise stacks over time steps
# GRU (Gated Recurrent Unit)
- The GRU offers a streamlined version of the LSTM that uses 3 gates instead of 4, which makes it faster to compute
- These gates are
	- **Reset Gate**
		- How much of the previous state to remember
	- **Update Gate**
		- How much of the now state is a copy of the old state
- ![[Pasted image 20250227190738.png]]
- Only has one state that is maintained across sequence elements
- 

For class #intro-DL 