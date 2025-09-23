# Complexity Analysis
## Dense
- Params:
	- $\text{OUT} \times (\text{IN} +1)$
		- Remove +1 if no bias
- MACS = Params
- SRAM = max sum of two connected layers
## Conv
- Params
	- $k^{2}* C_{in} * C_{out}$
- MACs
	- $k^{2}\times C_{in} \times D_{out}$