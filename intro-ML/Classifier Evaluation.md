Continues [[Logistic Classifiers]]
Continues [[Multi-Class Logistic Classifier]]
Continued by [[Classification Threshold and Balancing Precision and Recall]]
# Evaluation Metrics
## Accuracy, Error Rate
- Accuracy is percent of correct classifications
- Error rate is percent of incorrect
	- Error rate = 1-accuracy
###### Problems
- Assigns equal weight to both false positives or false negatives
- Assumes uniform class distribution
	- A training dataset with a biased class distribution will affect training and lead to overfit
- Example: Rare disease classifier
	- Let's say there is a disease that affects only 98% of people
	- Your model always predicts that the patient does not have the disease
	- Testing on a general population will result in 98% accuracy
	- Clearly, false negatives must be weighted heavier than false positives
## Recall, Sensitivity, Hit Rate, or True Positivity Rate (TPR)
- $$TPR= \frac{TP}{P} = \frac{TP}{TP + FN}$$
	- Percentage of truly positive data points that were correctly classified as positive
	- A high TPR means the model minimizes false negatives
		- False positives do not affect this metric
## Precision or Positive Predictive Value (PPV)
- $$ PPV = \frac{TP}{TP + FP}$$
- Percentage of data points that were classified as positive that were truly positive
- A high PPV means the model minimizes false positives
	- False negatives do not affect this metric
## Precision Vs. Recall
- By increasing recall, we decrease precision and vice versa
- ![[Pasted image 20241001140919.png]]
## F1 Score
- $$F_{1} = \frac{2PR}{P+R}$$
	- $P=$Precision, $R=$Recall
- A higher F1 score means higher acuracy
- It can never be larger than 1
## Confusion Matrix
- The confusion matrix is a way to visualize the accuracy of the classifier
- Define the following matrix
	- ![[Pasted image 20241001134458.png]]
	- Darken the fill color of each of these four squares based on the number of predicted values that fall into each of these categories
	- ![[Pasted image 20241001134618.png]]
		- The axes are arbitrary
		- This is a good model because only 13.12% of points are classified in error
# Imbalanced Data
- Sometimes, the dataset will have a bias towards one class over the others
## Solutions:
- **Oversampling**: re-sampling of data from minority class
- **Under-sampling:** randomly eliminate samples from majority class
- Synthesizing new data points for minority class
	- Take averages of samples in minority class
	- Add small noise to samples in minority class
- ![[Pasted image 20241001141310.png]]
For class #intro-ML