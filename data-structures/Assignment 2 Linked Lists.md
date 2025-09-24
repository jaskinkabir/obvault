Jaskin Kabir 801186717
## Problem 1: Linked List Concatenation
### 1.Problem description
Given three linked lists, make the third list a new linked list that is a concatenation of the first two. That is, the first list with its end connected to the head of the second.
### 2.Initial solution description
This initial solution explored was setting the head of the third list to the head of the first list. Then, the next node of the first list's end node is set to the head of the second list. The problem with this approach though, is that this connects the first two lists together, and does not leave them intact. To solve this, another approach must be used.

In this approach, a new linked list must be created by copying the first list into the third list, then copying the second list onto the end of the third list. This solves the problem completely, and keeps the input lists intact.
### 3.AI prompts used
None
### 4.Code explanation. Emphasize high level intuition (include code)
```C++
template <typename T>
void concat(SLinkedList<T>& l1, SLinkedList<T>& l2, SLinkedList<T>& lout) {
// Your code here
    if (l1.head == nullptr || l2.head == nullptr) return;
    
    SNode<T>* outNode = new SNode<T>();
    SNode<T>* nextOutNode;
    
    lout.head = outNode;
    
    SNode<T>* curNode = l1.head;
    for (int i = 0; i < 2; i++) { //Repeat twice
        while (curNode != nullptr) {
            outNode->elem = curNode->elem;
            nextOutNode = new SNode<T>();
            outNode->next = nextOutNode;
            outNode = nextOutNode;
        
            curNode = curNode->next;
        }
    curNode = l2.head;
    }
}
```
Firstly, the function need not run if either list is empty so it checks for this condition. Next, a new empty node object is created, and the head of the output list is set to this object. Then, the program iterates over all elements of the first list and then the second. At each step, it sets the element of the current output node to its corresponding element from the original two lists, and points its next pointer to a newly instantiated empty Node object. On the next iteration, this empty node is populated with its corresponding element. 
### 5.Code testing (Include test code)
I first added a print method to the linked list 
```C++
    void print() {
        SNode<T>* n=head;
        while (n != nullptr){
            std::cout<< n->elem << " ";
            n = n->next;
        }   
}
```
Then, I altered the given test code to print the contents of p1 at the end to show that it was left intact.
```C++
template<typename T>
void println(T msg) {
    std::cout << msg << std::endl;
}

int main() {
	SLinkedList<std::string> p1;
	SLinkedList<std::string> p2;
	SLinkedList<std::string> p3;
	// Add elements
	p1.addBack("C");
	p1.addBack("C++");
	p1.addBack("Java");
	p1.addBack("Python");
	p1.addBack("Javascript");

	p2.addBack("Go");
	p2.addBack("Rust");
	p2.addBack("Julia");

	// Concatenate the progLangsNew list to the end of progrLangs list
	concat(p1,p2,p3);

	// Print the concantenated list by repeatedly removing from list
	while (!p3.empty()) { // Should print C C++ Java Python Javascript Go Rust Julia 

		std::cout << p3.front() << " ";
		p3.removeFront(); 
	}
	std::cout << std::endl;
	println("p1: ");
	p1.print();
}
```
This produced the following output, which is the expected output.
![[Pasted image 20240528204138.png]]
### 6.Alternate solutions if attempted
This is the implementation of the naïve solution initially explored. 
```C++ 
template <typename T>
void concat(SLinkedList<T>& l1, SLinkedList<T>& l2, SLinkedList<T>& lout) {
// Your code here
    lout.head=l1.head;
    SNode<T>* l1Back = l1.head;
    while (l1Back->next != nullptr) l1Back= l1Back->next;
    
    l1Back->next = l2.head;

}
```

## Problem 2: Merge Two Sorted Lists 
### 1.Problem description
Given two sorted singly linked lists, create a function that merges them together while keeping the sorting intact
### 2.Initial solution description
Since the two lists are sorted, the lowest value of the final list will be the lower of the two head values. This means the algorithm can simply iterate through both lists at the same time, without worrying about backtracking to insert a low element into the merged list.

The solution to this problem first finds this lowest value and sets the merged head to it. Then, it iterates over both lists, only moving the iterator forward on a list once it has been shown that the current node in that list is less than or equal to the current node of the other list. If this happens, the lower value will be appended to the merged list.

This loop will end when one of the lists has been iterated through completely. At this point, the other list will be appended to the merged list.
### 3.AI prompts used
None
### 4.Code explanation. Emphasize high level intuition (include code)
```C++
ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
    if (list1 == nullptr) return list2;
    if (list2 == nullptr) return list1;
    else return nullptr;
    
    ListNode* newHead = nullptr;
    ListNode* tail = nullptr;
    
    if (list1->val <= list2->val) {
        newHead = list1;
        list1 = list1->next;
    }
    else {
        newHead = list2;
        list2 = list2->next;
    }
    
    tail = newHead;
    
    while (1) {
        if (list1 == nullptr) {
            tail->next = list2;
            break;
        }
        if (list2 == nullptr) {
            tail->next = list1;
            break;
        }
        
        if (list1->val <= list2->val) {
            tail->next = list1;
            list1 = list1->next;
        }
        else {
            tail->next = list2;
            list2 = list2->next;
        }
        tail = tail->next;
    }
    
    return newHead;
}
```
The function first checks for empty lists, and then declares the new head pointer and a tail pointer. It then finds which of the two heads should be the new head by finding the lower of the two, and it pushes both iterators forward. Next, the while loop iterates over both lists at the same time.

If the iterator of either list is a null pointer, the other list must be appended onto the tail of the new list, and the new head is returned, ending execution. If one of the lists has the lower value at the current iteration step, this node is added onto the tail and the list's iterator is moved forward. 
### 5.Code testing (Include test code)

The following test code was used
```C++
void printList(ListNode* list) {
    ListNode* curNode = list;
    while (curNode != nullptr) {
        std::cout << curNode->val << " ";
        curNode = curNode->next;
        
    }
    std::cout << std::endl;
}

int main() {
    
    ListNode* n4 = new ListNode(4);
    ListNode* n3 = new ListNode(3, n4);
    ListNode* n2 = new ListNode(2, n3);
    ListNode* l1 = new ListNode(1, n2);
    
    printList(l1);
    ListNode* i6 = new ListNode(6);
    ListNode* i5 = new ListNode(5, i6);
    ListNode* i4 = new ListNode(4, i5);
    ListNode* l2 = new ListNode(2, i4);
    
    printList(l2);
    
    ListNode* l3 = mergeTwoLists(l1,l2);
    printList(l3);
    
    return 0;
    
}
```
And it produced the expected output:
![[Pasted image 20240528222553.png]]
The leetcode testing tool also verified this solution
![[Pasted image 20240528222730.png]]
### 6.Alternate solutions if attempted
Initially, the check for the iterator pointing to a null pointer was the second step of the while loop. This meant that for lists of length 1, the call to the next node in the list resulted in an error. This is why the final code has these steps reversed.

For class #data-structures 