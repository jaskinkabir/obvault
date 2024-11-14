Jaskin Kabir 801186717
## Problem 1: BST Find()
### 1.Problem description
Search through a Binary Search Tree for a certain key. If it is present, return its value. Otherwise, return an empty string
### 2.Initial solution description
My initial intuition was to iterate through the tree until a leaf is reached. At each node, if the key is greater than the search key, move to the right child. If less than the search key, move to the left child. If it is equal, return the value. If a leaf is reached, return an empty string
### 3.AI prompts used
None
### 4.Code explanation. Emphasize high level intuition (include code)
This code implements the iterative algorithm described above. It starts at  the root, and progresses through the nodes according to a comparison with the current node's key and the search key. When it reaches a nullptr, it returns an empty string. If the key is found before this, it will return the found value.
```cpp
std::string BinarySearchTree::find(int key) const {
// Your code here

    Node* curNode = root;
    int curKey;
    std::string curVal;
    
    while (curNode != nullptr) {
        curKey = curNode->key;
        curVal = curNode->val;
        
        if (curKey == key) return curVal;
        if (curKey > key) curNode = curNode->left;
        if (curKey < key) curNode = curNode->right;
    }
    
    return "";
}
```


### 5.Code testing (Include test code)
The following code was used to test the algorithm
```cpp
int main()
{  
   BinarySearchTree t;
   t.insert(5, "Boron");
   t.insert(3, "Lithium");
   t.insert(7, "Nitrogen");
   t.insert(2, "Helium");
   t.insert(4, "Berylium");
   t.insert(6, "Carbon");
   t.insert(8, "Oxygen");
   t.printInOrder(); // Prints the keys in order (will appear sorted)
   int ele = 8;
   std::string val = t.find(ele);
   if (val == "" ) {
	   std::cout << ele << " does not exist in tree" << std::endl;
   } else {
	   std::cout << ele << " : " << val << std::endl;
   }
   ele = 0;
   val = t.find(ele);
   if (val == "" ) {
	   std::cout << ele << " does not exist in tree" << std::endl;
   } else {
	   std::cout << ele << " : " << val << std::endl;
   }
    return 0;
}
   

```
It produced the following result, which is expected.
![[Pasted image 20240618201048.png]]
### 6.Alternate solutions if attempted

## Problem 2: sortedArrayToBST
### 1.Problem description
Given a sorted array of integers, return the root node of a balanced Binary Search Tree. This means that for every node, the difference in height between its two subtrees can be no greater than 1. In other words, each level of the tree must be full before another level is populated.
### 2.Initial solution description
My intuition was to find the median of the list, and then set this value as the root. Then iterate over the list from both sides of the median, adding the numbers left of the median to the left child of the last added node until the beginning of the list is reached. Then do the same on the right. This would result in two sorted linked lists attached to one root node. After reading more about what a balanced BST is, I realized that this was not a balanced BST, as only the root node has two subtrees of equal height and no other node has that property.

To fix this, I switched to a recursive approach. I realized that the first step of my initial solution could be applied recursively to each subtree formed by the left and right lists. The procedure would be to find the median of the list, break the list into two halves centered around the median, and then attach these two halves to the left and right children of the root node, whose value is the median of this list. This algorithm in my mind was visualized by bending each side of the list in half, and reattaching the middle up to the root node. 
### 3.AI prompts used
None
### 4. Code explanation. Emphasize high level intuition (include code)
The code below implements the recursive algorithm described above. In the base case the list is empty, which would result in returning a null tree. The list would be empty if at any point the helper function receives a starting index greater than the end index. In the recursive case, the left and right subtrees should be the bent forms of the left and right halves of the list formed by breaking the full list around the median. 
```cpp
TreeNode * sortHelper(vector<int>& nums, int start, int end) {
    if (start > end) return nullptr;

    int medianIndex = (start+end)/2;
    
    
    TreeNode * root = new TreeNode(nums[medianIndex]);
    
    root->left = sortHelper(nums, start,medianIndex-1);
    root->right = sortHelper(nums, medianIndex+1,end);
    
    return root;


}
TreeNode* sortedArrayToBST(vector<int>& nums) {
    int n = nums.size()-1;

    return sortHelper(nums, 0, n);
}
```
### 5.Code testing (Include test code)
The leetcode website was used to test this code. 
![[Pasted image 20240618205407.png]]
### 6.Alternate solutions if attempted
```cpp
TreeNode* sortedArrayToBST(vector<int>& nums) {
    int medInd = int(nums.size()/2)+1;
    
    TreeNode * root = new TreeNode(nums[medInd]);
    
    TreeNode * curNode = root;
    
    for (int i = medInd+1; i < nums.size(); i++) {
        TreeNode * newNode = new TreeNode(nums[i]);
        curNode->right = newNode;
        curNode = newNode;
        
    }
    
    for (int i = 0; i < medInd; i++) {
        TreeNode * newNode = new TreeNode(nums[i]);
        curNode->right = newNode;
        curNode->left = newNode;
        curNode = newNode;
    }
    
    return root;
}
```
Resulted in two linked lists

For class #data-structures 