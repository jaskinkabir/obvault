Relates [[Transistors (LOGIC)]]
Continued by [[Operational Amplifiers]]
- ## Classifying Resistivity
	- Conductors: $\rho=10^{-8}-10^{-4} \frac{\Omega}{cm}$
	- Semiconductors: $\rho=10^{-4}-10^{8}\frac{\Omega}{cm}$
	- Insulators $\rho=10^{8}-10^{18}\frac{\Omega}{cm}$
	- ### Manipulating semiconductor resistivity
		- Doping
			- $\rho=f(N_{d})$
		- Optical excitation 
			- $\rho \downarrow$
		- Change in temperature
			- $\rho\space\alpha \exp\left( \frac{E_{g}}{2kT} \right)$
		- 
- ## Classifying semiconductors based on chemical content
	- Elemental classification: Si, Ge, Diamond
	- Compounds:
		- Organized in groups
			- Group III-V:
				- Binary: $GaAs, AlAs, InSb, InAs, GaN, AlN, InN$etc...
				- Ternary: $Ga_{x}Al_{1-x}As,Ga_{x}In_{{x-1}}, etc$
				- Quaternary: $Ga_{x}Al_{{1-x}}As_{y}P_{1-y}$
			- Group II-VI:
				-  $ZnS, ZnSe, CdS, CdSe, ZnTe, CdTe$
	- ### LEDs:
		- Blue/Green LED: Gallium Nitride $GaN$
		- Red LED: Indium Gallium Phosphide $InGaP$
- ## The Lattice Constant
	- Create silicon lattice with 6 people for extra credit
	- A measurement proportional to the distance between atoms in a crystal lattice
		- Represented by symbol $\dot{A}$
	- A simple cubic crystal has just one lattice constant, the distance between atoms
	- In more complex three-dimensional lattices have six lattice constants: 
		- The lengths _a_, _b_, and _c_ of the three cell edges meeting at a vertex, 
			- Measured in Angstroms ($\dot{A}$=0.1 nm) and define the size of the unit cell
				- The distance from a given atom to an identical atom in the same position and orientation in a neighboring cell
		- The angles _α_, _β_, and _γ_ between those edges.
			- Measured in degrees
- ## The Band-gap
	- The amount of energy required to promote a bound valence electron to a conductive electron; one that can move and be harnessed as electrical energy
		- This gap is the range of energy in which no electronic states can exist
		- Measured in electron-Volts (eV)
	- Substances with large band gaps are generally insulators
	- Semiconductors have smaller band gaps
	-  Conductors either have very small band gaps or none, because the valence and conduction bands overlap to form a continuous band.
	- ### Relation to LEDs:
		- The range of energy of the band-gap determines the wavelength of light that is emitted
			- From the relation between the energy of a photon and its wavelength, we can determine that the wavelength of any photon emitted through an electron moving across the band gap must be equal to the wavelength that would correspond to the band gap of energy 

- 
- 
## Types of Semiconductor Configurations
- a
	- ### Intrinsic Semiconductors
		- No doping, no impurities, pure semiconductors
		- at 0K, no free charge carriers. Electrons are accommodated in the valence band and the conduction band is empty
		- At higher temperature, the electrons are thermally excited across the band-gap, leaving a hole behind 
			- (electron hole pair produced)
			- In metals this effect is reversed
		- Thus
			- $n=p=n_{1}=$ intrinsic concentration
		- Due to the uneven distribution of heat, there will be a gaussian distribution across the lattice, and only some of the electrons will have the energy to break free into the conduction band
	- ### Extrinsic Semiconductors
		- Doped and impure
		- ### N and P Type
			- Adding a group 5 element will add an extra electron to the lattice and create an n-type lattice
				- Arsenic
			- Adding a group 3 element will create p-type by the opposite mechanism
				- Boron
			- N-type: Electrons are majority, holes are minoritiy carriers
			- P-Type: Electrons are minority, holes are majority carriers
For class #Electronics-Semiconductors 