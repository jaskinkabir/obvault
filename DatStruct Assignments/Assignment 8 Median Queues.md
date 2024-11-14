Jaskin Kabir 801186717
## Problem 1: Median From Data Stream

### 1.Problem description
While receiving a list of integers one at a time, constantly calculate the median of the list.
### 2.Initial solution description

The median of a dataset divides the set into its smaller and larger halves. Thus, the median always lies between the maximum of the smaller half and the minimum of the larger half. A max heap could keep track of the smaller, or 'left' half and a min heap could keep track of the larger 'right' half. 

Each time a number is added to the list, first check if it is less than the maximum of the left half. If it is, push it to the left heap. Otherwise, push it to the right heap. 

In the case where the data set has a true median, which is when there are an odd number of elements, one heap will have one more element than the other. This extra element is the median, and the arbitrary decision was made to store it in the left heap. In the case where the median is the mean of the two middle numbers of the set, which occurs when the data set is even in length, the two heaps are equal in size.

Thus, to ensure that the two heaps are either equal in size, or that the left heap has just one more element than the right, the algorithm must compare the sizes of the two heaps and balance them as needed. If the left heap grows to be two elements bigger than the right heap, move maximum value of the left heap to the right heap. If the right heap grows to be bigger than the left, move the minimum value of the right heap to the left heap. 

Calculating the median is now made trivial. If the left heap is one element larger than the right heap, the median is the maximum value of the left heap. If the two heaps are equal in size, the median is the mean of the two heap's top values.
### 3.AI prompts used
None

### 4.Code explanation. Emphasize high level intuition (include code)
```cpp
class MedianFinder {
    std::priority_queue<int, std::vector<int>, std::greater<int> > rightHeap;
    std::priority_queue<int> leftHeap;
    
    double median;
    
public:

    int getSize() {return leftHeap.size() + rightHeap.size();}
    
    MedianFinder() {
        median = 0;
    }
    
    void addNum(int num) {
        
        if (leftHeap.empty() || num <= leftHeap.top()) leftHeap.push(num); //Handle intial empty case
        else rightHeap.push(num);
        
        
        if (leftHeap.size() > rightHeap.size()+1) {
            rightHeap.push(leftHeap.top());
            leftHeap.pop();
        }
        else if (rightHeap.size() > leftHeap.size()) {
            leftHeap.push(rightHeap.top());
            rightHeap.pop();
        }
        
        if (leftHeap.size() > rightHeap.size()) median = leftHeap.top();
        else median = (leftHeap.top()+rightHeap.top() )/2.0;
    }
    
    double findMedian() {
        return median;
    }
};
 

std::vector<double> findMedian(std::vector<int>& data) {
    
    MedianFinder mf;
    
	std::vector<double> res;
	
	for (int n : data) {
	    mf.addNum(n);
	    res.push_back(mf.findMedian());
	}
    
    return res;

}
```

To match the format of leetcode, the functionality was implemented as a custom MedianFinder class. The findMedian function creates an instance of this class and calls its addNum function and its findMedian function for each element of the data stream vector. 

The code implements the algorithm described above using STL's priority queue class to create the max and min heaps. The priority queue is a max heap by default, so the minheap had to be implemented as an adaptation of the STL vector data structure.
### 5.Code testing (Include test code)
The provided testing code was used for debugging, leetcode for rigorous testing:
```cpp
int main() {
	std::vector<int> data_stream = {5, 42, 29, 85, 95, 99, 2, 15};
    // i-th element of median_stream is median of first i elements of input 
	std::vector<double> median_stream = findMedian(data_stream) ;
    for (double ele: median_stream) {
		std::cout << ele << " "; // Answer should be: 5 23.5 29 35.5 42 63.5 42 35.5 
    }
	std::cout << std::endl;
}
```
![[Pasted image 20240611212226.png]]
### 6.Alternate solutions if attempted
None

For class #data-structures 