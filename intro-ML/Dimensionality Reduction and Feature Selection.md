Continues [[Classifiers]]
Continued by [[Feature Mapping and Kernelization]]
# Why Reduce Dimensionality
- Ease of visualization
- Data compression
- Noise removal
- The **intrinsic** dimensionality may be small
	- For example, the # of genes responsible for a disease may be small
## The Curse of Dimensionality
- If the number of features $d$ is large, the number of samples $n$ maybe too small for accurate parameter estimation
- Increasing the number of features will not always improve accuracy
	- It may even worsen performance
- The number of training samples required increases exponentially
	- $k^{d}$, where $k$ is the number of classes

# Dimensionality Reduction Techniques
## Feature Selection
![[Pasted image 20241010134045.png]]
- Chooses an optimal subset of features according to an **objective function**
- Removes features that have the least impact on performance
- Example: 
	- Classify horse vs. Zebra
	- Both have 4 legs
	- Both have same shape
	- But color and color pattern are the most discriminative features
### Objectives
- Reduce dimensionality 
- Improve mining performance
	- Speed of learning
	- Accuracy
	- Simplicity and comprehensibility of mined results
## Feature Extraction
- Mapping of high-dimensional data onto a lower-dimensional space
- Given a set of data points of $p$ variables $\{ x_{1},x_{2},\dots x_{n} \}$
	- $x_{i} \in \mathcal{R}^{d} \to y_{i} \in \mathcal{R}^{p},\, (p \ll d)$
- Comparable to mp3/jpeg compression
- From a mathematical standpoint finding an optimum mapping is equivalent to optimizing the objective function
- Different methods use different objective functions
	- **Information Loss:**  Goal is to represent the data as accurately as possible without loss of information in the lower-dimensional space
	- **Discriminatory Information**: Goal is to enhance the discriminatory information in the lower-dimensional space
### Techniques
- Linear methods include:
	- Principal Components Analysis (PCA):
		- Seeks a projection that **preserves as much information as possible**
	- Linear Discriminant Analysis (LDA):
		- Seeks a project that **best discriminates the data**
- Other interesting methods
	- Retaining interesting directions (Projection Pursuit)
	- Making features as independent as possible (Independent Component Analysis or ICA)
	- Embedding to lower dimensional manifolds (isomap, locally linear embedding/LLE)
### Principal Component Analysis
- Tries to put the maximum possible amount of information, the max remaining info in the second component, and so on
	- ![[Pasted image 20241010135915.png]]
#### What are Principal Components?
- Principal components are new variables that are constructed as linear combinations of the initial variables
	- They should be uncorrelated with each other
	- They are less interpretable. They do not have any real meaning because they are constructed as linear combinations of the initial variables
- The larger the variance carried by a component, the more information it has
- Each principal component accounts for the **largest possible variance** in the dataset
For class #intro-ML