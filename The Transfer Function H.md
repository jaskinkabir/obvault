Continues [[Phasors in Active Circuit Analysis]]
Continued by [[AC Filters]]
- ## For some AC RC Circuit
	- Voltage source $V\angle\phi_{v}$
	- Magnitude of current is given by
		- $$|I| = |V| \frac{|j\omega C|}{|1+j\omega RC|}$$
		- As $\omega \to \infty$, $|I| \to \frac{|V|}{R}$
			- Approaches a DC circuit with no capacitor
		- At $\omega=\frac{1}{RC}$, $|I|=\frac{|V|}{R\sqrt{ 2 }}$
	- Graph of I and omega
		- ![[Pasted image 20221024124433.png]]
- ## The Transfer Function H
	- Defined as $$H(j\omega) = \frac{Output(j\omega)}{Input(j\omega)}$$
	- Can tell us about how an output responds to its input
		- Specifically what is transferred from in to out
	- Multiplying H by its input results in its output
		- Can convert a circuit into its equivalent mathematical function
	- For an RC circuit with a current source, the H function can be used to define the impedance of the network
		- $H(j\omega) = \frac{V_{C}}{I_{s}} = Z_{eq}$
	- For the circuit above, the output current can be found with the transfer function: $$H(j\omega) = \frac{1}{Z_{eq}} = \frac{1}{R-\frac{j}{\omega C}}$$
		- Which means: $$I = V_{s}H(j\omega)$$
		  
	- ### H(w) is a complex quantity, so it has magnitude (gain) and phase
		- $$H(\omega) = M(\omega)e^{ j\angle\phi(\omega) }$$
			- $M(\omega)=|H(\omega)|$
	

For class #Network-Theory-II 