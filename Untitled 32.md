S0 Idle
S1 go to pickup
S2 go to goal

Variable holds the current path being traversed
Variables also hold GOAL and PICKUP points

- S0
	- If PICKUP is given, transition to state S1
	- If GOAL is given, transition to state S2
- S1
	- If the current path ends at the PICKUP point, move one step along the path
	- Else, the pickup point has been changed, so pathfinding must be redone
	- Once PICKUP point is reached, transition to S1
- S2
	- If the current path ends at the GOAL point, move one step along the path
	- Else, the GOAL point has been changed, so pathfinding must be redone
	- Once GOAL is reached transition to S0