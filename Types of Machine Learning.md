Continued by [[Supervised Learning - Training]]
Continued by [[The Perceptron]]
# Supervised
- Use a series of labeled examples with direct feedback
	- includes correct answers
- Disadvantage is you need large sets of labeled data
- Primarily learn this technique in this class 
# Unsupervised/Clustering
- Learning with no feedback
- Training data includes no correct answers
# Reinforcement Learning
- Indirect feedback, after many examples 
- **Can be considered a form of supervised learning** 
- Good for personalization/customization
- Example: Hot or Cold
	- Looking for object, someone says hot as you get closer or cold when you get further
	- The person saying 'hot' or 'cold' is a reward function
# Semi-Supervised Learning
- Partially labeled samples and possibly (a lot of) unlabeled samples
# Self-Supervised Learning
- Also called **Weakly Supervised**
- **Subset of Supervised Learning**
	- Techniques for supervised learning can be applied to self-supervised learning
- Defined as follows:
	- The labels, or the correct answers are implicitly part of the input/training data
	- The correct answers must be extracted/extrapolated
- Won't be taught in this class
- Popular in the deep learning era
- Example for image classifier between cats and humans
	- Randomly pick a piece of a single image of a cat and mask it
	- Use the unmasked portion as the 'correct answer' as in supervised learning 
	- Over time it will be able to look at pictures of humans with blurred faces that the missing piece is its face; the missing piece of the cat is its feet and so on
		- In doing this, in learning to figure out what is missing from an image of a cat or human, it figures out what a proper image of a cat or human looks like!
	- You can then change its output parameters from, in this example a bunch of pixels, to a binary set of outputs representing cats and humans
- The learning is an emergent phenomenon of this method, it's very wacky and alien
- The crucial property of this technique is that the AI is trained for a completely different task than it's eventually used for

For class #intro-ML
