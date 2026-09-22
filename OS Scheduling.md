Continues [[Threads]]
Continues [[Processes]]
Continued by [[Data Consistency]]
# Scheduling Criteria/Metrics
- Metrics the OS can use to inform scheduling decisions
	- OS must choose which thread to run next
	- Must define some policy based on some metrics
- Run time
	- Time during which a process/thread uses the CPU
	- =$t_{end}-t_{start}-T_{wait}$
- Turnaround time
	- Total time it takes for a process to finish
	- Includes idle/IO time
	- =$t_{end}-t_{start}$
- Waiting time
	- Time spent waiting
	- May be waiting on
		-  I/O
		- Waiting on scheduler to move from ready to running
- Response Time
	- Time from process creation time to first time process is scheduled
- Throughput
	- Work/time
	- \# of processes completed per unit time
- CPU Utilization
	- How busy the CPU is kept
- Fairness: 
	- How evenly resources are distributed to processes over time
	- The definition of fairness can lead to different measured results on the same scenario
	- ![[Pasted image 20260908110800.png]]
	- In both scenarios, runtime of P1 and P2 are the same
	- However Turnaround time for P2 in the second scenario is much longer
	- Fairness should ideally be measured in terms of ~equal turnaround times
# Assumptions
- Let's start with unrealistic simplifying assumptions
	- Jobs arrive simultaneously
	- Jobs run to completion (non-preemptive scheduler)
	- CPU-intensive jobs (no I/O)
	- Runtime of jobs is known
- We will first focus on turnaround time and waiting time
# Polices
- Let's break one assumption at a time to get to the best policies
- 3 Jobs
	- A: running time 100
	- B, C: Running time 10
## Non-Preemptive Schedulers
### First Come First Serve (FCFS)
- Schedule A->B->C
- Turnaround time:
	- A: 100
	- B: 110
	- C: 120
	- Avg: 110
- Waiting Time:
	- A: 0
	- B: 100
	- C: 110
	- Avg: 70
- Response Time:
	- A: 0
	- B: 100
	- C: 110
### Schedule Shortest Job First (SJF)
- Schedule B->C->A
- Turnaround
	- A: 120
	- B: 10
	- C: 20
	- Avg: 50
- Waiting Time
	- A: 20
	- B: 0
	- C: 10
	- Avg: 10
- New scenario:
	- A arrives at 0, running time 100
	- B and C arrive at t=10, running time 10
- Turnaround
	- A: 100
	- B: 100
	- C: 110
	- Avg: 103
- Waiting
	- A: 0
	- B: 90
	- C: 100
	- Avg: 63
- Best we can do without preemption
## Preemptive Scheduler
- Whenever a new process arrives, make a new scheduling decision
### Shortest Time-to-Completion First (STCF)
- Aka preemptive shortest job first (PSJF)
- Revise scheduling decisions at any new job arrvival
- A arrives first, start running
- B and C arrive at t=10, have shorter running times than remaining time to finish A
- Schedule B and then C, then finish A
- Turnaround time
	- A: 120
	- B: 10
	- C: 20
	- Avg: 50
- Waiting time:
	- A: 20
	- B: 0
	- C: 10
	- Avg: 10
- Response time
	- A: 0
	- B: 0
	- C: 10
	- Avg = 3.3
## Time-Slice Schedulers
- Need to have a scheduler sensitive to response time
### Round-Robin
- Maximizing throughput sacrifices response time and fairness
- Round Robin optimizes for fairness
- How to set time slice time:
	- Compromise between response time and context switch overhead
	- RR is fair, improves response time at the cost of turnaround time
	- Unfair policies like SJF and STCF optimize turnaround time at cost of response time
## Introducing I/O
- When a process requests I/O, it goes idle and the OS can schedule a different job
- Interrupt can birng process back to ready state
- Example
	- Jobs A and B use CPU for same time
	- A is **interactive** and uses I/O every 10 time units
	- ![[Pasted image 20260910102327.png]]
- We can use Shortest Time to Completion First and treat every CPU sub-job (aka CPU burst) of A as an independent job
	- Sub job here refers to the short bursts after disk I/O where A uses the CPU
	- ![[Pasted image 20260910102338.png]]
## Queue-Based Scheduling
- Runtime of jobs is now unknown
- Unknown whether a job is I/O or CPU intensive
### Multi-Level Feedback Queue (MLFQ)
- Use recent past to predict future
	- Implicitly characterize jobs and classify them as CPU or I/O intensive
- Goals:
	- Optimize turnaround time for CPU intensive jobs
	- Minimize response time for interactive jobs
- Main mechanisms
	- Multiple Queues, each assigned a different priority level
		- Rule 1: priority-based scheduling across queues
		- Rule 2: RR scheduling within a queue
		- These rules are not enough yet
	- Priority of a job can vary dynamically according to its observed behavior
		- Interactive jobs maintain high priority
		- CPU-intensive jobs decrease in priority as they execute
- Start with two rules
	- If Priority(A)>Priority(B), run A
	- If Priority(A)=Priority(B), A&B run in RR fashion
	- Starvation problem?
		- High-priority processes will keep being scheduled and starve the lower-priority processes
		- Solution is to periodically decrease priority as jobs execute
- How to dynamically change priority?
- Add additional rules
	- Rule 3: When a job enters the system, it places at the highest priority (good response time and initial fairness)
	- Rule 4: a job uses up an entire time slice, its priority is decreased. Otherwise, it stays at the same priority level
	- ![[Pasted image 20260910104131.png]]
	- **Starvation Problem** again: Interactive jobs will still starve CPU-intensive jobs, as they will never increase in priority
	- **Circumvention Problem**: A process can sleep right before each time slice ends to game the system
- **Priority Boost** Tackling starvation problem:
	- After some time period $S$, move **all** jobs into the topmost queue
	- Resets state
- **Time Allotment:** Tackling circumvention problem
	- Modify rule 4: Once a job uses up its time allotment at a given level, its priority is reduced
	- ![[Pasted image 20260910105357.png]]
#### Final MLFQ Ruleset
1. If Priority(A)>Priority(B), run A
2. If Priority(A)=Priority(B), run A&B in RR fashion
3. Jobs are created at the highest priority
4. Once a job uses up its time allotment at a given level, its priority is reduced (Priority Downgrade)
5. After some time period $S$, move **all** jobs into the topmost queue (Priority Boost)
- The multiple queues can be implied by a priority field in the procent
	- Unified ready queue, sorted by priority
#### Varying the MLFQ Approach
- Can configure 
	- Number of queues/priority levels
	- Time slice per queue
	- Frequency of priority boost $S$
- Some approaches
	- Vary time slices across queues
		- Time slices increases (e.g. by a factor of two) as priority decreases
	- Adjust priority using mathematical functions + decay usage
	- High priority queues for OS work
	- Allow user advice
- MFLQ Uses:
	- BSD Unix derivatives, Solaris, Windows NT and later
## Proportional Share
### Goals
- Recall that SJFF and STCF optimize turnaround time
- RR optimizes response time
- MLFQ focuses on performance
	- Makes no assumptions about characteristics of programs
	- Balances:
		- Turnaround time for CPU-intensive
		- Response time for interactive
- Proportional-share scheduling focuses on fairness
	- Guarantee each job is given a predefined fraction of CPU time
	- Considered a marketplace system where each job is given time credits
- Mechanisms
	- Probabilistic: Lottery scheduling
	- Deterministic: Stride scheduling
### Lottery Scheduling
- In second project
- Probabilistic:
	- Cannot ensure fair sharing
- Tickets: share of a resource that a process should receive
- Periodic scheme like round robin
	- Probabilistic mechanism
	- Based on time slices
- Example:
	- 3 jobs A, B, and C with 10%, 20% and 70% expected share
	- Create ranges of numbers from 0-99
	- A gets 0-9, B gets 10-29, C gets 30-99
	- Every time slice, generate a random number in \[0,99\]
	- If number lands in a job's range, preempt and schedule that job
- The total number of tickets is determined only by the # of processes in the READY STATE
#### Implementation Code Snippet
```c
int counter = 0;

int winner = random() gtickets;

struct node_t *current = head;

while (current) {
	counter = counter + current->tickets;
	if (counter > winner) break;
	current = current->next;
}
ready(current->pid)
```
- Note that order of jobs in the linked list does not matter for correctness
- For performance, it's better to put the processes with the largest number of tickets first so linked list traversal ends earliest
#### Policy Extensions
##### Multiple ticket currencies
- System assigns tickets to users with a global currency
- Users assign tickets to their own jobs using local currencies
- System converts local into global currencies
- Example: User job tree
	- U1: 10 Global Tickets (GT)
		- J1: 20 local tickets (LT)
		- J2: 80 LT
	- U2: 30 GT
		- J3: 1 LT
		- J4: 1 LT
		- J5: 1 LT
	- U3: 60 GT
		- J6: 10 LT
-  Scheduler converts local currencies to global currency by multiplying global user currency by proportion of total local currency
- Scheduler makes linked list with 6 jobs
	- J1: 2
	- J2: 8
	- J3: 10
	- J4: 10
	- J5: 10
	- J6: 60
##### Ticket transfer
- A process can temporarily hand off tickets to another process
- Example: server and client process
	- Clients and 1 server job
		- C1: 50
		- C2: 20
		- C3: 20
		- S: 10
- C1 issues a request to server
- For C1 to receive a request from server, it will give its tickets to the server process so it is more likely to be scheduled next
##### Ticket Inflation
- A process can temporarily raise/lower its own ticket count
- Cooperative environment
#### Defining Fairness
- 2 jobs, each with 100 tickets
- ![[Pasted image 20260916223113.png]]
- Fairness = turnaround time of first completed job / turnaround time of second completed job
- Ideally, fairness is 1
	- Jobs have same turnaround time
- In the worst case, fairness is 0.5
	- J1 executes to completion while J2 waits
	- J2's turnaround time is twice J1's
	- fairness = 0.5
- Fairness is easier to achieve as job length increases (why?)
#### Pros and Cons
- Pros
	- Lightweight implementation
		- Minimal per-process state
		- No per-process accounting required
	- Fast
		- As long as RNG is readily available
	- Avoids corner cases
		- As long as lottery keeps being run, even a job with few tickets will eventually be sceduled
- Cons
	- Might not deliver right proportions
		- Because it is not deterministic
	- Ticket assignment
- Ticket assignment problem
	- May not know a priori the knowledge to effectively assign tickets

### Stride Scheduling
- Is deterministic
- Each job has
	- Pass value: used to track global process, incremented by the stride every time the process is scheduled
	- Stride: inverse in proportion to number of tickets
		- If J1=10 and J2=20, define an arbitrary numerator
		- J1 stride = 100/10=10, J2=100/20 = 5
		- J2 will be scheduled more because its **stride is lower**

#### Implementation Code Snippet
```c
current = remove_min(queue); 
schedule(current);
curennt->pass += current->stride;
insert(queue, current)
```
- Jobs with higher stride get bounced up the queue higher than lower stride jobs on each preemption
- Higher priority jobs fall to the bottom of the queue faster
#### Example
![[Pasted image 20260916224427.png]]
- Order of jobs is cyclical and deterministic
- Provides perfectly proportioned share based on ticket count
#### Problem: What if job enters/is created at runtime?
- When a job is created, assign its pass value to the minimum value currently in the system
#### Limitations
- Ticket assignment problem still exists
- Interaction with I/O
	- When a job goes into the wait state for I/O, its pass value is never updated
	- When I/O responds and it re-enters the queue, its pass value will be lower than all the others
# Relevant Code in Xinu
- Scheduler: `resched.c`
- Clock interrupt handler: `clkhandler.c`
- Queue implementation
	- `queue.h`
	- `newqueue.c` - Queue creation
	-  `queue.c` - Process queue and dequeue function
	- `insert.c`- Process insertion in decreasing order of key
	- `insertd.c` - Insert in delta list (for sleep)
	- `getitem.c` - Removal of a process from the queue
For class #operating-systems


