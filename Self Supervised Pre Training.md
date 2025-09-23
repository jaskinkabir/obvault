- Mask the embedding not the raw sequence input
- Train model to reconstruct missing/masked embedding
- Use this self supervised method on smaller dataset
	- Null the class token
- Then fine tune on much larger dataset
# Steps
1. Train the embeddings and attention heads for feature extraction with self-supervised learning
	1. Mask certain patch embeddings and train the model to reconstruct missing embeddings
	2. Null the class token and ignore it during training
2. Train the attention heads to transfer feature information to the class token with supervised learning
3. Fine tune the head for the final task
