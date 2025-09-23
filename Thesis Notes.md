# PYNQ for cards like V80
- Porting PYNQ to the V80 doesn't make sense
- Linux OS running on ps of V80 running within host OS? 
- Earlier versions of PYNQ for Alveo had the jupyter notebook and overlay logic running on the host CPU, and the PYNQ library was an abstraction to the Alveo's PL.
- Seems for alveo cards, the new approach is the XRT
- XRT supposedly has python bindings but they were removed in 2022.2
	- https://xilinx.github.io/XRT/2022.1/html/pyxrt.html
	- https://xilinx.github.io/XRT/2022.2/html/pyxrt.html
		- This page is empty
- Does this still work? What's going on here?