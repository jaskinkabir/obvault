# Architecture
- Includes the following
	- Count register
	- Incrementor/decrementor
	- Comparitor
	- Comparison register
# Computing Count Value
- $$\text{CountValue} = \frac{\text{DelayTime}}{ClockPeriod}$$
	- System clock of f901rc is 48MHz
# Types of Counters
- General Purpose
	- Simple, short delays
	- Have significant error compared to RTC
	- Error accumulates over long periods
- Real-Time Clocks
	- Very precise
- Watchdog
	- Used to reset mcu when stuck
- SysTick
	- Used for general purpose timing
	- Used by OS for scheduling
# ARPE
- ![[Pasted image 20251007174257.png]]
- The ARPE bit ensures that changes to the ARR register only occur after an update event
- 

For class #embedded