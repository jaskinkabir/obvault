Continues [[Combinational Logic Representations]]
Continued by [[Sequential Circuit Memory]]
- Shows the values of inputs and outputs as square waves over time
- Consider f = ab + a'b' 
	- (f := (a == b)
- ![[Pasted image 20221012112645.png]] 
	- Each gate involved in the circuit will have some propogation delay from when the inputs change to the change in output
- ### **Total Propogation Delay**
	- Most of the time only consider the **Critical Path**
		- The path where there is the most propogation delay (the most gates)
	- Strange behavior can occur when propogation time is not considered
	- For F=A'B' + BC
	- ![[Pasted image 20221012114227.png]]
	- As B changes to 0, there are 2 different propogation delays for each input of the or gate
		- There is a temporary, unintended, flicker of the output f during this time.
	- Critical pd = tpd_NOT + tpd_AND + tpd_OR
	- To account for the glitch, the circuit should be run at a frequency of < 1/tpd

For class #Logic-Systems-1 