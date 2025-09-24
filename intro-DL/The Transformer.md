# RNN Drawback
- RNNs are sequential and do not benefit from parallelization
- Either need a new accelerator or a new algorithm
# Transformer
- The transformer was proposed by Attention is All You Need
- Since the RNN is sequential and thus inefficient, get rid of it entirely
- Replace it with attention blocks
## Steps
- Repeat N times
	- Compute how each input token is correlated to the others
	- Update the embeddings into new hidden states
	- AKA apply attention across input embeddings
	- Repeat N times
	- This is called the self attention state (look at each other)
- Repeat N times
	- Predict output token based on current output hidden state
	- Apply attention from previous output tokens
		- Self attention step
	- Apply attention from input hidden states
![500](https://3.bp.blogspot.com/-aZ3zvPiCoXM/WaiKQO7KRnI/AAAAAAAAB_8/7a1CYjp40nUg4lKpW7covGZJQAySxlg8QCLcBGAs/s640/transform20fps.gif)
# Self Attention (Look At Each Other)
- Calculating correlation: Repeat this for each input token/embedding
	- Pass the current token and one of the other tokens through a fully connected network
	- Do this for each other token
	- Pass the output of each combination into a softmax
	- The output of the softmax is the new hidden state for the current token
- Passing each token through this step of several fully connected networks and softmaxes creates a mapping from each input embedding to a hidden state in a latent space
- Repeat this process N times to create a 1-1 mapping from the input embedding to a hidden state that contains information from every other input embedding
## The Start Token
- The start token's embedding will be updated through these attention layers into a hidden state that represents the first predicted token of the output sequence
## Self vs Cross Attention
- The encoder only uses self attention, where the input embeddings are updated with respect to each other
- The decoder uses cross attention where the encoder embeddings are used to update the current prediction
- Then self attention is applied to the predicted sequence
## Query Key and Value in Self Attention
- Three weight matrices multiplied by each token embedding to generate three vectors
	- Query:
		- Represents the question the token is asking; what contextual information it needs
	- Key: 
		- Represents what contextual information the token has
	- Value:
		- Represents the extracted contextual information
- Process
	- For the current token, generate the query vector
	- For each target token, generate key and value vectors
	- Output of attention head is 
# Multi-Head Attention
- Use this query key value mechanism multiple times
- Concatenate the outputs vectors of each head into one vector
- Pass this vector through a Dense layer
- This is the output of the multihead attention

# Transformer Architecture
![[Pasted image 20250324165354.png]]
## Feed Forward
- Two dense layers with a relu in between
- This layer allows the network to 'think' about the results from the multi-head attention
## Layer Norm
- Normalizes vector representations of each example in the batch
	- Controls the flow of data to the next layer
- Improves convergence and stability
## Residual Connections
- A skip connection is made across each attention and fully connected block
## Positional Encoding
- The architecture needs some way to learn the relationship between the positions of each token in the sequence
- The positions need to be given to the model explicitly
- For this, we create two sets of embeddings
	- Tokens
	- Positions
- The input representation of a token is then the sum of these two embeddings
- The positional embeddings can be learned, but it does not always impact performance
## Sinusoidal Positional Encoding
- Define some parameters
	- $L$: Input Length
	- $d$: Embedding dimension
	- $k$: Position of a token in the input sequence
	- $P(k,\,j):$ Maps a position 
- Create a positional encoding matrix of dimension $L\times d$
- Each element of the matrix is given by the following:
	- For $i=\left[ 0,\, \frac{d}{2} \right]$
	- $$P(k,\, 2i)=\sin\left( \frac{k}{10000^{2i/d}} \right)$$
	- $$P(k,\, 2i+1)=\cos\left( \frac{k}{10000^{2i/d}} \right)$$
# Key Value Cache For Next Token Prediction
- Each prediction requires computing KQ vectors for each token
- However at each step of inference these computations are repeated
- Cache these repeated computations to improve speed
For class #intro-DL 
