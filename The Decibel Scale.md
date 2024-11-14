Continues [[Filter Scaling]]
Continued by [[Bode Blots]]
- ## The dB Scale
	- The ratio of the power  $P$ relative to some reference Power $P_{0}$, such as the output power of an amplifier relative to its source, is called **relative** or **normalized** **power**. 
	- Since $\frac{P}{P_{0}}$ can vary over several orders of magnitude, the dB scale was introduced as a logarithmic conversion tool to facilitate the generation of relative power plots.
	- If $P_{0}$ is set as some fixed reference value, then the dB operator can scale P alone so long as it is expressed in the same units as the reference
- ## The dB Operation
	- If the gain $G$ is defined as $G=\frac{P}{P_{0}}$
		- The corresponding gain in dB is
		- $$G[dB]=10\log\left( \frac{P}{P_{0}} \right)$$
		- ![[Pasted image 20221104140601.png]]
	- If this operation is used for voltage/current rations, then 
		- $$G[dB]=20\log\left( \frac{|V|}{|V_{0}|} \right)$$
		- $$G[dB]=20\log\left( \frac{|I|}{|I_{0}|} \right)$$
- 
- ### EXP: For a series RL circuit
	- Find transfer function $H= \frac{V_{out}}{V_{s}}$ in terms of $\frac{\omega}{\omega_{c}}$ where $\omega_{c}=\frac{R}{L}$
		- $$V_{out}=\frac{j\omega LV_{s}}{R+j\omega L}$$
		- $$H=\frac{j\left( \frac{\omega}{\omega_{c}} \right)}{1+j(\frac{\omega}{\omega_{c}})}$$
	- Determine magnitude $M[dB]=20\log(H)$
		- $M=\frac{\left( \frac{\omega}{\omega_{c}} \right)}{\sqrt{ 1 + (\frac{\omega}{\omega_{c}})^2}}$
		- $M[dB]=20\log(\frac{\left( \frac{\omega}{\omega_{c}} \right)}{\sqrt{ 1 + (\frac{\omega}{\omega_{c}})^2}})$
			- $20\log\left( \frac{\omega}{\omega_{c}} \right)-20\log\left( \left( 1+\left( \frac{\omega}{\omega_{c}}\right)^2 \right)^{1/2} \right)$
		- $$\large M[dB]=20\log\left( \frac{\omega}{\omega_{c}} \right)-10\log\left(1+\left( \frac{\omega}{\omega_{c}} \right)^2\right)$$
	- Determine phase of $H$
		- $$\angle H=90-\tan^{-1}\left( \frac{\omega}{\omega_{c}} \right)$$
	- ![[Pasted image 20221104143308.png|700]]
	- 
	- 


For class #Network-Theory-II 