Related to [[Adders, Subtractors, and the ALU]]
Continued by [[Binary Integer Division]]
# Multiplication
## Sequential Long Multiplication
- The multiplier is 64 bits, multiplicand, product register, and ALU are 128 bits
- Process: For 64 clock cycles: (or $n$ cycles)
	- Shift the multiplier right and pass the output bit to the controller
	- Shift the multiplicand left
	- If the controller received a 1 from the multiplier, add this shifted multiplicand to the product
	- Otherwise, skip the add operation
## Optimized Multiplier
- 64 bit multiplicand and ALU, 128 bit product
# Division


For class #comporg
