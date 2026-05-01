Continues [[Directory Coherence Ordering and Correctness]]
# Virtualization
- ![[Pasted image 20260428173206.png]]
- ![[Pasted image 20260428173240.png]]
- Not exploiting locality because the processor has to send requests all the way to the directory to get data that is right next to it
- Not providing isolation because all VMs request data from the same directory
# Dynamic Home Node
- Each tile holds a table that maps blocks to a home tile within the partition
- Set by hypervisor (OS) on VM 
- ![[Pasted image 20260428173552.png]]
## Two-Level Directory Scheme
![[Pasted image 20260428173634.png]]

For class #parallel-arch