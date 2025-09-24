# Lexing Scheme
- Different tokens are monkey noises
- We can add a pre-lexing step where monkey noises are replaced with single characters
# Integers
- The numbers 1-9 can be represented by repeating 'oh' the number of times of the represented quantity 
	- 1 = oh
	- 4 = ohohohoh
- To create numbers larger than 9, add the number separation token –'uh'– between repeated ohs 
	- Separation token is |
	- 412 is ohohohohuhohuhohoh
	- ohohohoh uh oh uh ohoh
	- Can also have 0 'oh's in between separation tokens
	- 101 = ohuhuhohah = 1||10
- End a number with the number termination token 'ah'
	- Termination token is 0
	- 412 is ohohohohuhohuhohohah
	- This termination token also allows 0 to be written as simply ah
- To represent negative numbers add the negation token 'ehuh' to the beginning of the number
	- This is just -
- Example: 1234
	- oh uh ohoh uh ohohoh uh ohohohoh ah
	- pre-lexed as 1|11|111|11110
- Regex:
	- Pattern is `^0$|^1+(?:1*\|*)+0$`
	- Optionally start with -
	- Followed 0 or more digits, which are defined as
		- Starts with 1-9 occurrences of '1' followed by an optional '|'
	- Ends with 0
# Non-Integer Numbers
- An integer followed by the decimal token 'eh' followed by another integer
- Example: 123.321:
	- oh uh ohoh uh ohohoh eh ohohoh uh ohoh uh oh ah
	- 1|11|111.111|11|10

For topic #MonkeyC