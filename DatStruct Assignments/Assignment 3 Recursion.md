Jaskin Kabir 801186717
## Problem 1: Recursive Palindrome Detection
### 1.Problem description
Determine if a string is a palindrome using a recursive function
### 2.Initial solution description
Determine if the first and last letters are the same. If so, determine if the second and second to last characters are the same, and so on. If the two characters are not the same, the string cannot be a palindrome. Continue until the string cannot be broken up anymore. If the string has reached this point, it is a palindrome. 
### 3.AI prompts used
None
### 4.Code explanation. Emphasize high level intuition (include code)

```C++
bool isPalinHelper(std::string& s, int begin, int end) {

    if (s[begin] == s[end]) {
        
        if (end-begin==1 || end==begin) return true;
        
        isPalinHelper(s, begin+1, end-1);
    }
    else return false;
    
}
```

The function first checks if the first and last characters of the substring are equal. If not, the string is not a palindrome and returning false ends execution. Otherwise, check if the string can be reduced any further. If the difference between the begin and end indices is at most 1, this means the string cannot be split any further, and the string is a palindrome. Otherwise, reduce the end index and increase the begin index.
### 5.Code testing (Include test code)
```C++
int main() {
	std::string s1{"racecar"}; // Palindrome
	if (isPalin(s1)) std::cout << s1 << " is a palindrome" << std::endl;
	else std::cout << s1 << " is not a palindrome" << std:: endl;
	std::string s2{"racecars"}; // Not a palindrome
	if (isPalin(s2)) std::cout << s2 << " is a palindrome" << std::endl;
	else std::cout << s2 << " is not a palindrome" << std:: endl;
	std::string s3{"gohangasalamiimalasagnahog"};
	if (isPalin(s3)) std::cout << s3 << " is a palindrome" << std::endl;
	else std::cout << s3 << " is not a palindrome" << std:: endl;
	
}
```
This produced the following expected output
![[Pasted image 20240528224940.png]]
### 6.Alternate solutions if attempted
This only worked for strings of an even number length
```C++
bool isPalinHelper(std::string& s, int begin, int end) {

    if (s[begin] == s[end]) {
        
        if (end-begin==1) return true;
        
        isPalinHelper(s, begin+1, end-1);
    }
    else return false;
    
}
```

## Problem 2: Recursive Binary Search
### 1.Problem description
Given a sorted array and a number to find, use a recursive implementation of the binary search algorithm to find the index where that number can be found. If it is not in the array, return -1.
### 2.Initial solution description
The base case for this algorithm is when the size of the array is either 2 or 0 elements long. In the case of 2 elements, if either element is the number to be searched for, return the corresponding index. Otherwise, return -1. In the case of 0 elements, the number was not found, so return -1. 

To reduce the array to the base case, check if the middle element of the array is greater than or less than the search number. If it is equal, return this index. If it is less, recall the function on the lower half of the array. If larger, the higher half. 
### 3.AI prompts used
None
### 4.Code explanation. Emphasize high level intuition (include code)
```C++
int binSearchHelper(std::vector<int> vec, int num, int start, int end) {
    int index = (start + end) / 2;
    if (vec[index] == num) return index;
    
    if (end-start == 1) {
        if (num==vec[start]) return start;
        else if (num==vec[end]) return end;
        else return -1;
    }
    
    if (start > end) return -1;
    
    if (num < vec[index]) return binSearchHelper(vec, num, start, index-1);
    else return binSearchHelper(vec, num, index+1, end);
}

int binSearch(std::vector<int> vec, int num) {
    return binSearchHelper(vec,num, 0, vec.size());
}
```
The code implements exactly what is described in section 2. Checking for an empty array however involves checking if the start index is greater than the end index. This would occur if the splitting step of the last iteration sliced the ending index backwards behind the start, or the starting index forwards ahead of the end. Using start > end rather than start == end handles the condition of a single element array.
### 5.Code testing (Include test code)
```C++
int main()
{
    
    std::vector<int> v1 = {1,3,5,8,13,21,34};
    std::cout << binSearch(v1,8);
    std::cout << ',' << binSearch(v1,2);
    std::cout << ',' << binSearch(v1,34);
    
    std::vector<int> v2 = {3};
    std::cout << ',' << binSearch(v2,3);
    std::cout << ',' << binSearch(v2,4);
    
    return 0;
}
```
![[Pasted image 20240528233040.png]]
This is the expected output.
### 6.Alternate solutions if attempted


For class #data-structures 