Jaskin Kabir 801186717
Uses [[Trees]]
## Problem 1: Tree Height
### 1.Problem description
Given the root node of a tree, determine the maximum length of the path between it and any of its leaves. In other words, determine the height of the tree.
### 2.Initial solution description
A recursive algorithm can be used here. A tree that has no nodes at all has a height of 0, and the height of any tree is the maximum between the heights of its left and right subtrees + 1 to account for its own contribution to the height. Taking these two cases to the base and recursive cases, a simple recursive function can be created.
### 3.AI prompts used
None
### 4.Code explanation. Emphasize high level intuition (include code)
```cpp
int treeHeight(TreeNode *p) {

    if (p == NULL) return 0; // Handle null tree base case
    
    int l = treeHeight(p->left);
    int r = treeHeight(p->right);
    
    return 1 + std::max(l,r);

}
```
This implements the recursive algorithm described above. It reduces the size of the problem by one upon each recursion until the subtree consists of 0 nodes, upon which the number 0 can be returned up the chain of function calls.
### 5.Code testing (Include test code)
The following code was used for debugging, but rigorous testing was performed using leetcode.
```cpp
int treeHeight(TreeNode *p) {
// Your code here

    if (p == NULL) return 0; // Handle null tree base case
    
    int l = treeHeight(p->left);
    int r = treeHeight(p->right);
    
    return 1 + std::max(l,r);

}
```
![[Pasted image 20240611204723.png]]
### 6.Alternate solutions if attempted

## Problem 2: Tree Symmetry

### 1.Problem description
A tree is symmetric if it can be mirrored about its center. In other words, if a number were to be constructed from the values at each level of the tree, each of these numbers would have to be a palindrome.
### 2.Initial solution description
Initially I considered using this palindrome approach, but I realized it would be too complicated to construct these numbers and then check if they are palindromes.

So I quickly switched to thinking about the problem recursively. I realized that in the base case, where the tree consists only of a root and 0, 1, or 2 child leaves, the tree is symmetric if it has no leaves or if it has two leaves of the same value. In the recursive case, a tree is symmetric if its two children are of the same value, the subtrees formed by its outer grandchildren are symmetric with respect to each other, and the subtrees formed by its inner grandchildren are symmetric with respect to each other.
### 3.AI prompts used
None
### 4.Code explanation. Emphasize high level intuition (include code)
```cpp
bool symmetricHelper(TreeNode * left, TreeNode * right) {

    if (!left && !right) return true;

    if (!left || !right) return false;

    if (left->val != right->val) return false;

    return symmetricHelper(left->left, right->right) && symmetricHelper(left->right, right->left);

}

  
  

bool isSymmetric(TreeNode* root) {

    if (!root) return true;

    return symmetricHelper(root->left, root->right);

}
```

In the base case of the root node being null, the function returns true as a null tree is symmetric. Otherwise, the function calls the symmetric recursion helper function on its two children so that it may then recursively check the symmetry of the trees formed by that root's grandchildren.
### 5.Code testing (Include test code)
The provided testing code was used in debugging, rigorous testing was done with leetcode:
```cpp
bool symmetricHelper(TreeNode * left, TreeNode * right) {

    if (!left && !right) return true;

    if (!left || !right) return false;

    if (left->val != right->val) return false;

    return symmetricHelper(left->left, right->right) && symmetricHelper(left->right, right->left);

}

  
  

bool isSymmetric(TreeNode* root) {

    if (!root) return true;

    return symmetricHelper(root->left, root->right);

}
```
![[Pasted image 20240611210148.png]]
### 6.Alternate solutions if attempted
None

For class #data-structures 