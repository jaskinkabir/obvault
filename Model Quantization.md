# Scale and Offset
- TF uses scale and zero point to quantize
	- $val_{q}=\text{int}\left( \frac{\text{val}_{fp}}{\text{scale}}+\text{zero pt} \right)$
- Calibrating quantization requires a representative sample of values
## Enforcing zero center
- Consider the following expansion
	- $y=wx$
	- $y_{q}=w_{q}+x_{q}$
	- $=\left( \frac{w}{s_{w}}+z_{w} \right)\left( \frac{x}{s_{x}}+z_{x} \right)$
	- $=\frac{xw}{s_{w}s_{x}}+\frac{wz_{x}}{s_{w}}+\frac{xz_{w}}{s_{x}}+z_{w}z_{x}$
- If we assume the data and parameters are centered around zero, all terms except for the first one cancel
	- $y=wx=\frac{wx}{s_{w}s_{x}}$
# Dequantization
- Reconstructing the original value simply subtracts the zero point and multiplies the scale factor
# Quantization Aware Training
- Training the model in the floating point domain and then quantizing the parameters results in an inaccurate representation of the model
- By quantizing activations on the forward pass during training, the model learns from quantized data