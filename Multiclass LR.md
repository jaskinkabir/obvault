A machine learning problem can be cast as
$$\min_{x} \frac{1}{m}\sum_{i=1}^{m}l(a_{i},\, y_{i},\, x)+\lambda \text{pen}(x)$$
For a logistic regression, this loss function $\ell$

$$Q_{k}(a_{j},\, X) = \frac{e^{a^{T}X_{k}}}{\sum_{l=1}^{M}e^{a^{T}X_{k}}}$$
- Odds of $a_{j}$ belonging to class $k$
	- Uses softmax
- $$y_{jk} = \begin{cases}
1,\,  a_{j}\in\text{class k}  \\
0,\, \text{otherwise}
\end{cases}$$
True class distribution:
$$P = \begin{bmatrix}
y_{j_{1}} \\
y_{j_{2}} \\
y_{j_{3}} \\
\dots \\
y_{jM}
\end{bmatrix}
Q = \begin{bmatrix}
Q_{1} \\
Q_{2} \\
Q_{3} \\
\dots \\
Q_{M}
\end{bmatrix}$$
$a_{j}^{l}= \sigma(W^{l}a^{l-1}_{j}+g^{l})$
- The output of the $l^{th}$ layer
