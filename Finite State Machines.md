
Continues [[Sequential Circuit Memory]]
- Comically large button toggles lamp on and off
	- If lamp is on button turns it off
	- If lamp is off button turns it on
L_Current|Button|L_Next
-|-|-
0|0|0
0|1|1
1|0|1
1|1|0

- Can be implemented with combinational logic
	- ![[Pasted image 20221028114037.png|250]]
	- This is forbidden. Combinational logic cannot feed its output back into it's output because it will have unexpected behavior as the output propagates through the inputs and cycles the circuit.
- Add a D-flip-flop to gatekeep the input with the clock
	- ![[Pasted image 20221028114356.png|350]]
	- Proper notation for this is to replace the L variable with s and s' for state and state prime (next state)
	- The beginning combinational logic circuit is called **Next State Logic**
		- After the memory module there may be some **Current State Logic (or Output Logic)** to determine the proper output
S|B|S'|O
-|-|-|-
0|0|0|0
0|1|1|1
1|0|1|1
1|1|0|0
- ## State Diagram
	- ![[Pasted image 20221028114917.png|350]]
	- Captures the behavior of the circuit
		- Transitions between states occur on the clock edge
	- The arrows are defined by the Next State Logic
	- The variable S is some arbitrary encoding of the states of the circuit
		- If the on state is encoded as S0, then an inverter can be placed in the **Output/Current State Logic** to achieve this behavior
	- Must have an entry point to define intitial state
- ## Trash Incinerator Example
	- I/O
		- S input: senses user and opens can
		- M output: turns on the motor to open the can
		- F: Turns on the flame to burn the trash
	- State Diagram
		- ![[Pasted image 20221107112618.png]]
	- Truth Tables
		- #### INPUT:
			- ![[Pasted image 20221107113131.png|300]]
		- #### OUTPUT:
			- ![[Pasted image 20221107113156.png|250]]
	- #### Boolean:
		- $\large s_{1}'=s_{0}\overline{s}$
		- $\large s_{0}'=\overline{s_{1}}s$
		- $m=s_{0}$
		- $f=s_{1}$
	- #### Circuit:
		- ![[Pasted image 20221107114034.png|350]]
	- #### Timing Diagram:
		- ![[Pasted image 20221107114655.png]]
- ## Moore Machine
	- The above example is a **Moore Machine**
	- #### The outputs are purely based on the current state of the machine
- ## Mealy Machine
	- #### The outputs are based on state as well as the inputs
	- More reactive, but can be glitchy because of prop delays
- ## Trash Can Mealy Machine
	- ![[Pasted image 20221107115938.png]]
		- The outputs must be included with the state transitions
	- ![[Pasted image 20221107115945.png|400]]
	- ![[Pasted image 20221107115956.png]]
		- M changes instantly with s instead of waiting for the clock signal



For class #Logic-Systems-1 