Continues [[Operating System Organization]]
Continued by [[Context Switching]]
Continued by [[Threads]]
# Program
- Passive data existing on disk or memory
# Process
- Active memory-resident data structure/object used by OS to keep track of applications
- Many processes may be spawned by one program
- Each process has one PID (process id)
- PIDs are associated with a Parent PID or PPID
- Can be spawned with the C `fork()` primitive
# Processes in Memory
- Starting at 0 and increasing, processes see the following memory block organization
	- Text
	- Data
	- Heap
	- Stack
- Text and data have fixed size
- Heap and stack have variable size
# Process States
- Ready
	- Moves into the running state by the scheduler
- Running
	- Actively using the CPU
	- Moved into and back into the ready state by the scheduler
	- Scheduler exclusively owns transition into this state
- Waiting
	- Waiting on some event like I/O or synchronization
	- Can only transition back to the ready state when the event happens
	- The OS scheduler must solely own moving processes into the ready state
- ![[Pasted image 20260825104510.png]]
# Process Control Block (PCB)
- Process number (PID)
- State
- Program counter
- Registers
- Memory used
	- Pointers
- Open files, I/O devices
	- Pointers
- Scheduling info
- Resource usage info
- Others
## Linux Handling
- Keeps a doubly linked list of PCBs linking parent processes to child processes
```c
pid t_pid; /* process identifier */
long state; /* state of the process */
unsigned int time_slice /* scheduling information */
struct task_struct *parent; /* this process’s parent */
struct list_head children; /* this process’s children */
struct files_struct *files; /* list of open files */
struct mm_struct *mm; /* address space of this process *
```
![[Pasted image 20260825104759.png]]
## XINU
- Has some set maximum number of processes that can be spawned
- Has a fixed size array of PCBs called `proctab`
- Has a global number of active processes and current executing pid
```c
struct procent { /* Entry in the process table */
uint16 prstate; /* Process state: PR_CURR, etc. */
pri16 prprio; /* Process priority */
char *prstkptr; /* Saved stack pointer */
char *prstkbase; /* Base of runtime stack */
uint32 prstklen; /* Stack length in bytes */
char prname[PNMLEN]; /* Process name */
sid32 prsem; /* Semaphore on which process waits */
pid32 prparent; /* ID of the creating process */
umsg32 prmsg; /* Message sent to this process */
bool8 prhasmsg; /* Nonzero iff msg is valid */
int16 prdesc[NDESC]; /* Device descriptors for process */
};
extern struct procent proctab[]; /* Process table */
extern int32 prcount; /* Currently active processes */
extern pid32 currpid; /* Currently executing process */
```
- Note that the PCBs do not store their pids
- The PID is stored implicitly as its index into the process table
# XINU Memory Organization
- Only the stack is private to each process
- The heap, text, and data regions are globally shared
# Process Manipulation
- Performed by OS routines
- Operations
	- Creation
	- Termination
	- Suspension
	- Resumption
- Activity recorded in process table
## Process Creation
- Parent processes create child processes
- These processes can create other processes
- This creates a tree of processes
### Address Space Policies
 - Can duplicate parent address space into child (linux)
- Or load a different program (xinu)
### Resource Sharing Policies
- Parent can share all, some, or no resources with children
### Execution Polcies
- Parent and children can execute concurrently
- Parent can wait until children terminate

### Process Creation in UNIX
- `fork()` system call can fail or succeed
	- Duplicates address space upon success
	- Will return child PID
		- Since fork's return value is in the parent address space, the child will get the PID in its address space
		- The child will see 0 as its PID, when the parent knows its actual PID is different
	- Both parent and child will start execution on the line after the `fork()` system call
	- What if program calls `fork()` 3 times consecutively?
	- ![[Pasted image 20260825111345.png]]
	- 8 total processes
- What if 
```c
main() {
	int x = -1;
	x = fork(); // f1
	x = fork(); // f2
}
```
![[Pasted image 20260825111606.png]]
- `exec()` replaces the process's memory space (image) with a new program
- `wait()` parent waits until child completes execution
	- Because leaf processes have id 0, we can call wait if we have PID > 0
	- If PID=0, we can do the operation that requires waiting and then call `exit()` or return from `main`
- ![[Pasted image 20260825110327.png]]
#### Shell Process Creation
- Have a parent shell process
- When a command is entered, create a child to execute the command and wait until termination to get next command
- Use the pid > 0 pattern to check if current command should wait or call `exec()`
## Process Termination
- Child process invoke `exit()` 
	- Returns status to parent()
	- Asks OS to deallocate process's resources
- Parent calls `abort()`
	- Child is either no longer required or exceeded allocated resources
	- Parent task terminates
	- Termination cascades
		- Some OSes don't allow a child to execute if the parent has terminated
		- If parent terminates, OS terminates its children recursively
- System administrator calls `kill()`
- Parent process waits for termination of child `pid = wait(&status)`
- **Zombie Process:** Has completed execution but still has an entry in the process table
- **Orphan:** Parent terminated child without invoking `wait()`
	- Not possible if OS uses cascading termination
## Process Suspension
- Temporarily stop a process to:
	- Change state in PCB
	- Retain entry in process table
	- Save machine state for later resumption
- Scheduling mechanisms may use suspension to preempt processes
	- Priority based
	- Time slice based
## Process Resumption
- What is to be done?
	- Either move process state in PCB to running state
		- Save status of running process
		- Preempt running process
		- Load status of new process
		- Update PCB
	- Or move the process to the ready state
For class #operating-systems 
