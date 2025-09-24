Continues [[Sequential Circuit Memory]]
- # Latches have a power up sequence
- At startup, all inputs are zeros, so both outputs will be 1, and the cross-coupling will cause an infinite flicker between output states
	- Because of manufacturing tolerances, one NOR gate will be slower than the other, and so Q will eventually settle on 0
	- This means the output values on startup will be random, which needs to be accounted for
- ## Comparing level and edge based latching
	- If an input data line changes value mid-clock cycle, a level based module will change its output, whereas an edge based circuit will stay latched to the initial data input
- # How to Achieve Edge Sensitivity
	- You can 'gatekeep' a level sensitive circuit with another level sensitive circuit
	- ### In the case of the Chained D-Latch
		- ![[Pasted image 20221024115156.png]]
		- If the first dataline switches value while the clock signal is high, the first D-latch isn't listening to that dataline anymore, and so the second D-Latch doesn't see the change in the dataline at all. If there is a change in dataline while the clock is low, the second D-Latch isn't listening to its input anymore, and so no change is observed in the output
		- Chaining D-Latches in this way makes sure the output only changes on the edge of the clock signal
For class #Logic-Systems-1 
 