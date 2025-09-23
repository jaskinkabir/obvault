# Introduction

# Model Architecture
For image classification on embedded hardware, the most widely used paradigm is the convolutional neural network, which was used in this project. As for the structure of the network itself, a choice was made between a wide and short network or a narrow and deep network. A wide and short network would have few convolutional layers with each layer consisting of many convolutional filters, whereas the deep and narrow network would have many layers with fewer filters in each layer. To allow for the greatest abstraction from the input images, the narrow and deep network was chosen. To resolve the issue of vanishing gradients, skip connections were added between every two convolutional layers after the initial layer. 

