# Training a Model
- I created a basic 1->50->50->1 neuron MLP model to predict the output of sin(x)
- I trained it for 1000 epochs, and I'll be using it for HLS
```python
import torch
from torch import nn

x = torch.linspace(0, 2 * torch.pi, 100)
y = torch.sin(x)

model = nn.Sequential(
	nn.Linear(1, 50),
	nn.ReLU(),
	nn.Linear(50, 50),
	nn.ReLU(),
	nn.Linear(50, 1)
)

optimizer = torch.optim.Adam(
	model.parameters(), 
	lr=0.01
)
criterion = nn.MSELoss() 

# Train on gpu

if torch.cuda.is_available():
	print("Training on GPU")
	model = model.cuda()
	x = x.unsqueeze(1).cuda()
	y = y.unsqueeze(1).cuda()

	# Training loop

	for epoch in range(1000):
	model.train()
	optimizer.zero_grad()
	output = model(x)

	loss = criterion(output, y)

	loss.backward()
	optimizer.step()

	if epoch % 100 == 0:

print(f'Epoch [{epoch}/1000], Loss: {loss.item():.4f}')

torch.save(model, 'sin_model.pth')
```
# Using HLS4ML
- Following the quickstart I instantly ran into a problem
```python
import torch
import numpy as np
import hls4ml
import matplotlib.pyplot as plt

model = torch.load('sin_model.pth', weights_only=False)
model = model.cpu()
  
cfg = hls4ml.utils.config_from_pytorch_model(
	model = model
)
```

```
Exception has occurred: TypeError

config_from_pytorch_model() missing 1 required positional argument: 'input_shape'

File "/home/jaskin/projects/hls4ml/sin_hls.py", line 8, in <module> model=model, ) ^^^^^^^^^^^^^ TypeError: config_from_pytorch_model() missing 1 required positional argument: 'input_shape'
```
- The quickstart doesn't mention that you need to specify input shape, but that was a pretty simple fix.
```python
cfg = hls4ml.utils.config_from_pytorch_model(
	model=model,
	input_shape=(1,),
)
hls_model = hls4ml.converters.convert_from_pytorch_model(
	model = model,
	hls_config=cfg,
	backend='Vitis',
	board='pynq-z2',
)
```
- After that, I ran into another problem. I specified that I was synthesizing for the pynq-z2 but the tcl script it generated ran into this error:
```
INFO: [HLS 200-1510] Running: set_part xcvu13p-flga2577-2-e 
ERROR: [HLS 200-1023] Part 'xcvu13p-flga2577-2-e' is not installed.
```
- It seems like the part has to be manually specified, and specifying the board doesn't do anything for some reason.
```python
hls_model = hls4ml.converters.convert_from_pytorch_model(
	model = model,
	hls_config=cfg,
	backend='Vitis',
	board='pynq-z2',
	part = 'xc7z020clg400-1'
)

hls_model.compile()
```
- Once I ran this, it completed the RTL synthesis. I also ran simulated inference using `hls_model.predict()` and compared it against inference done with pytorch:
![[Pasted image 20250715192833.png]]
![[Pasted image 20250715192842.png]]
- It also generated this hls report![[Pasted image 20250715193412.png]]

# Next Steps
- Generate a bitstream and test this functionality on the Z2

For topic #thesis/hls4ml