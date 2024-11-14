Continues [[Classifiers]]
# Bayes Theorem
- Bayes theorem states that $$p(A|B)=p(A) \frac{p(B|A)}{p(B)}$$
	- Where $p(A),\, p(B)$ are independent probabilities
	- $p(A|B)$ is the probability of $A$ given $B$
	- $p(B|A)=\frac{p(A\cap B)}{p(A)}$
- To classify data point $d$, Bayesian classifiers use this theorem in the following way: $$p(c_{j}|d) = \frac{p(c_{j})p(d|c_{j})}{p(d)}$$
	- $p(c_{j}|d)$: probability of instance $d$ being in class $c_{j}$ **POSTERIOR**
		- This is what we are trying to compute
	- $p(c_{j})$ number of occurrences of class $c_{j}$ in training data divided by number of training points **PRIOR**
		- How frequent class $c_{j}$ occurs in training
	- $p(d|c_{j})$: Probability of generating instance d given class $c_{j}$ **LIKELIHOOD**
		- Being in class $c_{j}$ causes feature $d$ with some probability
	- $p(d)$ **EVIDENCE**
		- Can be ignored because it is the same for all classes
- Example: Classifying Drew as female or male
	- $p(male|drew)= \frac{p(drew|male)p(male)}{p(drew)}$
		- $p(male|drew):$ probability of someone named drew being male
		- $p(drew|male)$: probability of a male being named drew
- $$P=\frac{\text{prior} \times \text{likelihood}}{\text{evidence}}$$
# Naive Bayes Classifier
- How can we use this to classify points that have many different features?
## Naivete and Independence
- Two events A, and B are independent if
	- $p(A \cap B)=p(A)*p(B)$
	- $p(A|B)=p(A)$
		- $\frac{p(A \cap B)}{p(B)}=p(A)$
	- $p(B|A)=p(B)$
		- $\frac{p(A\cap B)}{p(A)}=p(B)$
- The "Naive" is the assumption that each feature $x_{i}$ is conditionally independent of every other feature $x_{j}$ for $j \neq i$ given the category $C_{k}$
	- Thus $p(x_{i}|x_{i+1},\,\dots,\,x_{n},\,C_{k})=p(x_{i}|C_{k})$
	- In other words, the only probabilities that affect the probability that a given class has feature $x_{i}$ are the probabilities of an instance being that class and the probability of an instance having that feature
	- No feature affects any other feature
## Discrete Feature Model Definition
- Define the following equation:$$p(C_{k}|X)=\frac{p(C_{k})p(X|C_{k})}{p(X)}$$
	- Where $X=x_{1},\dots,x_{n}$ (feature vector)
- This can be expanded into the following iterative product: $$p(C_{k}|x)=\frac{p(C_{k})\prod_{i=1}^{n}p(x_{i}|c_{k})}{p(X)}$$
	- Since $p(X)$ is constant with respect to $k$, we can write this relationship in terms of proportionality: $$p(C_{k}|X)\propto p(C_{k})\prod_{i=1}^{n}p(x_{i}|c_{k})$$
		- Where the constant of proportionality is $\frac{1}{p(X)}$
- We can classify a new point $x$ by taking the highest probability according to the following formula $$\hat{y}=max_{k\in\{  1,\dots,K\}}\left(p(C_{k})\prod_{i=1}^{n}p(x_{i}|c_{k})\right)$$
	- Problem: this is a product of very many small numbers. This could run into overflow/underflow
		- **Underflow:** A problem that occurs when the result of an operation is larger than the range of values that can be represented by the hardware
			- I.e. $P(x_{1}|C_{1}) =7 \times 10^{-3}$ and $P(x_{2}|C_{1})=7 \times 10^{-4}$
			- The probability $P(C_{1})|X)=P(C_{1} *P(C_{1}|x_{1})*P(C_{1})|x_{2})=4.9 \times 10^{-8}$ cannot be represented by an 8-bit floating point number
			- The range of 8-bit floating point is $[7.8 \times 10^{-3},\,4.8 \times 10^{2}]$. The probability described above lies below this range and thus causes underflow
	- Problem: If one of these likelihood probabilities is 0, the entire term becomes 0 and cancels out every other feature's likelihood
	- Solution: use logs and add
- $$max_{y_{k}}\log P(Y=y_{k})+\sum_{j=1}^{n}\log P(X_{j}=x_{j}|Y=y_{k})$$
	- Using a logarithmic calculation has two benefits
		- It solves the problem of underflow by increasing the value of the probability
		- It solves the problem of 0 probability because $\log(x) \neq 0\ \forall x$
			- $\forall$=for all
		- It changes the multiplication operation to addition, which is faster in hardware
- Laplace Smoothing:
	- Calculate likelihood using the following formula
	- $$p(X_{i}=x|Y=y)=\frac{cnt(X_{i}=x,\, Y=y)+1}{\sum_{x'}cnt(X_{i=x'},\, Y=y)+|values(X_{i})|}$$
		- Where $x'$ is not x
		- Where $|values(X_{i})|$ is the number of values $X_{i}$ can take 
		- This solves the problem of a probability of 0
## Naive Bayes Graphical Model for Discrete Inputs
- ![[Pasted image 20241008135035.png]]
- Each node has a conditional probability table conditioned by its parents
	- For each possible value of $X_{i}$ and $Y_{i}$, calculate and store the value $p(X_{i}|Y_{i})$
- Predicting the class of instance $X$ requires computation of this formula: $$\hat{y} = max_{k}\left(P(X|C_{k})=\sum_{i=1}^{n}P(C_{k})*P(X_{i}|C_{k})\right)$$
## Continuous Features (Gaussian Naive Bayes)
- The above technique only works when the features take on discrete values. What if the features are continuous? (i.e. breast size for cancer classification)
- First we must segment the training data by class and compute the mean and variance of $x_{j}$ in each class $C_{k}$
	- $\mu_{j,k}:$ Mean of feature $x_{j}$ for class $C_{k}$
	- $\sigma_{j,k}:$ Variance of feature $x_{j}$ for class $C_{k}$
- Then we can create a Gaussian normal probability density function that computes the likelihood of generating a data point whose feature $x_{j}$ has value $v$ given its class is $C_{k}$   $$p(x_{j}=v|C_{k})=\frac{1}{\sqrt{ 2\pi\sigma^{2}_{j,k} }}e^{- (v-\mu_{j,k})^{2}/2\sigma^{2}_{j,k}}$$
	- For each combination of $x_{j}$ and $C_{k}$
	- This is it for training. Training a Gaussian Naive Bayes classifier purely involves calculating the mean and variance for each feature of each class
- To predict the classification of a certain point, we must compute each of these probabilities and add the log probability of the class occurring 
	- $$\hat{y}=max_{\{ k \}}\,\ p(v|C_{k})=\log(p(C_{k})) + \sum_{j=1}^{J}\log\left(\frac{1}{\sqrt{ 2\pi\sigma^{2}_{j,k} }}e^{- (v_{j}-\mu_{j,k})^{2}/2\sigma^{2}_{j,k}}\right)$$
	- Where $\hat{y}$ is the predicted class of a data point whose features are contained in vector $v$
### Problem: Assumption of Normality
- This technique assumes that the features are normally distributed. In real life this may not always be the case
- In this case, other probability distribution functions must be used
## Explainability of Bayes Classifiers
- Logistic Classifiers use gradient descent to find a decision boundary used to classify data
	- If somebody asks you to explain why your model classified a data point as some class, you wouldn't be able to
	- The training process abstracts away that decision making
- Naive Bayesian models classify data based on calculable probabilities 
	- It is much more explainable
	- You can point to the actual probability calculations
- This explainability is very attractive for security and ethical purposes
- But Bayesian classifers consistently underperform logistical classifiers, and neural networks blow them out of the water
- However, the explainability of Bayesian classifiers can sometimes outweigh this in cases where security or ethics is a big concern

For class #intro-ML