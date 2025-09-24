Uses [[CNN Convolutional Neural Network]]
Uses [[Model Regularization]]
Jaskin Kabir
github link:
https://github.com/jaskinkabir/Intro_IoT_ML/tree/master/hw5
# 1. Keywords
I chose to detect the key words 'stop' and 'go' from the mini version of the dataset
# 2. 80% Model
## Architecture
### English Description
The model uses the following layers in sequential order:
1. 2D Convolution:
	- 32 Filters
	- Kernel Size 5x5
2. 2D Convolution
	- 20 Filters
	- Kernel Size 3x3
3. Global Max Pooling
4. Dense
	1. In: 32
	2. Out: 4
This model was trained for 30 epochs on the mini speech commands dataset
### `model.summary()` Output

```
Model: "sequential"
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 conv2d (Conv2D)             (None, 16, 28, 32)        832       
                                                                 
 conv2d_1 (Conv2D)           (None, 14, 26, 20)        5780      
                                                                 
 global_max_pooling2d (Glob  (None, 20)                0         
 alMaxPooling2D)                                                 
                                                                 
 dense (Dense)               (None, 4)                 84        
                                                                 
=================================================================
Total params: 6696 (26.16 KB)
Trainable params: 6696 (26.16 KB)
Non-trainable params: 0 (0.00 Byte)
_________________________________________________________________
```
## Training Curves
![[Pasted image 20250418195626.png]]
# 3. FPR and FNRs

| **Word** | **FPR** | **FNR** |
| -------- | ------- | ------- |
| Stop     | 6.99%   | 39.81%  |
| Go       | 11.27%  | 46.61%  |
|          |         |         |
# 4. 10% Train-Test Acc Difference
The second convolution layer was changed to have 64 output filters instead of 20 and a 5x5 kernel rather than 3x3. This increased complexity resulted in a final training accuracy of 90.62% and a test accuracy of 79.60% after 30 epochs. The model learned more specific features of the training data that did not generalize to the test data.
# 5. Regularization
L1 and L2 kernel regularization was applied to each of the two convolutional layers in separate training runs. Each used a coefficient of 0.01 over 30 epochs.

| Model   | Train Accuracy | Test Accuracy | Difference |
| ------- | -------------- | ------------- | ---------- |
| Initial | 90.62%         | 79.60%        | 11.02%     |
| L1      | 76.625%        | 73.57%        | 3.06%      |
| L2      | 87.53%         | 81.89%        | 5.64%      |
Both regularization techniques decreased the difference between training and test accuracy, however L1 regularization reduced this difference more than L2 did. L2 increased test accuracy while L1 did not.

To explain these results, we must delve into the differences between the two regularization techniques. L1 regularization adds a penalty proportional to the *absolute* value of the weights $(|w|)$, while L2 regularization's penalty is proportional to the *squared* value of the weights $(w^2)$. As the weights get closer to zero, L1's penalty provides a constant push towards 0, whereas the L2 penalty decreases as the absolute value of the weight decreases. This makes L1 regularization more likely to shrink some weights exactly to zero, effectively performing feature selection and creating sparser models. This explains the significant reduction in the train-test accuracy gap, as the model complexity was reduced. It also explains the lower test accuracy, as potentially useful features may have been eliminated.  

Because L2 regularization is less likely to push weights to exactly zero, it provides a less aggressive form of regularization which often retains more features, potentially leading to better generalization and higher test accuracy--as observed here--while still reducing overfitting.

# 6. Sparsity

The sparsities of the layers in each of the three models trained for the regularization experiment were measured and recorded in the table below. This was done by finding the weight in the layer with the largest absolute value and calculating the fraction of weights whose absolute value was below 1% of this maximum value.

| Model   | Conv 1 | Conv 2 | Dense |
| ------- | ------ | ------ | ----- |
| Initial | 2.52%  | 5.22%  | 2.69% |
| L1      | 66.35% | 98.05% | 4.23% |
| L2      | 55.77% | 76.89% | 6.92% |
While L2 regularization resulted in the greatest sparsity of the final dense layer, L1 regularization led to the greatest sparsity in the two convolutional layers. In fact, L1 almost completely eliminated the weights in the second convolutional layer.  This increased sparsity of the models leads to a decrease in their capacity to learn the training features, which lead to decrease in training accuracies for both models. This is evidenced by the fact that the L1 model had greater sparsity as well as lower accuracies. 

While L2 regularization resulted in the greatest sparsity of the final dense layer, L1 regularization led to the greatest sparsity in the two convolutional layers. This aligns with the theoretical properties of these regularizers: the L1 penalty $(|w|)$ pushes weights to exactly zero, whereas the L2 penalty $(w^2)$ pushes weights to be small but non-zero. In fact, L1 almost completely eliminated the weights in the second convolutional layer. This increased sparsity reduces the models' capacity to learn intricate training features, leading to the observed decrease in training accuracies for both regularized models compared to the initial one. This effect is more pronounced in the L1 model, which exhibited greater sparsity and lower training/test accuracies. 

# 7. Reduced Dataset

In the training dataset, samples were randomly removed until there were only 25 samples for the word 'stop' and 250 for the word 'go'. The model was retrained with L1 regularization rather than L2 regularization. This choice was made because L1 regularization reduces the model's ability to overfit the imbalanced training dataset. The effect of L2 regularization would not be pronounced enough for this scenario. The results after evaluating the model on the test dataset can be seen below

| **Word** | **FPR** | **FNR** |
| -------- | ------- | ------- |
| Stop     | 0%      | 100%    |
| Go       | 1.49%   | 98.9%   |
The word stop had only 25 training examples, so the model learned to never classify a sample as 'stop' and it was still able to reach 78.13% overall test accuracy. Similarly for the word 'go', it learned to rarely classify a sample as 'go', however this push towards 0 positive predictions was not as strong since there were more samples for this class.

# 8. Sample Count Investigation

## Method
This experiment seeks to find the minimum amount of samples in the training data required for that class to reach a minimum True Positive Rate of 75% and a maximum False Positive Rate of 20% on the training data. For this experiment, no regularization was used. To start, the number of samples for the word 'stop' was limited to 1000 samples. This limit was then incremented by 100 samples until the required TPR and FPR values were reached. 

At 1000, the model learns to never predict the word 'stop' and the tpr and fpr are both 0. At 1500, the model has started to make positive predictions, but the tpr is only 25%. Finally, at 1700 samples, the True Positive Rate reaches 78.84% and the False Positive Rate reaches 17.98% after 30 epochs. 

For class #IoT-ML/homework