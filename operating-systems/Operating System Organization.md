# OS Services
![[Pasted image 20260820103122.png]]
- OS is an intermediary between user programs and hardware
- Programs access hardware through OS services called through system calls
 # Services

- Program Execution
	- Allocate memory
	- Load binary
	- Jump to entry point
- I/O Operations
	- Sending commands
	- Servicing interrupts
	- Receiving data
- File Systems
	- Read/write
	- Permissions
	- Logical to physical block mapping
- Communication
	- Inter process
	- Networking
- Resource allocation
- Accounting
	- Keep track of which resources have been allocated by which applications
	- Allocation must be fair to applications
- Error detection/handling
	- Exceeding memory bounds
	- Violating memory access permissions
	- When an application cannot handle an error, it calls the OS
- Protection and security
	- Preventing applications from accessing memory of other applications
# System Calls
- Programming interface to OS services
- Typically written in a high-level language
- Mostly accessed by programs via high-level API
	- Win32
	- POSIX for Unix
	- Java API for JVM
- Types 
	- Process control
	- File/device management
	- Info mgmt (timers. system data query,...)
	- Communication
	- Protection
![[Pasted image 20260820104039.png]]

# Dual-Mode Operation
![[Pasted image 20260820104337.png]]
- Need to have some mechanism for determining whether a given program should be able to access hw
- Use dual-mode execution
- **Kernel/Supervisor Mode**
	- Task executed on behalf of OS
	- Access hardware resources
	- Protected from interference with user programs
- **User Mode**
	- Task executed on behalf of application
	- Tasks that don't need direct access to hw resources
- Implementation:
	- Mode bit provided by hardware
	- Privileged instructions execute only in kernel mode
	- Syscalls and interrupts cause user-to-kernel mode transition
# Traps Vs. Interrupts
## Interrupt
- Asynchronous hardware event
- Caused by external event
- Can be masked
	- Bitfield that tells OS whether a hardware interrupt trigger can be ignored/not services
- Interrupt Service Routines cannot be interrupted (in XINU)
## Trap
- Synchronous software event
- Caused by execution of current instruction

# System Call Invocation
![[Pasted image 20260820110221.png]]

# Inter-Process Communication Models
## Message Passing
- Connection oriented
- For small data exchanges
- Easier
## Shared Memory
- Simple and performant
- Must be protected and synchronized
# OS Structure
## Monolithic
![[Pasted image 20260820111520.png]]
- Put every core service into a single large program running in kernel mode
- Linux is one of these
## Layered Approach
![[Pasted image 20260820111534.png]]
- OS divided into levels
- Bottom layer is hw, outer layer is user interface
- Each layer uses functions and services of only the next lower level
- Note that there are two memory management layers
## Microkernel Approach
![[Pasted image 20260820111837.png]]
- Basic OS services in kernel mode
- Some services moved to user mode (modules)
- Comunication between user modules implemented by exchanging messages with microkernel

### Pros
- Extensibility
- Portability to new architectures
- Reliability and security (less code running in kernel mode)
### Cons
- Performance overhead of user-kernel space communication


|             | Performance | Extensibility | Reliability |
| ----------- | ----------- | ------------- | ----------- |
| Monolithic  | Very good   | Terrible      |             |
| Layered     |             | Good          |             |
| Microkernel |             | Best          | Best        |

## Loadable Kernel Modules
- Compromise between layered and microkernel approach
- Kernel provides core services, loadable kernel modules provide more services
	- Linked/loaded either at boot or run time
- Similar to layered system
	- Clear interfaces between kernel modules
	- More flexible: each module can call any other module
- Similar to microkernel
	- Primary module has core functionality
	- More efficient: no message passing
	- Use shared memory
- Modern OSes do this
# System Boot
## BIOS
- Basic input output system runs on startup
	- Firmware located on EPROM chip on motherboard
	- Functions:
		- Test and init hardware: POST
		- Locates boot device and invokes bootstrap loader
		- Provdes basic system services that OS can use during boot process
		- Offers setup utility
- Replaced by UEFI (Unified Extensible Firware Interface) with more advanced features
	- Secure boot, networking, included drivers, extensibility
## Bootloader
- Code typically stored in Master Boot Record (MBR)
	- Located at start of storage device
	- Contains
		- Partition table (layout and status of partitions)
		- Identifiers of storage devices (disk signature)
- Loads OS into mem
- Example: GNU GRUB (Grand Unified Bootloader)
	- Allows selection of kernel from multiple disks and versions

For class #operating-systems