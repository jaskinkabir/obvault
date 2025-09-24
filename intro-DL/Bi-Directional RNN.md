# Motivation
- Consider language prediction
- In this case, the only useful conditioning direction is from the first input token to the last
	- The leftward context
	- The only tokens that inform the output are to the left of the current input
- But other sequence learning tasks may require conditioning of the prediction at every time step on both the leftward and rightward context
	- Example: part of speech detection
	- Part of speech could change based on words to the left or right of the current word, so both contexts must be 

# Encoder Decoder Networks
- The problem is a seq2seq problem where the inputs and outputs are of varying lengths that are unaligned
- In this case, the input is called the **Source Information Sequence** and the output is the **Target Information Sequence**
- An **Encoder Network** is an RNN that takes a variable length sequence as an input and generates a tensor in some **latent space**
- This tensor is then passed to a decoder network. 
- The **Decoder Network** is another RNN that uses the encoded input and the leftward context of the target information sequence to generate the next token of the target sequence
- ![[Pasted image 20250226165006.png]]
## Conditional Language Models
- A Language model learns the probability that the input sequence is valid
	- $$P(y_{1},\, y_{2},\, \dots,\, y_{n}) = \prod_{t=1}^{n}p(y_{t}\mid y_{<t})$$
- A **Conditional Language Model** learns the probability of the input sequence *given* the source sequence
	- $$P(y_{1},\, y_{2},\, \dots,\, y_{n} \mid x) = \prod_{t=1}^{n}p(y_{t}\mid y_{<t},\, x)$$
## Encoder Decoder Architecture
- ![[Pasted image 20250226165517.png]]
- The source sequence is encoded into the embedding space
- The decoder takes the embedding of the current token concatenated with the leftward context of the source sequence and then outputs its own hidden state tensor
	- This output tensor is the representation of context (the source sequence and history of target predictions)
- This hidden state is passed to a linear classifier that predicts the next token
## EDN Training
- Given an example source and target:
	- Run the encoder on the source data until the full sequence has been embedded into the latent space
	- Predict token $t_{0}$ 
	- Compute loss from ground truth token 0 and backpropagate all the way back through the encoder
		- In this way, the encoder and decoder networks are trained at the same time
For class #intro-DL