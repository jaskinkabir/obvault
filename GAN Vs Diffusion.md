# GAN
## Basic Intuition
![[Pasted image 20250422090558.png]]
- Two models (adversaries) competing with one another
- Generator generates images, discriminator learns to discriminate between real and fake images
- Loss going to discriminator is from whether the image is fake.
- Loss for generator is whether image was correctly discriminated
## Upsides
- Good for resource constrained inference
## Downsides
- Feedback structure has failure modes that can make training difficult
	- Generator can learn to exactly copy the input
- Discriminator must be good until it can provide useful feedback to the generator
- The progress of one model depends on the progress of the other
- Therefore they are much harder to train
# Diffusion
## Intuition
- Physical Diffusion: Random particles tend towards an unordered even distribution
- Diffusion generative models:
	- Train a model to de-noise a noisy image using progressively noisier images
	- Eventually can start from pure noise
- Cannot go from pure noise to clean image in one step
- Alignment/edge uncertainty ⇾ optimal guess a blurry image
- Solution is to de-noise in multiple steps
## Downside
- Very slow and unparallelizable due to the multistep nature
- GANs don't have to iterate and are faster at inference time
# Grouped Convolution
- Intermediate between depthwise and full convolution
- Depthwise has each output channel dependent on exactly one input channel
- Full has each output channel dependent on every input channel
- Grouped conv has groups of output channels dependent on different groups of input channels
- Can dramatically reduce number of weights
- Number of input/output channels must evenly divide by number of groups
- Typical to have stages of grouping followed by stages of full convolutions to ensure all input features have a chance to influence all output features