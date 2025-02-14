Expands [[Properties of Convexity]]
# How can a Matrix Be Positive?
## Scalar Positivity
- Consider a vector $\overrightarrow{x}$ and a scalar $\alpha$. 
	- If $\alpha$ is positive, multiplying the two would result in a vector that points in the same direction as $\overrightarrow{x}$ and is scaled by $\alpha$
	- If $\alpha$ is negative, the resulting vector points in the opposite direction

```tikz
\begin{document}
  \begin{tikzpicture}[domain=-4:4]
    \draw[very thin,color=gray] (-4.1,-4.1) grid (4.1,4.1);
    \draw[->] (-4.2,0) -- (4.2,0) node[right] {$x$};
    \draw[->] (0,-4.2) -- (0,4.2) node[above] {$f(x)$};
    
    \draw[->, color=red, very thick] (1,1) -- (2,2) node[below] {$x$};
    \node[color=red, circle, fill] (x0) at (1,1) {};
    
    \draw[->, color=green, very thick] (1, 1) -- (3, 3.3) node[above] {$2x$};
    \draw[->, color=blue, very thick] (1,1) -- (-1,-1) node[left] {$-2x$};
  \end{tikzpicture}
\end{document}
```
- In other words, $\alpha$ is positive if $\overrightarrow{x}$ and $\alpha \overrightarrow{x}$ point in the same direction
- The Cauchy Schwartz inequality shows how to say this quantitatively:
	- $\alpha>0$ iff $x^{T}\alpha x > 0$ 
- 
## Matrix Positivity
- Now consider that vector $x$ and a matrix $A$. We can say $A$ is positive if $x^{T}Ax > 0,\, \forall x$
	- If the inner product must be strictly greater than 0, then A is positive and definite
- However, if we allow for the possibility that the resulting vector $Ax$ is orthogonal to $x$, when the inner product is 0, then $A$ is **Positive Semidefinite**
- This is written as $A \succ 0$ for definite and$A \succeq 0$ for semidefinite
# How to Determine If a Matrix is PSD?
## Eigenvalues
- An eigenvalue is a scalar $\lambda$ such that $Au = \lambda u$, where $u$ is an Eigenvector of $A$
- If you multiply the eigenvector and the matrix, this is an equivalent operation to multiplying the eigenvector by the scalar $\lambda$
- This means that for a positive semidefinite matrix, all eigenvalues must be positive. 
	- The converse is also true. If all the eigenvalues are positive, the matrix is positive semidefinite
## Determine if a symmetric matrix is PSD
- Calculate the determinant of the 1x1, 2x2, 3x3...nxn matrices with the top left value as $A_{11}$
- If all of these values are positive, the matrix is PSD

For class #optimization-ml
