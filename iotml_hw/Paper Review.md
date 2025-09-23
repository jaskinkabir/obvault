Jaskin Kabir
jkabir@charlotte.edu
# Paper Title 
**DEEPTRACK: LIGHTWEIGHT DEEP LEARNING FOR VEHICLE TRAJECTORY PREDICTION IN HIGHWAYS**
# Author(s)
Vinit Katariya
Mohammadreza Baharani
Nichole Morris
Omidreza Shoghli
Hamed Tabkhi

# Affiliation(s)
Vinit Katariya : Department of Electrical and Computer Engineering, University of North Carolina at Charlotte

Mohammadreza Baharani : Department of Electrical and Computer Engineering, University of North Carolina at Charlotte

Nichole Morris : Department of Mechanical Engineering, University of Minnesota

Omidreza Shoghli : Department of Engineering Technology and Construction Management, University of North Carolina at Charlotte

Hamed Tabkhi : Department of Electrical and Computer Engineering, University of North Carolina at Charlotte

# Venue & Year
IEEE Transactions on Intelligent Transportation Systems 2022
# Link
https://arxiv.org/abs/2108.00505

# Problem/Purpose Description
Vehicle trajectory prediction is a challenging problem, especially in real-time, as this complex problem demands large, complex, high latency models that are not typically suitable for real-time applications. However, it is nevertheless an important one. Among many other applications, when implemented properly, it can be leveraged to ease traffic congestion and alert emergency responders and road maintenance workers of incoming distracted drivers. In this paper, the authors discuss their solution to the problem of developing a lightweight, low-latency vehicle trajectory prediction model suitable for deployment at the edge.
# Main Innovation
The mainstream LSTM-based approach to trajectory prediction suffers due to the sequential nature of the LSTM architecture. It is difficult to parallelize, even during the forward pass. DeepTrack, however, uses a Temporal Convolutional Network as its backbone, which shrinks the size and compute demands of the model. This complexity is reduced even further by their choice to use depthwise convolutions, which reduce the number of parameters and MAC operations in each convolution compared to standard convolutions. Additionally, they use time-attention modules to improve accuracy with little computational overhead. These improvements in model complexity lead to lower inference latency, which is crucial in real-time applications. The speedup between DeepTrack and the traditional LSTM could be the difference between a life-threatening crash and a near-miss.
# How was the effectiveness of the method evaluated?
The Federal Highway Administration provides datasets under their Next Generation Simulation program. The DeepTrack model was compared head-to-head against the top of the line CS-LSTM model on this same dataset

# Describe the experimental results presented
They present 7 different versions of their DeepTrack model with varying levels of complexity. They then present their best version compared against the CS-LSTM, CF-LSTM, SAAMP, and STA-LSTM models. The STA-LSTM model outperforms DeepTrack in terms of final displacement error, but the gap between in MACs and Parameters is substantial. DeepTrack is much less complex, while not falling too far behind in prediction accuracy.
# How was the clarity of explanations?
The authors explained themselves very well. The underlying architecture of their model was easy to understand, as well as the reasoning behind each of their decisions. I especially appreciated the qualitative results they presented with certain cases where their model performed well and others where it did not. 
# What questions do you have for the authors?
If you were to redo this project, what would you do differently? Were you satisfied with the data you collected? Would you use a different paradigm like the newer RWKV architecture?
# Does the result seem useful?
I would say this result seems very useful. DeepTrack presented a novel method of providing potentially lifesaving technology with lower latency achievable with less computational load compared to other models. 