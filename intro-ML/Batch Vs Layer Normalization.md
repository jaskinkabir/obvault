Continues [[Building Very Deep Networks]]
# Internal Covariate Shift
- Consider this scenario
	- Gradient descent causes the layer before the current layer to drastically change its output
	- Now the current layer must drastically change its weights at the next step of gradient descent
- This phenomenon is called **Internal Covariate Shift**
	- The variance of the model weights across a training run will be high
# Solutions
## Batch Norm
- With batchnorm we normalize by columns (features)
	- Normalization of input features with respect to each batch
- In each batch, find $\mu$ and $\sigma$ of each feature in each batch
- Standardize the features of each datapoint in the batch according to these stats
- With batchnorm we normalize each feature of each datapoint with respect to all datapoints in the batch
- With layer norm we normalize the features in each datapoint with respect to the other features in the datapoint
## RMS Layer Norm
- Take the root-mean-square of each feature in each data point
- Transform each feature of the datapoint by scaling by the RMS
- ![[Pasted image 20250421164112.png]]
	- The learnable parameter gamma ($g$) is multiplied by the normalized values
For class #intro-ML