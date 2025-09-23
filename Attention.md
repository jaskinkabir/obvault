# Confusion Matrix
- Attention is training a classifier to choose which input token is most relevant for the current output step
- The confusion matrix for a general classifier ideally has max values along the diagonal
- For an attention classifier, this is the worst result. This means that the model is simply learning to associate input token t with output step t
- The ideal case is a uniform distribution of values
- 