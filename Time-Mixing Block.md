# RNNs Cannot be Parallelized

# Time Mixing Block
- Mix input $x[t]$ with $x[t-1]$ and project linearly into r,k,v
- $r_{t}=W_{r}*(\mu_{r}x_{t}+(1-\mu_{r})x_{t-1})$
- $r_{t}=W_{r}*(\mu_{r}x_{t}+(1-\mu_{r})x_{t-1})$ (k)
- $r_{t}=W_{r}*(\mu_{r}x_{t}+(1-\mu_{r})x_{t-1})$ (v)
- $o_{t}=W_{o}*(\sigma (r_{t})\cdot wkv_{t})$
# Channel Mixing Block