Continues [[params]]
# CNN Complexity
- Params = $D_{out}(W_{F}H_{F}D_{in}+1)$
	- This is for a single layer
- MACs: Each output pixel is computed from $D_{in}W_{F}H_{F}$ pixels
	- $D_{in}W_{F}H_{F}$ MACs per pixel per output channel
	- MACS = $D_{IN}W_{F}H_{F}D_{OUT}W_{OUT}H_{OUT}$
- Example
	- Input: 128x128x8, Filter = 5x5x8x32, padding = valid
- Params = $32(5*5*8+1)=6432$
- MACs = $5*5*8$ per pixel
	- = $32*5*5*8*32*124*124$
	- Lose 2 pixels per side for valid padding $\frac{k-1}{2}$
## Required Parameters
- Kernel size + 1 for bias
## Required MACs
- 
# Dilated Convolution
- Subsampling input spacce
- Cover more input space with same # weights
- Can dilate by any integer factor
- Increases padding needed for 'same'
# Striding
- Subsampling in the output space
- Reduces output size by skipping over certain centering locations of the filter
$(3*3*128)*()$

# Depthwise Seperable Convolutions
## Depthwise
- Typically, a convolution will have $D_{out}$ filters that are each $W_{F} \times H_{F} \times D_{in}$ in dimension
- A depth wise convolution has $D_{out} = D_{in}$, such that it has $D_{out}$ filters that are each $W_{f} \times H_{F}$ in dimension.
- Each kernel only operates on a single feature map
- Its parameter count is thus $D_{out}*(W_{F}*H_{F}+1)$
	- A normal convolution has $D_{out}*(D_{in}*W_{F}*H_{F}+1)$
	- Significantly fewer parameters
- MAC Count is $W_{F}*H_{F}$ per pixel
	- A convolutional layer has $D_{in}W_{F}H_{F}$
## Seperable (1x1)
- A 1x1 convolution has $D_{out}$ filters that are each $D_{in} \times 1 \times 1$ in dimensionality
- Has $D_{out}(D_{in}+1)$ parameters
- Finds co-occuring patterns in different input maps
## Depthwise Seperable
- Combines the two
- A DW layer whose output depth is the same as the input
- A 1x1 cnv layer whose output dimensions are equal to the desired output dimensions

## Counting Params
- Params of DW = $D_{in}*(W_{F}*H_{F})$
- Params of 1x1 = $D_{out}(D_{in}+1)$
- Together $\#P=D_{in}*(W_{F}*H_{F})+D_{out}(D_{in})$
## Counting MACs
- MACs of DW = $W_{F}H_{F}$ per output pixel
- MACs of 1x1 = $D_{in}$ MACs per output pixel
- Together $$\frac{\text{\#MACs}}{\text{Out Pixel}}=D_{in}+W_{F}H_{F}$$