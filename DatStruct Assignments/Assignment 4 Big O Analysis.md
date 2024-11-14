Jaskin Kabir 801186717
Uses [[Big-O Analysis of Recursive Algorithms]]
Related to [[Big O Notation]]
## Q1. For each of the following 6 program fragments, give a Big-Oh analysis of the running time  
(3 points) -  
### 1. 
```cpp
sum = 0;  
for ( i = 0 ; i < n ; i++ )  
	++sum;  
```
Ans: Loops over $n$ iterations, algorithm is $O(n)$

### 2.
```cpp
sum = 0 ;  
for( i = 0 ; i < n ; i++ )  
	for( j = 0 ; j < n ; j++)  
++sum;  
```
Ans: Each of the $n$ operations of the outer loop requires $n$ operations of the inner loop. Algorithm is $O(n^{2})$
### 3.
```cpp  
sum = 0 ;  
for( i = 0 ; i < n ; i++ )  
	for( j = 0 ; j < n*m ; j++)  
		++sum;  
```
Ans: Each of the $n$ operations of the outer loop requires $n*m$ operations of the inner loop. Algorithm is $O(n^{2}m)$
### 4.
```cpp
sum = 0 ;  
for ( i = 0 ; i < n ; i++ )  
	for ( j = 0 ; j < i ; j++)  
		++sum;  
```
Ans: 
The inner loop requires $i$ operations. For each integer $i$ from $0$ to $n-1$, $i$ operations must be performed. This algorithm thus requires $\sum_{i=0}^{n-1}i$ operations. Wolfram Alpha simplifies this to the following expression: $\frac{n(n-1)}{2}$ Thus, the algorithm is $O(n^{2})$
### 5.
``` cpp
sum = 0 ;  
for ( i = 0 ; i < n ; i++ )  
	for ( j = 0 ; j < i*i ; j++)  
		for (k = 0; k < j; k++)  
			++sum;   
```
Ans:
The innermost loop calls for $j$ operations. For each integer $j$ from $0$ to $i^{2}-1$, $j$ operations must be performed. Thus, the inner two loops call for $\sum_{j=0}^{i^{2}-1}j$ operations when combined. The outermost loop requires the middle loop be executed for each integer $i$ from $0$ to $n-1$, so combining all three loops would require $\sum_{i=0}^{n-1}\sum_{j=0}^{i^{2}-1}j$ operations. Wolfram Alpha simplifies this to the expression: $\frac{n^{5}}{10} - \frac{n^{4}}{4} + \frac{n^{2}}{4} - \frac{n}{10}$ Therefore, the algorithm is $O(n^{5})$
### 6.
```Cpp
sum = 0;  
for ( i = 0 ; i < n ; i++ )  
	for ( j = 0 ; j < i*i ; j++)  
		if (j % i == 0)  
			for (k = 0; k < j; k++)
				++sum;
```
Ans:
The innermost loop calls for $j$ operations, but only if j is divisible by $i$. This means that the innermost loop will only be executed when $j$ is an integer multiple of $i$, which will happen $i-1$ times. Therefore, the two inner loops call for $\sum_{k=0}^{i-1}ki$ operations. When factoring in the outer loop, the starting value of $i$ must be 1, because $i^{2}-1=0$. Therefore, the full function calls for $\sum_{i=1}^{n-1}\sum_{k=0}^{i-1}ki$ operations, which Wolfram Alpha simplifies to $\frac{n^{4}}{8} - \frac{5 n^{3}}{12} + \frac{3 n^{2}}{8} - \frac{n}{12}$. Thus, the algorithm is $O(n^4)$

## Q2. 
Programs A and B are analyzed and found to have worst-case running times no greater than $150N \log_{2}N$ and $N^{2}$ , respectively. Answer the following questions (3 points) -  
### a. Which program has the better guarantee on the running time for large values of N (N > 10,000)?  
Ans:  
Algorithms with logarithmic time complexity outperform those of polynomial time when evaluated over large values of N, so Program A has the better runtime. This is confirmed by calculations:
![[Pasted image 20240606000942.png]]
### b. Which program has the better guarantee on the running time for small values of N (N < 100)?  
Ans:  
The same calculations show that program B has better runtimes for small N, which is generally the case when comparing polynomial and logarithmic algorithms
### c. Which program will run faster on average for N = 1000?  
Ans:  
The worst case scenario of program A requires $1.495\times 10^{6}$ operations, while that of program B only requires $1\times 10^{6}$ operations. Thus, program B will run faster for N=1000

## Q3. Solve the following recurrence relations using the Master theorem (2 points) -  
### a. $T(n) = 3T(\frac{n}{2}) + \frac{n}{2}$  
Ans:
$a=3,\,b=2,\,d=1$
$b^{d}=2, b^{d}<a$ 
This is a type 3 algorithm with $T(n)=O(n^{\log_{2}3})$
O(n) =  $O(n^{1.585})$
### b. $T(n) = 4T(\frac{n}{2}) + n^{2.5}$
Ans: 
$a=4,\,b=2,\,d=2.5$
$b^{d}=2^{2.5}, b^{d}>a$ 
Type 2 algorithm with 
O(n) =  $O(n^{2.5})$
## Q4. Analyze the run time complexity of the following algorithms (2 points)  
### a. Given an array (or string), the task is to reverse the array/string.  
Algorithm -  
1) Initialize start and end indexes as start = 0, end = n-1  
2) In a loop, swap arr\[start] with arr\[end] and change start and end as follows : start = start +1,  end = end – 1  
3) Repeat 2) while start < end  

Ans:  
Each swap of characters requires constant time, and these swaps occur $\frac{n}{2}$ times. Thus, the algorithm is $O(n)$
## Q5. Given an array A[], the task is to segregate even and odd numbers. All even numbers should appear first, followed by odd numbers.  
Algorithm -  
1) Initialize two index variables left and right: left = 0, right = size -1  
2) Keep incrementing left index until we see an odd number.  
3) Keep decrementing right index until we see an even number.  
4) Swap arr[left] and arr[right]  
5) Repeat 2 - 4 while left < right  

Ans:
There is no nesting of loops, and all operations within the single loop require constant time. Considering the worst case, where each number in the array must be swapped, $\frac{n}{2}$ operations must be completed. Thus, the algorithm is $O(n)$

For class #data-structures 