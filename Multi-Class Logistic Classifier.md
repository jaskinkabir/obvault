Continues [[Logistic Classifiers]]
# How to use Logistic Regression For N-Class Classification
- Train $N$ models, where each model is trained to predict the probability that a data point is either part of class $n$ (positive), or not class $n$ (negative)
- To predict the class of a data point, run prediction for each of these models. The predicted class is the class with the highest predicted probability 
- 

# Calculating Precision and Recall
- For each class $n$:
	- Assume $n$ is positive, $\overline{n}$ is negative
	- $TPR_{n} = \frac{TP}{TP + FN}$, recall
	- $PPV_{n} = \frac{TP}{TP+FP}$, precision
	- Take the average across all $n$ classes
- $$TPR = \frac{1}{N}\sum_{n=0}^NTPR_{n}$$
- $$PPV = \frac{1}{N}\sum_{n=0}^{N}PPV_{n}$$