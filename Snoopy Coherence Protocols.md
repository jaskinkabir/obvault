Continues [[Cache Coherence]]
Continued by [[Cache Protocol Optimizations]]
Continued by [[Scalable Cache Coherence]]
- ![[Pasted image 20260212170411.png]]
- Cache sees requests from both processors and from other caches
- Bus request must lookup the cache line to determine hit/miss
# Write-Through Protocol
- Each processor has a private 1 level cache
- Cache is write-through and write-allocate
	- Memory writes allocate space on the cache
- When a bus write is snooped for a cached block, the block is invalidated
	- Snooper must access tag array on every observed write
- If cache reads again, it will miss and retrieve correct data from memory
	- This achieves write propagation
## Scenarios
### Read Hit
![[Pasted image 20260212171050.png]]
### Read Miss
![[Pasted image 20260212171119.png]]
### Write Hit
![[Pasted image 20260212171211.png]]
- Invalidation occurs at the same time step as the memwrite
- What if there is a read before the bus is able to service the write request?
	- Most common fix is called store-to-load forwarding
		- When P issues the read, the hardware searches cache and the request buffer
		- If a match is found in the buffer, the new value is forwarded to the processor and bypasses the cache
### Write Miss
![[Pasted image 20260212171324.png]]
- This is a different Bus message: **Read Exclusive**
	- There must be exclusive access to the cache line
	- 
- Read in order to write, provide both read address and new data to update with
### Simultaneous Write Hit
![[Pasted image 20260212175115.png]]
- P1 and P2 are writing to the same cache line
- One processor will win the arbitration, let's say P1 on the left
- P2 must now invalidate its copy of the data
- P2 must also change its request from BusWr to BusRdX
## Protocol Pros and Cons
- Con: Excessive bus bandwidth requirement
	- Every write from every processor issues a bus write, even if the write is to non-shared data
	- High power consumption, high load on memory
- Pro: Simplest protocol
	- No states other than I and V
	- Memory responds to all reads
	- Serializes memory transactions
	- No cache-cache transfers

# Coherence Protocol State Machines
- Coherence protocols can be represented as a state machine from the perspective of each cache line
- Mealy state machine, transition defined by trigger/action
- I is invalid, V is valid
- PrRd/PrWr is processor r/w
# Write-Through Write-Allocate Protocol SM
![[Pasted image 20260212180150.png]]
- The valid state invalid state only when it observes a bus write
	- For reads, it takes no action
	- For a processor write, it issues a bus write for write propagation
- The invalid state moves to valid when the processor interacts with the cache line
	- This causes a BusRd or BusRdX
## Example Problem

| Access | C1 State | C2 State | C3 State | Bus Request | Data source |
| ------ | -------- | -------- | -------- | ----------- | ----------- |
|        | I        | I        | I        |             |             |
| R1     | V        | I        | I        | BusRd       | Mem         |
| W1     | V        | I        | I        | BusWr       | C1          |
| R3     | V        | I        | V        | BusRd       | Mem         |
| W3     | I        | I        | V        | BusWr       | C3          |
| R1     | V        | I        | V        | BusRd       | Mem         |
| R3     | V        | I        | V        | -           | C3          |
| R2     | V        | V        | V        | BusRd       | Mem         |
# Snooping Overhead
- Both the cache controller and the processor need to access the tag array
	- Cache controller needs to check if a buswr or busrdx conflicts with one of the cache lines
	- PU needs to check for cache hits/misses
- One solution is to duplicate the tags
	- Have one array for the PU, one for the CCU
	- Requires coordination when tags change (during eviction)
- Another solution is snoop filtering
	- Keep track of most recent snoop misses
	- If the tag of the snooped buswr/busrdx is in this array, don't have to access tag array
# Write-Back Protocols
- Allows non-shared writes to happen locally
- Ensure that there is **only one** cached copy of the data
- Allows cache-to-cache transfers, which may be faster than reading from memory
- Reduces Bus bandwidth usage, fewer memory writes
# Modified-Shared-Invalid (MSI)
- Each processor has a private, write-back, write-allocate cache
- Read miss - bring block into cache in **Shared** state
	- **Shared** state means the block may be replicated in other caches
- Write (hit or miss) marks block as **Modified** which invalidates other copies
	- Write back the Modified block when evicted, or when another cache needs the data
	- The **Modified** state asserts that there is only one valid copy of this block
## MSI States
![[Pasted image 20260212182811.png]]
- **Modified:** The data is not clean, there is only one valid copy of this data that has not yet been written to memory
	- R/W permissions on this block
	- Reading or writing to this block requires no action from any other CCU
- **Shared:** The data is clean (memory is coherent with this data), and there may be other copies
	- Moving from M to S is a permission downgrade, also called **Intervention**
	- Can read without consequence, but writing moves to modified state. All other CCUs must invalidate their copies
- **Invalid:** Not in cache
	- Moving to the invalid state is an **Invalidation**
	- Cannot read or write to this block until it is upgraded to S or M state
## Memory Perspective
- Memory responds with data only to <u>some</u> BusRd and BusRdX requests
	- It only responds if no cache was in the M state
	- How does it know it needs to respond?
		- Wait a specific amount of time before responding, long enough to give caches a chance to snoop and respond (timeout)
		- Require caches to report when snooping is complete
- Store data on all flush responses
### Snoop Completion
- How does the cache tell the memory that it's done snooping?
- ![[Pasted image 20260212194532.png]]
- The Dx signal is active low. When cache X completes it snoop, it pulls Dx low
- The NOR operation will set the DONE signal high when all caches are done snooping
- If the memory sees the done signal is high, it will then respond to the read operation
## MSI FSM
- Optimize the state machine by adding a BusUpgr operation
	- If the block is in the S state and gets PrWr, it does not need to read from memory. Use BusUpgr to invalidate other copies and get write permission without data fetch
- Note that moving into the M state invalidates all other copies of the data
	- This ensures only one cache line can be in the M state
	- The M state is essentially the ownership state
	- This means that there need not be a transition to handle what to do when an M state line sees a BusUpgr command, because that can never happen. 
	- Once a BusUpgr happens, it forces all other cache lines into the I state
```tikz

\usetikzlibrary{automata, positioning, calc}
\begin{document}
\begin{tikzpicture}[
	node distance = 11cm,
	on grid,
	auto,
	state/.style={circle, draw, minimum size=1.5cm, thick, font=\Large},
	every node/.style={font=\Large, align=center}
]

\node[state] (M) [] {M};
\node[state] (S) [right=of M] {S};
\node[state] (I) at ($(M)!0.5!(S) + (0,-8cm)$) {I};
   
\path[->, very thick] 
	(M) edge[loop left] node {PrRd / -\\PrWr/-} (M)
	    edge[bend left=15] node[swap] {BusRd/Flush} (S)
	    edge[bend left=15] node[yshift=17pt, xshift=-9pt] {BusRdX/Flush} (I) 
	
	(I) edge[bend right=15] node[swap] {PrRd/BusRd} (S)
	    edge[bend left=15] node {PrWr/BusRdX} (M)
	    edge[loop below] node {BusRd/-\\BusRdX/-\\BusUpgr/-} (I)
	
	(S) edge[loop right] node[swap] {PrRd/-\\BusRd/-} (S)
	    edge[bend left=15] node[swap] {PrWr/BusUpgr} (M)
	    edge[bend right=15] node[swap, yshift=-30pt, xshift=-10pt] {BusRdX/-\\BusUpgr/-} (I)
	
	
;
\end{tikzpicture}
\end{document}
```

## Example Problem
| Access | C1 State | C2 State | C3 State | Bus Request | Data source |
| ------ | -------- | -------- | -------- | ----------- | ----------- |
|        | I        | I        | I        |             |             |
| R1     | S        | I        | I        | BusRd       | Mem         |
| W1     | M        | I        | I        | BusUpgr     |             |
| R3     | S        | I        | S        | BusRd       | C1          |
| W3     | I        | I        | M        | BusUpgr     |             |
| R1     | S        | I        | S        | BusRd       | C3          |
| R3     | S        | I        | S        |             |             |
| R2     | S        | S        | S        | BusRd       | Mem         |
## Other Optimizations
- Invalidate M block on BusRd
	- If a new reader is likely to write soon, this saves a BusRdX transaction
	- Reader detects Flush response, moves to M instead of S
	- Benefit depends on application behavior
		- If operations like += are common
- On a read miss likely to be followed by write, issue BusRdX instead of BusRd
	- Same effect as before, but initiated by reader
## MSI Problems
- Read-write requires 2 bus transactions
	- First BusRd to get line
	- Next, do a BusUpgr to tell other caches that the write has occurred
		- If none of the other caches have this block, then this busupgr is useless.
		- E state in MESI solves this
- Only supports clean sharing
	- Cache-cache transfers only occur when one cache line is in the M state
	- When cache lines are shared, they must all be valid in memory
# MESI Protocol
- Most popular
- Each processor has a private cache
- Write-back, write-allocate
- Adds an Exclusive state, which allows silent upgrade from clean to dirty
## MESI States
- Modified: Only one copy, dirty – R/W permission
- Exclusive: Only one copy, clean – R/W permission
- Shared: Clean, maybe other copies – R permission
- Invalid: Not in cache

## MESI Bus Actions
- BusRd: Request a block for reading only
- BusRdX: Request a block for reading and writing (exclusive)
- Flush: Respond by sending data to another cache that requested it and to memory
- FlushOpt: Respond by sending data to another cache, but not to memory
	- Opt stands for optional, because it's not needed for correctness
		- The protocol works just fine without the FlushOpt transaction
	- Flush occurs when memory does not have the up to date copy of the cache line. FlushOpt is only used to avoid a memory transaction
	- Opt can also stand for optimized, only there to make the protocol faster
### C/S signal
- On a read miss, we need other caches to signal (C or !C) whether there is a cached copy
- This is similar, but separate from the DONE signal shown earlier
- In M, E, or S state, line should output C=1
- In I state, line should output C=0
### What if multiple caches in the S State?
- Every cache will try to issue a FlushOpt (add to queue)
- Once one is issued, other requests need to be removed from queues
## MESI FSM
![[Pasted image 20260223164925.png]]
![[Pasted image 20260223164602.png]]

| **State** | **Received Action** | Next State | **Response** | **C Output** |
| --------- | ------------------- | ---------- | ------------ | ------------ |
| **M**     | PrRd                | M          | -            | 1            |
|           | PrWr                | M          | -            |              |
|           | BusRd               | S          | Flush        |              |
|           | BusRdX              | I          | Flush(X)     |              |
| **E**     | PrRd                | E          | -            | 1            |
|           | PrWr                | M          | -            |              |
|           | BusRd               | S          | FlushOpt     |              |
|           | BusRdX              | I          | FlushOpt     |              |
| **S**     | PrRd                | S          | -            | 1            |
|           | PrWr                | M          | BusUpgr      |              |
|           | BusRd               | S          | FlushOpt     |              |
|           | BusRdX              | I          | FlushOpt     |              |
|           | BusUpgr             | I          | -            |              |
| **I**     | PrRd (C)            | S          | BusRd        | 0            |
|           | PrRd (!C)           | E          | BusRd        |              |
|           | PrWr                | M          | BusRdX       |              |
|           | BusRd               | I          | -            |              |
|           | BusRdX              | I          | -            |              |
|           | BusUpgr             | I          | -            |              |

```tikz
\usetikzlibrary{automata, positioning, arrows.meta}
\begin{document}

\begin{tikzpicture}[
	node distance = 8cm,
	on grid,
	auto,
	state/.style={circle, draw, minimum size=1.5cm, thick, font=\Large},
	every node/.style={font=\Large, align=center}
]
    \node[state] (M) {M};
    \node[state] (E) [right=of M] {E};
    \node[state] (S) [below=of E] {S};
    \node[state] (I) [below=of M] {I};

    \path[->, very thick]
        (M) edge[loop left] node {PrRd / - \\ PrWr / -} (M)
        (E) edge[loop right] node {PrRd / -} (E)
        (E) edge[bend right=20] node[above] {PrWr / -} (M)
        (S) edge[loop right] node {PrRd / -} (S)
        (S) edge[bend left=15] node[pos=0.4, sloped, above] {PrWr / BusUpgr} (M)
        (I) edge[bend left=25] node[left] {PrWr / BusRdX} (M)
        (I) edge[bend left=25] node[pos=0.7, sloped, above] {PrRd(!C) / BusRd} (E)
        (I) edge[bend right=10] node[below] {PrRd(C) / BusRd} (S);
\end{tikzpicture}

\vspace{3cm}

\end{document}
```

```tikz
\usetikzlibrary{automata, positioning, arrows.meta} \begin{document}
\begin{tikzpicture}[
	node distance = 8cm,
	on grid,
	auto,
	state/.style={circle, draw, minimum size=1.5cm, thick, font=\Large},
	every node/.style={font=\Large, align=center}
]
    \node[state] (M) {M};
    \node[state] (E) [right=of M] {E};
    \node[state] (S) [below=of E] {S};
    \node[state] (I) [below=of M] {I};

    \path[->, very thick]
        (M) edge[bend left=15] node[pos=0.3, sloped, above] {BusRd / Flush} (S)
        (M) edge[bend right=15] node[left] {BusRdX / Flush} (I)
        (E) edge[bend left=15] node[right] {BusRd / FlushOpt} (S)
        (E) edge[bend left=40] node[pos=0.2, sloped, above] {BusRdX / FlushOpt} (I)
        (S) edge[loop below] node {BusRd / FlushOpt} (S)
        (S) edge[bend left=25] node[above] {BusRdX / FlushOpt \\ BusUpgr / -} (I);
\end{tikzpicture}
\end{document}
```
```tikz

```

## Memory Perspective
- Responds with data to some BudRd/BusRdX requests
	- Use the C bit to decide, but this only works if FlushOpt is used
		- If C=1, don't respond
	- Can also wait to see Flush/FlushOpt response (timeout)
- Store data on all Flush responses
	- Flush only issued by M state, which means data is (likely) dirty
- Ignore FlushOpt responses

## Example Problem
| Access | C1 State | C2 State | C3 State | Bus Request | Data source      |
| ------ | -------- | -------- | -------- | ----------- | ---------------- |
|        | I        | I        | I        |             |                  |
| R1     | E        | I        | I        | BusRd       | Mem              |
| W1     | M        | I        | I        |             | -                |
| R3     | S        | I        | S        | BusRd       | C1 (Flush)       |
| W3     | I        | I        | M        | BusUpgr     | -                |
| R1     | S        | I        | S        | BusRd       | C3 (Flush)       |
| R3     | S        | I        | S        |             |                  |
| R2     | S        | S        | S        | BusRd       | C1/C3 (FlushOpt) |
## MESI Pros and Cons
- + Reduced bus bandwidth vs. write-through
- +Compared to MSI, allows for cache-to-cache transfer of clean data
- + Read-write requires only one bus transaction (Only if C=0)
- -Added Complexity
	- Extra state
	- Needs Snoop Result signal (C)
	- Need to avoid multiple FlushOpt
- - Only supports clean sharing
	- Sometimes, flushing dirty cache line doesn't need to go to memory
# MOESI Protocol
- Private, write-back, write-allocate cache
- Adds the Owner state, which allows **Dirty Sharing**
- Owned means the cached data is (possibly) different from memory's data
	- This cache has the responsibility for writing back the data when the line is evicted
	- Enter this state when an M cache line sees a BusRd
- The key feature is dirty sharing. Allows sharing of modified data between caches, only writing back to memory during invalidation
- There is no need for FlushOpt, because flush will never write to memory
## MOESI States
- Modified: (1 copy, dirty) – R/W
- Owned: (Maybe other copies, Maybe dirty) – R
- Exclusive: (1 copy, clean) – R/W
- Shared: (maybe other copies, clean) – R
	- If S sees a BusRd, it won't respond
	- The logic is that there is probably an owner (M or O) that will respond
	- If there aren't any, lost opportunity for cache-cache transfer
	- Tradeoff is no multiple flushopt race condition
	- This is a big simplification of the protocol, and the S->S cache sharing loss is less than the gain of dirty sharing
- Invalid: Not in cache

## MOESI FSM

| **State** | **Received Action** | Next State | **Response** | **C Output** |
| --------- | ------------------- | ---------- | ------------ | ------------ |
| **M**     | PrRd                | M          | -            | 1            |
|           | PrWr                | M          | -            |              |
|           | BusRd               | O          | Flush        |              |
|           | BusRdX              | I          | Flush        |              |
| **O**     | PrRd                | O          | -            | 1            |
|           | PrWr                | M          | BusUpgr      |              |
|           | BusRd               | O          | Flush        |              |
|           | BusRdX              | I          | Flush        |              |
|           | BusUpgr             | I          | -            |              |
| **E**     | PrRd                | E          | -            | 1            |
|           | PrWr                | M          | -            |              |
|           | BusRd               | S          | FlushOpt     |              |
|           | BusRdX              | I          | FlushOpt     |              |
| **S**     | PrRd                | S          | -            | C            |
|           | PrWr                | M          | BusUpgr      |              |
|           | BusRd               | S          | **-**        |              |
|           | BusRdX              | I          | -            |              |
|           | BusUpgr             | I          | -            |              |
| **I**     | PrRd (C)            | S          | BusRd        | 0            |
|           | PrRd (!C)           | E          | BusRd        |              |
|           | PrWr                | M          | BusRdX       |              |
|           | BusRd               | I          | -            |              |
|           | BusRdX              | I          | -            |              |
|           | BusUpgr             | I          | -            |              |



```tikz
\usetikzlibrary{automata, positioning, arrows.meta}
\begin{document}

\begin{tikzpicture}[
    node distance = 4.5cm,
    on grid,
    auto,
    >=Stealth,
    state/.style={circle, draw, minimum size=1.5cm, thick, font=\Large},
    every node/.style={font=\Large, align=center}
]
    \node[state] (M) {M};
    \node[state] (O) [below=of M] {O};
    \node[state] (E) [below=of O] {E};
    \node[state] (S) [below=of E] {S};
    \node[state] (I) [below=of S] {I};

    % Left side (Processor) - Paths go UP
    \path[->, very thick]
        % Tight loops pushed slightly up/down to dodge horizontal spans
        (M) edge[out=155, in=205, looseness=5] node[left] {PrRd/-\\PrWr/-} (M)
        (O) edge[out=155, in=205, looseness=5] node[left] {PrRd/-} (O)
        (E) edge[out=155, in=205, looseness=5] node[left] {PrRd/-} (E)
        (S) edge[out=155, in=205, looseness=5] node[left] {PrRd/-} (S)
        
        % Cascading labels along the massive arcs (staggered vertically)
        (I) edge[bend left=105] node[left, pos=0.15] {PrWr/\\BusRdX} (M)
        (S) edge[bend left=80]  node[left, pos=0.25] {PrWr/\\BusUpgr} (M)
        (E) edge[bend left=55]  node[left, pos=0.35] {PrWr/-} (M)
        (O) edge[bend left=30]  node[left, pos=0.5]  {PrWr/\\BusUpgr} (M)
        
        % Inner lower arcs tucked beneath
        (I) edge[bend left=60]  node[left, pos=0.75] {PrRd(!C)/\\BusRd} (E)
        (I) edge[bend left=30]  node[left, pos=0.5]  {PrRd(C)/\\BusRd} (S);

    % Right side (Bus) - Paths go DOWN
    \path[->, very thick, dashed]
        % Tight loops pushed slightly up/down
        (O) edge[out=25, in=335, looseness=5] node[right] {BusRd/\\FlushOpt} (O)
        (S) edge[out=25, in=335, looseness=5] node[right] {BusRd/-} (S)
        
        % Cascading labels along the massive arcs (staggered vertically)
        (M) edge[bend left=105] node[right, pos=0.15] {BusRdX/\\Flush} (I)
        (O) edge[bend left=80]  node[right, pos=0.25] {BusRdX/\\Flush} (I)
        (E) edge[bend left=55]  node[right, pos=0.35] {BusRdX/\\FlushOpt} (I)
        
        % Inner mid/upper arcs tucked beneath
        (M) edge[bend left=30]  node[right, pos=0.5] {BusRd/\\FlushOpt} (O)
        (E) edge[bend left=35]  node[right, pos=0.5] {BusRd/\\FlushOpt} (S)
        (S) edge[bend left=30]  node[right, pos=0.5] {BusRdX/-\\BusUpgr/-} (I);

    \node[anchor=north] at ([yshift=2.5cm]M.north) {\textbf{Processor (Left)} \quad \textbf{Bus (Right)}};
\end{tikzpicture}

\end{document}
```
![[Pasted image 20260223190508.png]]
## Memory Perspective
- Responds with data to some BusRd/BusRdX Requests
	- Cannot use C bit alone to decide
		- If C=1 but all in S state, cache will not respond
	- Must wait to see if a Flush response is issued
- Store data only for writeback
- Ignore Flush responses
## Example Problem
| Access | C1 State | C2 State | C3 State | Bus Request | Data source |
| ------ | -------- | -------- | -------- | ----------- | ----------- |
|        | I        | I        | I        |             |             |
| R1     | E        | I        | I        | BusRd       | Mem         |
| W1     | M        | I        | I        |             |             |
| R3     | O        | I        | S        | BusRd       | C1          |
| W3     | I        | I        | M        | BusUpgr     |             |
| R1     | S        | I        | O        | BusRd       | C3          |
| R3     | S        | I        | O        |             |             |
| R2     | S        | S        | O        | BusRd       | C3          |
## MOESI Pros and Cons
- + Reduces memory usage by allowing dirty sharing
- - Added complexity
	- Extra state
- S state can't flushopt
- Ownership lost on eviction
	- Could transfer ownership instead
# Dragon: An Update Protocol
- Private, write-back, write-allocate
- Instead of **Invalidating** other copies on a write, shared copies are **Updated** with new data
- The cache will only respond when memory is stale; when the cache has newer data
## Bus Transactions
- PrRd, PrRdMiss
- PrWr, PrWrMiss
	- There are separate miss requests because there is no I state
- BusRd: Request block for reading
- BusUpd: Request – send **one word** of data to other caches
- Flush: Response – send **block** to another cache that requested it
## Dragon States
- M: Modified (one copy, likely dirty) – R/W
	- Exclusive owner
- E: Exclusive (1 copy, clean) – R/W
- Sc aka S: Shared Clean – R/W
- Sm aka O: (owner) R/W 
	- Shared owner
	- Only one cache can be in Sm, but others can be in Sc
	- Here, ownership just means responsibility to update memory
	- Only owners can respond to BusRds
- There is no I state because data is not invalidated through coherence actions

| **State** | **Received Action** | Next State | **Response** |
| --------- | ------------------- | ---------- | ------------ |
| M         | PrRd                | M          |              |
|           | PrWr                | M          |              |
|           | BusRd               | Sm         | Flush        |
| **E**     | PrRd                | E          |              |
|           | PrWr                | M          |              |
|           | BusRd               | Sc         |              |
| **Sc**    | PrRd                | Sc         |              |
|           | PrWr (C)            | Sm         | BusUpd       |
|           | PrWr (!C)           | M          | BusUpd       |
|           | BusRd               | Sc         |              |
|           | BusUpd              | Sc         | Update       |
| Sm        | PrRd                | Sm         |              |
|           | PrWr (C)            | Sm         | BusUpd       |
|           | PrWr (!C)           | M          | BusUpd       |
|           | BusRd               | Sm         | Flush        |
|           | BusUpd              | Sc         | Update       |
| Start     | PrRdMiss (C)        | Sc         | BusRd        |
|           | PrRdMiss (!C)       | E          | BusRd        |
|           | PrWrMiss (C)        | Sm         | BusRd;BusUpd |
|           | PrWrMiss (!C)       | M          | BusRd        |
|           |                     |            |              |

## Example Problem

| Access | C1 State | C2 State | C3 State | Bus Request | Data source |
| ------ | -------- | -------- | -------- | ----------- | ----------- |
|        | I        | I        | I        |             |             |
| R1     | E        | I        | I        | BusRd       | Mem         |
| W1     | M        | I        | I        |             |             |
| R3     | Sm       | I        | Sc       | BusRd       | C1          |
| W3     | Sc       | I        | Sm       | BusUpd      | C3          |
| R1     | Sc       | I        | Sm       |             |             |
| R3     | Sc       | I        | Sm       |             |             |
| R2     | Sc       | Sc       | Sm       | BusRd       | C3          |

## Dragon Pros and Cons
- + Avoids coherence misses
	- May keep shared data in cache for longer
- - Increased bus traffic, especially for blocks that remain in the cache (but are not used) for long periods
	- Because of updates
- - Can complicate memory consistency
	- Have to be careful about out-of-order updates
- - A processor write miss causes 2 bus transactions
	- BusRd, then BusUpd

For class #parallel-arch