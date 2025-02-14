
```tikz
\begin{document}
  \begin{tikzpicture}[domain=-4:4]
    \draw[very thin,color=gray] (-4.1,-4.1) grid (4.1,4.1);
    \draw[->] (-4.2,0) -- (4.2,0) node[right] {$x$};
    \draw[->] (0,-4.2) -- (0,4.2) node[above] {$f(x)$};
    
  \end{tikzpicture}
\end{document}
```