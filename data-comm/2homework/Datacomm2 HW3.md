Jaskin Kabir 801186717
Uses
[[Routing in Packet-Switching Networks]]
[[IPv4]]
[[IPv6]]
1. Consider the following network. With the indicated link costs, use Dijkstra’s least cost  algorithm to compute the least cost path from x to all other network nodes. Show how the algorithm works by filling in the table below.
	1. ![[Pasted image 20251003124328.png]]

| Iteration | T                        | L(z), Path     | L(y), Path | L(w), Path | L(v), Path | L(u), Path | L(t), Path   | L(s), Path     |
| --------- | ------------------------ | -------------- | ---------- | ---------- | ---------- | ---------- | ------------ | -------------- |
| 1         | {x}                      | ∞              | 6, x–y     | 1, x–w     | 3, x–v     | ∞          | ∞            | ∞              |
| 2         | {x, w}                   | ∞              | 6, x–y     | 1, x–w     | 2, x–w–v   | 4, x–w–u   | ∞            | ∞              |
| 3         | {x, w, v}                | ∞              | 3, x–w–v–y | 1, x–w     | 2, x–w–v   | 3, x–w–v–u | 11, x–w–v–t  | ∞              |
| 4         | {x, w, v, y}             | 17, x–w–v–y–z  | 3, x–w–v–y | 1, x–w     | 2, x–w–v   | 3, x–w–v–u | 10, x–y–t    | 7, x–w–v–u–s   |
| 5         | {x, w, v, y, u}          | 17, x–w–v–y–z  | 3, x–w–v–y | 1, x–w     | 2, x–w–v   | 3, x–w–v–u | 5, x–w–v–u–t | 7, x–w–v–u–s   |
| 6         | {x, w, v, y, u, t}       | 7, x–w–v–u–t–z | 3, x–w–v–y | 1, x–w     | 2, x–w–v   | 3, x–w–v–u | 5, x–w–v–u–t | 6, x–w–v–u–t–s |
| 7         | {x, w, v, y, u, t, s}    | 7, x–w–v–u–t–z | 3, x–w–v–y | 1, x–w     | 2, x–w–v   | 3, x–w–v–u | 5, x–w–v–u–t | 6, x–w–v–u–t–s |
| 8         | {x, w, v, y, u, t, s, z} | 7, x–w–v–u–t–z | 3, x–w–v–y | 1, x–w     | 2, x–w–v   | 3, x–w–v–u | 5, x–w–v–u–t | 6, x–w–v–u–t–s |
2. Repeat for Bellman-Ford

| Iteration | L(z), Path     | L(y), Path | L(w), Path | L(v), Path | L(u), Path | L(t), Path   | L(s), Path     |
| --------- | -------------- | ---------- | ---------- | ---------- | ---------- | ------------ | -------------- |
| 0 (init)  | ∞              | ∞          | ∞          | ∞          | ∞          | ∞            | ∞              |
| 1         | ∞              | 6, x–y     | 1, x–w     | 3, x–v     | ∞          | ∞            | ∞              |
| 2         | ∞              | 3, x–w–v–y | 1, x–w     | 2, x–w–v   | 4, x–w–u   | 11, x–w–v–t  | ∞              |
| 3         | 17, x–w–v–y–z  | 3, x–w–v–y | 1, x–w     | 2, x–w–v   | 3, x–w–v–u | 5, x–w–v–u–t | 7, x–w–v–u–s   |
| 4         | 7, x–w–v–u–t–z | 3, x–w–v–y | 1, x–w     | 2, x–w–v   | 3, x–w–v–u | 5, x–w–v–u–t | 6, x–w–v–u–t–s |
| 5         | 7, x–w–v–u–t–z | 3, x–w–v–y | 1, x–w     | 2, x–w–v   | 3, x–w–v–u | 5, x–w–v–u–t | 6, x–w–v–u–t–s |
| 6         | 7, x–w–v–u–t–z | 3, x–w–v–y | 1, x–w     | 2, x–w–v   | 3, x–w–v–u | 5, x–w–v–u–t | 6, x–w–v–u–t–s |
| 7         | 7, x–w–v–u–t–z | 3, x–w–v–y | 1, x–w     | 2, x–w–v   | 3, x–w–v–u | 5, x–w–v–u–t | 6, x–w–v–u–t–s |


1. The centralized least-cost routing table for a network of 6 nodes with asymmetrical links is given below:
	1. ![[Pasted image 20251003134509.png]]
	2. Least cost route from 2 to 6?
		1. 2-4-5-6
	3. 3 to 1?
		1. 3-5-4-2-1
2. Given “65.51.240.1”: 
	1. What is the address class? [2]  
		1. **Class A** , less than 128
	2. What is the network address? [2]  
		1. 7 bits for network
		2. Network address is 65
	3. What is the host address of this host? Assume sub-networking is not used. [2]  
		1. **Host address is 51.240.1**
	4. Now assume 4 bits are used for subnets. What is the subnet address? What is the host address? [2]
		1. Convert IP to binary
			1. 01000001 00110011 11110000 00000001
		2. Subnet mask 255.240.0.0
			1. 11111111 11110000 00000000 00000000 & 
			2. 01000001 00110011 11110000 00000001 =
			3. 01000001 00110000 00000000 00000000
			4. Underlined portion is subnet addr, rest host number
			5. <u>01000001 0011</u>0011 11110000 00000001
		3. Address is in **Subnet No. 3**
		4. **Subnet address is 65.48.0.0**
		5. Host portion is **3.240.1**
		6.  (Host number 258049)
3. Suppose an IP packet with the following property will be forwarded to another network where the maximum total packet size is only 228 bytes. Show (a) Total length, (b) Fragment offset, and (c) More fields in the second and last packets after fragmentation. Assume IHL =  5 for every packet.
	1. Total Length = 740
	2. IHL = 5
	3. Fragment Offset = 0
	4. More = 0
- Length of data is 740-20 = 720 bytes
- Max total packet size = 228, max data size per packet = 208
- 720 / 208 = 3r96 (4 total packets)
- **Second Packet**
	- **Total length = 228**
	- **Fragment offset = 26**
	- **More = 1**
- **Last packet**
	- **Total length = 116**
	- **Fragment offset = 78**
	- **More = 0**
4. The protocol field used in the IPv4 header is not present in the mandatory IPv6 header. Why not? [5]
- The protocol field is not needed in the IPv6 protocol because its function is replaced by the Next Header Field. This field can either specify an upper-layer protocol or an extension header, which allows IPv6 to be more extensible. This also means that intermediate routers don't need to waste time reading information about what the next layer on the destination host machine will be.

For class #data-comm/2homework