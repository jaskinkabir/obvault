Continues [[Parallel Programming]]
# True Dependence
- Read after write (RAW)
- Producer-consumer
- ![[Pasted image 20260210195707.png]]
- S1 comes before S2 in program order, S1 stores value that is read by S2
- Notation
	- S1 imposes true dependence on S2
	- $S_{1} \to^{T}S_{2}$
	- $S_{1} \to^{T}S_{3}$
	- T is for true
# Anti-Dependence
- Write after read (WAR)
- ![[Pasted image 20260210195949.png]]
- S3 comes before S4, S3 reads a value written by S4
- $S_{3}\to^{A}S_{4}$
# Output Dependence
- Write after write (WAW)
- ![[Pasted image 20260210200101.png]]
- S2 before S3, S2 writes value written by S3
- $S_{2} \to^{O}S_{3}$
# Loop-Carried Dependence
![[Pasted image 20260210200253.png]]
- A true dependence between loop iterations
- A dependence always moves forward in time.
# Dependence Visualization
![[Pasted image 20260210201009.png]]
## Iteration Traversal Graph (ITG)
- Shows how program flow moves through iterations

# Loop-Carried Dependence Graph (LDG)
- Shows how dependencies move through iterations and across which dimension
- In the above example, dependence is carried across the j dimension
- It would be best to partition parallelism across the i dimension
- Matmul:![[Pasted image 20260212135926.png]]
For class #parallel-arch