Jaskin Kabir 801186717
## Problem 1: Valid Anagrams
### 1.Problem description
Given two strings, determine if the strings are anagrams. In other words, that the strings contain the same letters in the same amounts. The algorithm must be O(n)
### 2.Initial solution description
An unordered map could be used for this problem. By walking over the two strings and adding each character to the unordered map as a key with its value being the number of times it has appeared in the string, I could check if the same letters were used the same number of times. Initially, my solution was to try to count the collisions when trying to add letters to the map, and if the number of collisions equaled the number of characters in the strings, return true. However, this failed when used on strings that had repeated characters. The solution was then reworked to account for repeated characters by decrementing the frequency value of a key if it is greater than one. However, this too failed on test case 46 from leetcode.

To solve this, the solution was reworked to simply count the number of times each letter appears in the first string, and then subtract from that count while iterating over the second string. If any characters in the second string do not appear in the first string, or if they appear more often than they do in the first string, their frequency will be negative. If they appear less frequently, their frequency will be positive. 

After this loop is completed, the function can iterate over the map and return false if any of the frequency values is not 0. Otherwise, return True
### 3.AI prompts used
None
### 4.Code explanation. Emphasize high level intuition (include code)

```cpp
bool isAnagrams(string s, string t) {
    unordered_map<char, int> map;

    for (char c : s) map[c]++;
    for (char c : t) map[c]--;

    for (auto i = map.begin(); i != map.end(); i++) if (i->second) return false;

    return true;
}
```
This code implements the algorithm described above. This is an O(n) algorithm, where n is the length of the strings, because the first loop performs n operations of constant time, these operations are finding a node in an unordered map, and incrementing its value. The next loop does the same, except it decrements the values.

The worst case of the final loop is when the two strings are anagrams with letters that are all only used once. In this case, the loop will perform n comparison operations, which require constant time.

Thus, in the worst case, this algorithm's time complexity is O(n)
### 5.Code testing (Include test code)

For debugging, the following code was used.
```cpp
int main() {  
string s = "anagram";  
string t = "nagaram";  
if (isAnagram(s, t)) cout << "True" << endl;  
else cout << "False" << endl;  
s = "rat";  
t = "car";  
if (isAnagram(s, t)) cout << "True" << endl;  
else cout << "False" << endl;  
}
```
For rigorous testing, the code was pasted into leetcode and achieved the following result. 

![[Pasted image 20240611201200.png]]
### 6.Alternate solutions if attempted
```cpp
bool isAnagram(string s, string t) {
    unordered_map<char, int> map;
    int numCollisions = 0;
    char c;
    
    int len = s.length();
    
    for (char c : s) {
        if (map.find(c) != map.end() ) numCollisions++;
        map[c]++;
    }
    cout << numCollisions << endl;
    
    for (char c : t) {
        if ( map.find(c) == map.end() ) return false;
        if (map[c]>1) {
            
            map[c]--;
        }
        else{
            numCollisions++;
        }
    }

    
    return numCollisions == len;
}
```
This failed with the inputs ''aacc" and ""ccac"
## Problem 2: Linked List Cycle
### 1.Problem description
Given the head of a linked list, return true if the list has a cycle. In other words, if continuously following the next pointer to the next node results in an infinite loop, return true. 
### 2.Initial solution description
I thought a hash map would easily solve this problem. Iterate through the list by continuously following the next pointer. At each node, add the node to the map. If any collision occurs, there is a loop so return true. If NULL is reached, return false. 
### 3.AI prompts used
Is this a good hashing function if I want to make an unordered map with nodes as keys? 
```cpp
struct NodeHasher { size_t operator()(const Node* n) const { 
		int val = n->val; 
		int nextVal = 0; 
		if (n->next != NULL) nextVal=n->next->val; 
		int i = 0; 
		while (n->next != NULL) { i++; n = n->next; }
 		return std::hash<int>(i) ^ std::hash<int>(val) ^ std::hash<int>(nextVal); 
	} 
};
```

ChatGPT pointed out that traversing the list to find the number of nodes between it and the end was unnecessary, and collision could still be avoided without this step. In retrospect, this would have resulted in an infinite loop anyway.
### 4.Code explanation. Emphasize high level intuition (include code)
```cpp
struct NodeHasher {
    size_t operator()(const ListNode* n) const {
        int val = n->val;
        int nextVal = n->next ? n->next->val : 0;
        
        size_t hash1 = std::hash<int>()(val);
        size_t hash2 = std::hash<int>()(nextVal);
        
        return hash1 ^ (hash2 << 1); 
    }
};

bool hasCycle(ListNode *head) {
    
    std::unordered_map<ListNode *, int, NodeHasher> nodeMap;
    
    
    while (head != NULL) {
        if (nodeMap.find(head) != nodeMap.end() ) return true;
        
        nodeMap[head] = head->val;
        head = head->next;
    }
    
    return false;
}
```

A custom hashing function had to be implemented to use nodes as keys in the unordered map. I considered simply using the value, but the problem description was unclear as to whether two nodes could have the same value, so I erred on the side of caution. The hashing function uses the current value and the next value, if there are such values, to calculate the hash.

This code implements the algorithm described above. Where n is the number of nodes in the list, this program is of O(n) time complexity. Iteration through the list would result in n iterations in the worst case. Within the iteration loop, all operations are of constant time complexity, thanks to the use of the unordered map. Thus, the algorithm is O(n).
### 5.Code testing (Include test code)
```cpp


void addNode(ListNode * list, int val) {
    while (list->next != NULL) list = list->next;
    list->next = new ListNode(val);
    
    
}

void addLink(ListNode *list, int end) {
    if (list == NULL) return; // Check for empty list
    
    int i = 0;
    ListNode *startNode = NULL;
    ListNode *endNode = NULL;
    
    while (list != NULL) {
        if (list ->next == NULL) {
            startNode = list;
        }
        else if (i == end) {
            endNode = list;
        }
        
        i++;
        list = list->next;
    }
    
    if (startNode != NULL && endNode != NULL) {
        startNode->next = endNode;
    } else {
        std::cout << "Invalid index" << std::endl;
    }
}

void printList(ListNode *list) {
    while (list != NULL) {
        std::cout << list->val << " ";
        list = list->next;
    }
    std::cout << std::endl;
}


int main() {
    //[3,2,0,-4]
    ListNode* l1 = new ListNode(3);
    addNode(l1, 2);
    addNode(l1, 0);
    addNode(l1, -4);
    
    printList(l1);
    
    addLink(l1,1);
    printList(l1);
    
    std::cout << hasCycle(l1);
    
}
```

I used the above code for testing. I created a function to create loops in the list to construct the looped lists to save myself from writing too much testing code.

For rigorous testing, I used leetcode which gave me the following result:
![[Pasted image 20240611203639.png]]
### 6.Alternate solutions if attempted

For class #data-structures 