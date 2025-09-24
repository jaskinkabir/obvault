Related to [[Finite State Machines]]
# Explanation of Wordle
- A game where a 5-lette
- r word must be guessed by the player
- Upon each guess, the wordle puzzle will give the player this information about the word:
	- Characters marked as **Black** are not in the word in any position
	- Characters marked as **Green** are in the word and in the right position
	- Characters marked as **Yellow** are in the word but in the wrong position
- For example: The Wordle puzzle has chosen 'cater' as the correct answer and the player inputs 'creak' as their guess. The Wordle puzzle would tell the player:
	- 'c' is **Green** as c is the first letter of the correct word
	- 'r', 'e', and 'a' are **Yellow**, as these words appear in the correct word but are in the wrong positions
	- 'k' is **Black** because it does not appear in the correct word in any position
- This now cuts down the list of possible solutions from all 5-letter English words to a smaller list of 5-letter English words that have the following properties:
	- The word starts with 'c'
	- The 2nd character is not 'r'
	- The 3rd character is not 'e'
	- The 4th character is not 'a'
	- The word contains the letters 'r', 'e', and 'a'
	- The word does not contain the letter 'k'
- By guessing more words, the list can be further cut down by taking the new information provided by the puzzle into account until the correct answer is chosen
- The process of searching through the list of 5-letter English words and applying this pattern to find all possible solutions can be implemented on an FPGA using a state machine. 
- Because the pattern the state machine is matching changes upon each guess, the state machine must be able to be dynamically updated as the puzzle is being solved.
# Three Actors
- The system involves three actors: the Puzzle Master, the Middle Man, and the Solver
- The operation of the system follows this cycle of communication between the actors upon each guess:![[Pasted image 20241017132802.png]]
- The specific roles of these actors are as follows:
## Puzzle Master
- The Puzzle Master knows the correct answer, and will read the guess from the Middle Man and output the category that each letter of the guess falls into:
	- Green, Yellow or Black
- If the correct answer is guessed by the Middle Man, the Puzzle Master will reply with a message that every character is Green, which the Middle Man can recognize as the solution to the puzzle.
## Middle Man
- The Middle Man will hold all the letter category information given by the Puzzle Master since the first guess
- The Middle Man will also hold the list of possible solutions
	- Initially, this will be the list of all 5-letter English words
	- Each time the solver searches through the list to find possible solutions, the Middle Man will update its list of solutions.
- Upon each guess, it will use the previous information and the new information from the most recent guess to create a list of constraints that the Solver must use to find the list of possible solutions. These constraints are:
	- Which characters must be in certain position (Green characters)
	- Which characters cannot be in certain positions (Yellow characters)
	- Which characters must be in the word (Yellow characters)
	- Which characters cannot be in the word at all (Black characters)
- It will give these constraints and its previously stored list of solutions to the solver. Upon receiving the updated list of possible solutions, the Middle Man store this new list and then use some sort of prioritization function to choose the best answer to give to the Puzzle Master
## Solver
- This will be the state machine that reads the constraints given by the middle man and searches through the previously found list of possible solutions. It will narrow the list down based on the new constraints and then return this new list to the Middle Man


For topic #wordle-automata