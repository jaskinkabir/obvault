Related to [[Three Y's]]
- VHSIC Hardware Description Language
	- Very High Speed Integrated Circuit
- Language used to describe digital electronic systems
- Similar to C where the system's inputs and outputs are declared first, and its implementation is written separately
- Implementing a system in VHDL:
	- A motion detecting light must turn on when motion is detected and light is not detected
		- F = Light state
		- A = Motion Dector
		- B = Light Detector
		- F <= A AND NOT B
```vhdl
entity MotionLight is
	Port {
		a : in bit;
		b : in bit;
		f : out bit;
	}
end MotionLight

architecture Structual of MotionLight is
begin
	F <= a AND NOT b;
end Structural
	
```

- ## FPGA
	- Field Programmable Gate Array
	- Can implement a written VHDL circuit in hardware

For class #Logic-Systems-1 