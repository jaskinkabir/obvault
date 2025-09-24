# Transformers and Graphs
- Assumes all input tokens are connected to each other
- The input is a fully connected graph
- The learning task of attention is to discover the relationship graph of the input space
- **Transformer attention learns graphs**
# Vehicle Trajectory Prediction
- Must regress the position of each car
- Represent each frame as a graph
	- Cars are nodes
	- Create edges directly in front and behind each car
- **GNN Acts Like Encoder**
- Creates richer embeddings

For class #intro-DL