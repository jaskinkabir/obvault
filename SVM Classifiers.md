Continues [[Classifiers]]
# Intuitive Definition of Support Vector Machines
- A linear discriminative classifier would attempt to draw a straight line separating the two sets of data
	- This line has a width of zero with no margin
	- A point is either on one side or the other
- Rather than simply drawing this zero-width line, we can draw around each line a **margin** of some width, up to the nearest point in the training data
	- Any point that falls exactly on the margin is called a **Support Vector**
- In Support Vector Machines, the line that maximizes this margin is the optimal model
	- This is called a **Maximum Margin** Estimator
# Mathematical Computation
## Intuition
- The SVM involves finding the optimal hyperplane where the margin between the nearest correctly classified points is maximized
	- Hyperplane: Any flat $N-$dimensional surface that occupies an $N+1$ dimensional space
- Consider a binary classification problem with two classes: $\pm 1$
- The equation for the linear hyperplane separating the two classes is $w^{T}x + b = 0$
	- The vector $w$ represents the vector normal to the hyperplane.
		- $w$ is not a unit vector, its length is inversely proportional to the margin
	- The parameter $b$ represents the offset or distance of the hyperplane from the origin along the normal vector $w$
## Distance From Hyperplane
- The distance between a datapoint $x_{i}$ and the decision boundary can be calculated with these steps
	- First, find some point $x_{0}$ on the hyperplane
		- Any point that satisfies $w \cdot x=0$ is on the hyperplane
	- Next, form a vector from $x_{0}$ to $x_{i}$
		- This vector is $x_{i}-x_{0}$
	- Finally, project $x_{i}-x_{0}$ onto $w$
		- The projection of a vector $a$ onto $b$ is given by $$proj_{b}a= \frac{a\cdot b}{||b||}$$
		- Thus, the distance $d$ can be found with $$d=\frac{|(x_{i}-x_{0})\cdot w|}{||w||}$$
	- This can be simplified further
		- Since $w_{0}$, is on the hyperplane, $w \cdot x_{0}=-b$
		- Thus the distance of point $x_{i}$ from the hyperplane can be calculated with: $$d_{i}=\frac{|w^{T}x_{i}+b|}{||w||}$$
			-  $||w|| = \sqrt{ w.w }$
				- Euclidean length of vector
## Finding the Margin
- The margin can be defined as the space that exists between the hyperplane and two more hyperplanes on which the support vectors lie
- We can define these two boundary hyperplanes with $w \cdot x+b=-1$ and $w \cdot x+b=+1$
	- The values of $\pm1$ are not arbitrary, the classifier is supposed to classify points with labels $\pm 1$, so the support vectors should lie exactly at $\pm 1$
- The total margin $m$, or the distance between the support vectors, can be found as follows:
	- The distance from $w$ to the positive boundary hyperplane can be found with $d_{+}=\frac{|w^{T}\cdot x+b|}{||w||}=\frac{1}{||w||}$
	- The distance from $w$ to the negative boundary hyperplane can be found with $d_{-}=\frac{|w^{T}\cdot x+b|}{||w||}= \frac{|-1|}{||w||}=\frac{1}{||w||}$
	- Thus, the total margin $m=d_{+}+d_{-}=\frac{2}{||w||}$
- ![[Pasted image 20241031183534.png]]
### Reason for Using the Margin Approach
- The two support vectors will result in a distance of $\pm 1$. Any data point further away from the hyperplane will have greater distance magnitudes
- Any data point between the hyperplane and the margin will have a fractional distance, but its sign is still used for classification
- Thus, the margin is not used during inference/classification. The decision boundary still has a width of 1. However, during training the decision boundary that creates the largest margin is selected, which can lead to better classification results.
- Thus, the predicted class of any data point $x$ is done through the calculation of
	-  $\hat{y}=\text{sign}(w^{T}\cdot x+b)$
# Optimization Problem
- The optimal vector $w$ used to classify the data is one for which $m=\frac{2}{||w||}$ is maximized
	- This means minimizing $\frac{||w||}{2}$
	- To ensure that the curve of the optimization problem is convex, we instead try to minimize the quantity $\frac{1}{2}||w||^{2}$
- 
