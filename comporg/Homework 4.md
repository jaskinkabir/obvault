Jaskin Kabir 801186717
# Q1 
![[Pasted image 20241111215351.png]]
1. i
	1. Non-Pipeline
		1. $250+350+150+300+200=1250ps$
	2. Pipeline
		1. max = $350ps$
2. ii
	1. Non-Pipeline
		1. Same as any other instruction, $1250ps$
	2. Pipeline
		1. $\text{\# of stages} \times \text{Cycle Time}=5\times 350 = 1750ps$
3. iii
	1. Split instruction decode because it is the slowest stage
	2. New cycle time is $300ps$
4. iv
	1. LDUR + STUR = $20+15=35\%$
5. v
	1. LDUR + ALU = $20 + 45 = 65\%$
# Q2
![[Pasted image 20241111220006.png]]
i. ![[Pasted image 20241111223157.png]]
ii. 
```c
ADD X5, X2, X1   
LDUR X2, [X2, #0]
NOP
LDUR X3, [X5, #4]
NOP
NOP
ORR X3, X5, X3
STUR X3, [X5, #0]
```
- Reordering the two loads is all that can be done, and it only removes one NOP
- There are no antidependencies, X7 cannot be used to prevent stalls
iii. 
```c
ADD X5, X2, X1   
LDUR X3, [X5, #4]
LDUR X2, [X2, #0]
ORR X3, X5, X3
STUR X3, [X5, #0]
```
![[Pasted image 20241111223411.png]]
![[Pasted image 20241111225608.png]]
# Q3
![[Pasted image 20241111224705.png]]
![[Pasted image 20241111224712.png]]
## 3a. 
```c
ADD X5, X2, X1   
NOP
NOP
LDUR X3, [X5, #4]
LDUR X2, [X2, #0]
NOP
ORR X3, X5, X3
STUR X3, [X5, #0]
```
- This is the same code from the last question, nothing has changed
## 3b. 
- Nothing would happen, the program would execute as expected.  There are no load-use hazards that would be detected by the hazard detector. However, if the order of the load instructions were reversed, there would be a hazard where the old value of X3 would be used in the ORR instruction rather than the value that should have been pulled from memory
## 3c.
![[Pasted image 20241111225608.png]]
Again this is the same code, so nothing has changed.
However, if the load instructions were reversed, the IF/IDWrite, PCWrite, and ID.Flush values would be inverted during clock cycle 5 to initiate a stall.
# Q4
![[Pasted image 20241111230206.png]]
![[Pasted image 20241111230528.png]]
## 4I
- Always taken predictor has 45% accuracy
- 55% of conditional branches with the Always-taken predictor result in an additional cycle to flush the pipeline
- Thus, $0.55 * 0.25 = 13.75\%$ of instructions take 6 cycles to execute instead of 5
- New CPI = $(5 * (1-0.1375) + 6 * 0.1375  =5.1375$ CPI
## 4II
- $0.45 * 0.25 = 11.25\%$ 
- New CPI = $(5 * (1-0.1125) + 6 * 0.1125  =5.1375$ CPI
## 4III
- $0.15 * 0.25 = 3.75\%$ Increase in CPI
- New CPI = $(5 * (1-0.0375) + 6 * 0.0375  =5.0375$ CPI
## 4IV
- CPI Increase = $0.15 * 0.25 * 0.5 = 1.875\%$
- New CPI = $(5 * (1-0.01875) + 6 * 0.01875  =5.01875$ CPI
- Speedup = $\frac{5.0375}{5.01875}=1.0037$
## 4V
- Percent of branch instructions = 25%
	- Percent of 5 cycle branches = 12.5* 0.85
	- Percent of 6 cycle branches = 12.5* 0.15
	- Percent of 10 cycle branches = 12.5
- CPI Increase = $0.15 * 0.25 * 0.5 = 1.875\%$
- New CPI = $5 * (0.75 + 0.125* 0.85) + 6*0.15 * 0.125 + 10*.125=5.64375$ CPI
- Speedup = $\frac{5.0375}{5.64375}=0.893$
## 4VI
- Accuracy = $0.8 * 1 + 0.2*0.85 = 0.97$
# Q5
![[Pasted image 20241111234022.png]]
## 5i
- Always Taken: $\frac{3}{5}=60\%$ Accuracy
- Always Not Taken: $\frac{2}{5}=40\%$ Accuracy
## 5ii
- ![[Pasted image 20241111235336.png]]
- $\frac{1}{4}=25\%$ Accuracy
# 5iii
- ![[Pasted image 20241111235516.png]]
- After the initial 4 predictions, the 2-bit predictor becomes an Always-Taken predictor
- As the number of predictions approaches infinity, these 4 initial predictions become irrelevant
- Accuracy = 60%


For class #comporg