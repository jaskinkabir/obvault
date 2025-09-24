# Definition
- Transform the data in some way to artificially create more samples
- These transformations must be similar to what could happen to real data
# For Images
- Translation
- Random scaling
- Random noise
- Flipping left-right
	- Vertical maybe
- Random rotation
- Vary hue, brightness
- Key: Transformations should mimic real world!!!
# For Audio
- Vary speed
- Shift pitch
- Add noise
	- Instead of random (Gaussian) noise, add recorded background noise
- We can also generate synthetic data based on a model of the problem
	- Example
	- We know the input dataset only contains frequencies between 8-12hz
	- "Augment" samples by randomly generating sine waves between these frequencies
- 

For class #IoT-ML