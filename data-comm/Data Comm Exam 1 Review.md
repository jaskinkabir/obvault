![[Pasted image 20240718084617.png]]
Each pixel can take on 1 of 32 values, so $M=32$, $L=\log_{2}32=5$
There are $480*500$ pixels, $480*500*5$  bits per picture
Transmission of this TV signal requires a transmission rate of $R=480*500*5*30=36$Mbps. 
If the channel has 4.5MHz bandwidth and a 35dB SNR, what is the capacity?
$C=2B\log_{2}M=2*4.5*5=45$Mbps
$C=B\log_{2}(1+10^{SNR_{dB}/10})=52.3$Mbps
![[Pasted image 20240718085408.png]]
$C=9600$
$M=4$
$C=2B\log_{2}M,\,B=\frac{C}{(2\log_{2}M)}=\frac{9600}{2\log_{2}4}=\frac{9600}{4}=2.4KHz$

![[Pasted image 20240718085911.png]]
$L=4$
Baud $D=1000$ baud
$D=\frac{R}{L}, \, R=DL=4000$bps
![[Pasted image 20240718090015.png]]
$L=8$
$R=9600$
$D=\frac{R}{L}=\frac{9600}{8}=1200$ baud

![[Pasted image 20240718090143.png]]
$B_{T}=R=2Kbps$
![[Pasted image 20240718090212.png]]
$B_{T}=5000=R$
Maximum bit rate is 5Kbps. Maximum baud for Binary ASK is 5Kbps
![[Pasted image 20240718090344.png]]
$B=2\Delta F+(1+r)R$
$B=3000+2000=5000$Hz
# ![[Pasted image 20240718092424.png]]
$B=3600Hz$ 
![[Pasted image 20240718092454.png]]
$f_{s}=2f_{max}=8000Hz$
$D=\frac{R}{\log_{2}M}$
$R=C=2BL=8000L$
$C=40000=8000L$
$L=5$, $M=32$ 32 **Quantization levels** at $8kHz$ sampling frequency
![[Pasted image 20240718093400.png]]
$SNR_{db}=6.02(5)+1.76=31.86$dB $SNR=10^{31.86/10}=1535.7$
![[Pasted image 20240718094506.png]]
$B_{T}$

For class #data-comm