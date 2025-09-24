Jaskin Kabir
801186717
Uses [[Complexity of Dense Layers]]
[[CNN Complexity and Filtering Techniques]]
# Model 1
## Params and MACs

| Layer     | Type        | Params     | MACs         | Output Size  |
| --------- | ----------- | ---------- | ------------ | ------------ |
| 1         | Convolution | 896        | 221184       | (16, 16, 32) |
| 2         | Batch Norm  | 128        | 0            | (16, 16, 32) |
| 3         | Convolution | 18496      | 1179648      | (8, 8, 64)   |
| 4         | Batch Norm  | 256        | 0            | (8, 8, 64)   |
| 5         | Convolution | 73856      | 1179648      | (4, 4, 128)  |
| 6         | Batch Norm  | 512        | 0            | (4, 4, 128)  |
| 7         | Convolution | 147584     | 2359296      | (4, 4, 128)  |
| 8         | Batch Norm  | 512        | 0            | (4, 4, 128)  |
| 9         | Convolution | 147584     | 2359296      | (4, 4, 128)  |
| 10        | Batch Norm  | 512        | 0            | (4, 4, 128)  |
| 11        | Convolution | 147584     | 2359296      | (4, 4, 128)  |
| 12        | Batch Norm  | 512        | 0            | (4, 4, 128)  |
| 13        | Convolution | 147584     | 2359296      | (4, 4, 128)  |
| 14        | Batch Norm  | 512        | 0            | (4, 4, 128)  |
| 15        | Max Pool    | 0          | 0            | (1, 1, 128)  |
| 16        | flatten     | 0          | 0            | (128,)       |
| 17        | Dense       | 16512      | 16384        | (128,)       |
| 18        | Batch Norm  | 512        | 0            | (128,)       |
| 19        | Dense       | 1290       | 1280         | (10,)        |
| **Total** | -           | **704842** | **12035328** | (10,)        |
## Training Results
![[Pasted image 20250212224149.png]]
Training accuracy is 100%, while validation accuracy is slightly above 60%. The complexity of the model allowed it to fully learn the training data, which means has poor ability to generalize to the validation data. There is significant overfit, and the model trained for more than enough epochs to reach its beDog Test
## Dog Test
I downloaded this image of a dog and scaled it down to 32x32
![[Pasted image 20250212230201.png|250]]
I then passed the image into the model trained above, and it correctly classified the image as a dog!

# Model 2
## Params and MACs

| Layer     | Type           | Params     | MACs        | Output Size  |
| --------- | -------------- | ---------- | ----------- | ------------ |
| 1         | Convolution    | 896        | 221184      | (16, 16, 32) |
| 2         | Batch Norm     | 128        | 0           | (16, 16, 32) |
| 3         | Separable Conv | 2400       | 167936      | (8, 8, 64)   |
| 4         | Batch Norm     | 256        | 0           | (8, 8, 64)   |
| 5         | Separable Conv | 8896       | 149504      | (4, 4, 128)  |
| 6         | Batch Norm     | 512        | 0           | (4, 4, 128)  |
| 7         | Separable Conv | 17664      | 280576      | (4, 4, 128)  |
| 8         | Batch Norm     | 512        | 0           | (4, 4, 128)  |
| 9         | Separable Conv | 17664      | 280576      | (4, 4, 128)  |
| 10        | Batch Norm     | 512        | 0           | (4, 4, 128)  |
| 11        | Separable Conv | 17664      | 280576      | (4, 4, 128)  |
| 12        | Batch Norm     | 512        | 0           | (4, 4, 128)  |
| 13        | Separable Conv | 17664      | 280576      | (4, 4, 128)  |
| 14        | Batch Norm     | 512        | 0           | (4, 4, 128)  |
| 15        | Max Pool       | 0          | 0           | (1, 1, 128)  |
| 16        | flatten        | 0          | 0           | (128,)       |
| 17        | Dense          | 16512      | 16384       | (128,)       |
| 18        | Batch Norm     | 512        | 0           | (128,)       |
| 19        | Dense          | 1290       | 1280        | (10,)        |
| **Total** | -              | **104106** | **1678592** | (10,1)       |
## Training Results
![[Pasted image 20250212224901.png]]
With this model's reduced accuracy, it was not able to learn the training data as well as the previous model. As such, its ability to generalize was even worse. While the training accuracy could use more epochs to reach 100%, the validation accuracy already reached its maximum value: a little higher than 50%
# Model 3
## Architecture
![[Pasted image 20250212225109.png]]
This model used skip connections and dropout layers according to the requirements in the assignment requirements
## Training Results
![[Pasted image 20250212225217.png]]
This model had even more parameters than the first model, due to the 1x1 convolution required for the skip connection between layers of unequal dimensions. This should cause the model to suffer from more significant overfit, but the dropout layers and skip connections sufficiently fought the problem of overfit and prevented the model from learning the training data too closely. Its validation accuracy reached well over 70%, while the training accuracy reached 80%. From the curve of the graph, it is clear that the model could have used more epochs for the curves to flatten and reach the optimal solution.

# Comparison 1-3

| Model | Training Accuracy | Validation Accuracy | Time per Epoch | Param Count |
| :---- | :---------------- | :------------------ | :------------- | :---------- |
| 1     | 100%              | 66.22%              | 1.15s          | 704842      |
| 2     | 96.22%            | 53.01%              | 1.12s          | 104106      |
| 3     | 80.14%            | 71.97%              | 1.15           | 706954      |
The models had very similar training time, although the smaller model 2 did have a slightly faster training time. Models 1 and 2 suffered from significant overfit, and certainly won't improve with more training epochs. Model 3 was clearly the best model, which shows how effective dropout and skip connections can be at tackling the problems typically associated with deep, complex models.
# 50k Model
## Architecture
![[Pasted image 20250212225553.png]]
To reach 50k parameters, I first converted all convolutions from Model 3 into depthwise separable convolutions, which reduced the parameter count almost sevenfold.
Next, I set the channel count of each convolutional layer except for the first and last convolutions to 64. This halved the channel count of the final 5 convolutions, and also eliminated the need for the 1x1 convolution to convert dimensions. After this, the parameter count was almost below 50k
Finally, I set the channel count of the final convolution down from 128 to 110, which finally brought the parameter count below 50k

## Training Results
![[Pasted image 20250212225839.png]]
Because of the reduced parameter count, this model didn't suffer from any overfit at all. Its final validation accuracy was a little over 60%, while its training accuracy was just shy of 60%. If the model were given more training epochs, these curves could have flattened to a more optimal solution. 

# NOTE FOR GRADER
I was not able to get the tests working due to issues with conflicting versions of tensorflow and keras. I included comments in the test file as to why I think the tests are failing and why I think they should be succeeding. I hope the graphs and screenshots I included above satisfy the requirements. I also ran my script and piped the output into `hw2_complete.out` if you need to verify even further.

For class #IoT-ML/homework 