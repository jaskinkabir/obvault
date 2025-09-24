Uses [[Clock Skew and Path Constraints]]
# Schematic Screenshots
## Latch Schematic![](https://lh7-us.googleusercontent.com/H5VvWiQOFvk_JM93oWSt1ReYvncNy41FCSdGv1HwSh8KE4az0mJczk39jC6TWTWuv944HVAP0Vnlgpc2qs4_6qdf8ZPupf3F-FdwJOrAlG0rrE2svXfe4JD7cwEjchdyIOWEs02YiHXYkM46pvG6ZD0)
## Flip-Flop Schematic![](https://lh7-us.googleusercontent.com/8ZYdnF6y2xcZIosP6peJ1KIbakLuY5hs1nde7u9KYlEGQOZgwNLwVUI-ybTEPCEXnOLk3sCVZ34t6wHnBCGlyGrtx_g350YLJqq_BRhjCEctX6M6fuiVG8M0pCQxdP11oWCw55QK1uhKzUu_MijwDXw)
## Flip-Flop Test bench![](https://lh7-us.googleusercontent.com/VlOxjHHof-vk4k6qTOeFd1VQ_YqX8_njFMprjELmNOIh2b32Byr4EALpxmNo8rsPNDmZs6UB2DtQJeAZ5_N66dpDyRjB3GC6ZmEt85wOeHv3v0FhF1-mfST7T-kQFGwZUhxjllKVWytZD_CT6rZAiMY)
# Simulations
## Proper Operation
### ADE Window![](https://lh7-us.googleusercontent.com/M4sQQrjSWriNUqHa3ZKUeo1z92LPvibw9hRf3zxdPOy9DxQh2G_PlihOpwStHNolQAhKZiEg2umUyzoJ4PfT2mGUWoQQqX41JYepBRV9t_qtvNzawP-v5UkpCaHa5C0xz0-JF7jSOUCw-532XI-pd-Q)
 The clock signal in the flip-flop test bench has a period that is configured by changing the simulation variable Tclk
 The data signal has the following parameters
				- Tdat: Period of the data signal
				- datDelay: Delay between start of simulation and first edge of the data signal
				- datPw: Pulse width of the data signal
### Waveform![](https://lh7-us.googleusercontent.com/-kgEqXFQnDlcvu2VKq1vsG7RSGBBZNX9a-IGyxMJarU4094FyujUqXstZWbLxY_LrRgww4q2pRZ6B1Vk4kc_QKksRmO6PZlfV37LPxvfi_fDlXg0D9P3YIZDWWtxbEsPR4-ccGALpB3ayF-QzUup5jo)
 The Q output only changes on the rising edge of the clock signal. This is true even when there is a change in the data input while the clock signal is high. The falling edge of the clock signal does not affect the Q output either. The waveform pictured above demonstrates the proper operation of the D Flip-Flop.
## Setup Time
### ADE Window![[Pasted image 20240315135813.png]]
The ADE Window is set to plot a value designated Tcq, which is a calculator expression that measures the time between the first clock edge and the first edge of the Q output of the flip-flop
There is now a variable in the window called t_shift, that shifts the first edge of the data signal to the left as it is increased. This t_shift value is the value of $t_{DC}$, or the time between the data edge and the clock edge
The Parametric Analysis window is set to vary the value of $t_{DC}$ to measure the minimum and ideal setup and hold times for this flip-flop
### Minimum![[Pasted image 20240315210955.png]]
For this simulation, the data signal was set to start high and transition low. This is because the flip-flop design's Q output starts high when powered on. On the first rising edge of the clock signal, the flip-flop should latch the low value. If it instead latches the high value, that would indicate that $t_{DC}$ was too low, and the setup time requirement has not been met.  
This failure occurred for values of $t_{DC}$ less than 26ps, meaning the minimum value of $t_{setup}$–the minimum time the data input must be stable before the clock edge– is between 25ps and 26ps. Since the step size of this simulation was 1ps, the value of 26ps will be considered the minimum.
The graph on the left plots the calculated value of $t_{PCQ}$, or the propagation delay between the clock edge and the change in the Q output, plotted over the varying values of $t_{DC}$. The minimum $t_{setup}$value of 25ps is also associated with the highest value of $t_{PCQ}$ which was found to be 142.8ps. Using this value as the $t_{setup}$ time is therefore not desirable.
### Ideal![](https://lh7-us.googleusercontent.com/477wsIMRakjGBdfaSwH8iD4irFjrlVUNjSV2IddjcPVl6bSFjyeYldjauv9rnkdcONzZv_KNQIuKyLjzpvNjM66s8kEZ1OdavljGKVDYMA9Jc1VKVw_ava795IV0ur6TEu2FaGHKzafMcJYT6dLyEbU)
Using the unity slope method, the ideal value of $t_{setup}$ was found to be 45ps, where the associated $t_{PCQ}$ is only 89.6ps
## Hold Time
### ADE Window![[Pasted image 20240315115640.png]]
Note that the t_shift variable now shifts the data signal to the right. t_shift now represents the value $t_{CD}$
### Minimum![](https://lh7-us.googleusercontent.com/z-BFKZvx9ql0Co0qGY3itUNKgp3tL4EN5jgKIoezkM3dqCCWs7EP3gmE6vQZbQGk5GH43MsRkhsmpPpO3bH37qC2Vw40ztI_2SksqXhBCMx5ETjN5G0YB_nnCDa8WSaPhM8On7VXl-zBnSfSH_BiNH0)
For this simulation, the data signal was set to start low and transition high. The flip-flop should latch the initial zero on the clock edge, and if it latches a one instead, that would indicate that the hold time $t_{hold}$was too low.
The minimum amount of time the data input must be held stable after the clock edge in order for the flip-flop to latch the correct data is called the flip-flop’s hold time, or $t_{hold}$. The minimum hold time can be found by varying $t_{CD}$ until the flip-flop fails to latch the correct data. Because the D input signal has some propagation delay before it is read by the flip-flop, the data can change slightly before the clock edge and so the minimum $t_{hold}$ is negative. However, this minimum value of $t_{CD}$ also comes with the maximum possible value of $t_{pCQ}$, or the propagation delay between the clock edge and the change in the flip-flop’s Q output.
The waveform on the left of the graph above shows the relationship between $t_{CD}$ on the x-axis and $t_{pCQ}$ on the y-axis. A smaller $t_{CD}$ results in a larger $t_{pCQ}$
Since hold time failure occurs when $t_{CD}$  is -18ps but does not occur at -17ps, the minimum hold time for this flip-flop is between -18ps and -17ps. The step time for this simulation was 1ps, so the measured minimum $t_{hold}$ was -17ps
The meaning of the negative hold time is that the latest time the data is sampled is before the clock edge.
Taking into account the minimum setup time found above, the data to be read by the latch must be stable between 26ps and 17ps before the clock edge. This is the data it can read.
### Ideal![](https://lh7-us.googleusercontent.com/TbqtqjMKNfLAnlHKj7nISg4DHnJ3_3xbyRsdLk9Fky_9POPu7uIw6Iw5XxEUq7wX3ROoDQZUZ4E3V89mBJHzsAEpkQn1mGOqs6Vd7iCOgBYXRl0KCutWx939zqq0LTDHe_w94QfqwGo4WNs53mQvJFI)
Using the unity slope method, the ideal hold time was found to be -14ps
## Average Current And Propagation Delay
### ADE Window![[Pasted image 20240315233015.png]]
The value of $t_{DC}$ was chosen to be the midpoint between the ideal setup and hold times: $t_{DC}=30ps$
The rest of the values were reset to their state during the Proper Operation simulation
An added plot was added for the current consumption of the flip-flop
This screenshot was captured after the simulation was run so it contains the calculated average current consumption and propagation delay of the flip-flop with an ideal data input
	$I_{DDavg}=3.951nA$
	$T_{pcq}=119.4ps$
### Ideal Waveform![[Pasted image 20240315233333.png]]
The current spikes on the edges of the clock and data input signals
# Measured Value Table

| Measurement |  Value   |
| ----------- |:--------:|
| $I_{DDavg}$ | 3.961 pA |
| $t_{setup}$ |  45 ps   |
| $t_{hold}$  |  -14 ps  |
| $t_{pcq}$   | 119.4 ps |

For class #vlsi/assignments
