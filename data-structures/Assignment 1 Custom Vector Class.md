Jaskin Kabir 801186717
## Problem 1: Vector Product

### 1. Problem description

This assignment asks for a function that takes two equal length vectors of doubles as its arguments and returns an equal length vector of doubles that contains the element-wise products of the two vectors. As in, the ith element of the resulting vector will be the product of the ith element of the first and second vectors. If the two vectors given as arguments are of unequal length, the function should return an empty vector.

### 2. Initial solution description
The initial solution involves a guard clause that returns an empty vector if the two argument vectors are of unequal length. If they are equal in length, the program will iterate over each element of the two argument vectors, multiply them, and push their product back into the resultant vector. The resultant vector will then be returned.
### 3. AI prompts used

None
### 4. Code explanation. Emphasize high level intuition (include code)

```C++
std::vector<double> vecProduct(const std::vector<double>& v1, const

std::vector<double>& v2) {

// Your code here

// Return empty vector if v1 and v2 are of different sizes; 
    std::vector<double> res; 

    if (v1.size() != v2.size()) return res; 

    for (int i=0; i<v1.size(); i++) {
        res.push_back(v1.at(i) * v2.at(i));
    }

    return res;
}
```
The function will first declare the resultant vector as an empty vector of doubles. It will then check to see if the two argument vectors are of equal length. If they are not, the program will simply return the empty resultant vector. Otherwise, the function will enter a for loop to iterate over the elements of the vectors. At each iteration, the two values of the vectors will be multiplied, and the product pushed back to the resultant vector. Finally, the resultant vector will be returned.
### 5. Code testing (Include test code)
The following code was used to test the above solution.
```C++
#include <iostream>
#include <vector>
std::vector<double> vecProduct(const std::vector<double>& v1, const
std::vector<double>& v2) {
// Your code here
// Return empty vector if v1 and v2 are of different sizes;

    std::vector<double> res;

    if (v1.size() != v2.size()) return res;

    for (int i=0; i<v1.size(); i++) {
        res.push_back(v1.at(i) * v2.at(i));
    }
    
    return res;
}
// Overload << operator to print std::vector
std::ostream& operator <<(std::ostream& os, const std::vector<double>& v) {
for (int i = 0; i < v.size(); i++) {
os << v.at(i) << " ";
}
os << std::endl;
return os;
}
// Test
int main() {
// Test 1
std::vector<double> v1{1.0, 2.0, 3.0};
std::vector<double> v2{4.0, 5.0, 6.0};
std::vector<double> v3 = vecProduct(v1, v2);
std::cout << v3; // Should print 4, 10, 18
// Test 2
std::vector<double> v4{42.0};
std::cout << vecProduct(v1, v4); // Should print empty vector
std::cout << "done";
}
```
Running this code results in the following terminal output 
![[Pasted image 20240522183257.png]]

This testing program initializes two equal length vectors of doubles, an empty resultant vector, and a vector of unequal length to the others. Running the function on the two unequal length vectors produces the correct output, and the function produces an empty vector upon being passed argument vectors of unequal length. This is made more clear by the addition of the statement "done" at the end of the program. Since the string "done" follows a blank line after the three element product vector, the program must have printed an empty vector before the done statement.
### 6. Alternate solutions if attempted
None
## Problem 2: Vector Class
### 1. Problem description 
The task at hand is to create a class that implements the same functionality as the standard vector class built into C++. The requirements are as follows:
Public methods should include
1. Default constructor - MyVector()
2. Constructor that takes size as input - MyVector(int sz)
3. Copy Constructor - MyVector(MyVector& vin) 
4. Appends to end of array - void pushBack(int ele) 
5. Inserts to i-th position in array - void insert(int i, int ele) 
6. Reads the i-th element - int at(int i) 
7. Overloaded [ ] operator that reads the i-th element - int operator [ ] 
(int i)
8. Deletes the i-th element - void erase(int i) ./
9. Returns the number of elements - int size() ./
10. Return true if empty else false - bool empty() ./
11. Destructor - ~MyVector() ./
The vector should grow dynamically, doubling capacity when the number of elements exceeds the allocated size.
Write tests for each of the methods.
Bonus: Template the implementation, so that it can store any type of
elements (not limited to int). Also, add a copy assignment operator.
### 2. Initial solution description
The initial solution stores a fixed length array, and its initial length can be optionally set on construction of the instance. If the array is full of data when another element is supposed to be added to the vector, the data will be copied into a new array of twice the size, and the new element will be added into this new array. 
### 3.AI prompts used
None
### 4. Code explanation. Emphasize high level intuition (include code)
```C++
#include <iostream>
#include <string>

template<typename T>
void println(T msg) {
    std::cout << msg << std::endl;
}

template<typename T>
class MyVector {
    
    T* data;
    int numEle;
    int arrSize;
    
    public:
    
    MyVector(int sz=1) {
        arrSize = sz;
        numEle=0;
        
        data = new T[sz];
        
    }
    
    MyVector(MyVector& vin) {
        numEle = vin.numEle;
        arrSize = vin.arrSize;
        data = new T[arrSize];
        for (int i = 0; i < numEle; i++) {
                data[i] = vin.data[i];
        } // Was originally data = vin.data

    }
    
    MyVector& operator=(MyVector& other) {
        return new MyVector<T>(other);
    }
    
    ~MyVector() {
        delete[] data;
        
        println("Destructed");
    }
    
    void pushBack(T ele) {
        if (numEle == arrSize) {
            arrSize *=2;
            
            T* tempArr = new T[arrSize];
            
            for (int i = 0; i < numEle; i++) {
                tempArr[i] = data[i];
            }
            
            delete[] data;
            data = tempArr;
            
        }
        data[numEle] = ele;
        numEle++;
    }
    
    void insert(int ind, T ele) {
        if (ind==numEle) {
            pushBack(ele);
            return;
        }
        
        if (numEle == arrSize) arrSize*=2;
        numEle++;
        
        T* tempArr = new T[arrSize];
        
        for (int i = 0; i < ind; i++) {
            tempArr[i] = data[i];
        }
        tempArr[ind] = ele;
        for (int i = ind+1; i< numEle; i++) {
            tempArr[i] = data[i-1];
        }
        
        delete[] data;
        data = tempArr;
    }
    
    void erase(int ind) {
        numEle--;
        T* tempArr = new T[arrSize];
        
        for (int i = 0; i <ind; i++) {
            tempArr[i] = data[i];
        }
        
        for (int i = ind; i < numEle; i++) {
            tempArr[i] = data[i+1];
        }
        delete[] data;
        data = tempArr;
    }
    
    int size() {
        return numEle;
    }
    
    bool empty() {
        return !size();
    }
    
    T* atPtr(int i) { // So the operator [] can be used for element assignment
        if (i >= numEle) return &data[numEle-1];
        if (i < 0) return &data[0];
        return &data[i];
    }
    
    T at(int i) {
        if (i >= numEle) return data[numEle-1];
        if (i < 0) return data[0];
        return data[i];
    }
    
    T& operator [ ](int i) {
        return (*atPtr(i));
    }
    
    
    void print() {
        std::cout << '{';
        for (int i = 0; i<numEle-1; i++) std::cout << (at(i)) << ", ";
        std::cout << (at(numEle-1)) << '}' << '\n';
    }
    
    
};
```

To ensure that the array dynamically resizes itself, the class must keep track of the maximum array size, the number of elements in its array, and a pointer to its data array. Every time data is to be pushed back or inserted into the array, the code first checks if the number of elements is equal to the size of the array. If so, a new array of twice the size is created, and the existing data is copied into it. If this is an insert operation, the copying stops when the insertion point is reached, the new data is inserted, and the copying proceeds with an offset. This same method is used in the erase function, but with a backwards offset.

The copy constructor also copies the data into a new array. The at function can return the value or a pointer to the value. The overload for the [ ] operator returns a pointer so that elements can be assigned using this operator. 

5. Code testing (Include test code)
```C++
template<typename T>
void println(T msg) {
    std::cout << msg << std::endl;
}

int main() {
    println("Constructor");
    
    MyVector<int> v1;
    v1.print();
    println("Empty: " + std::to_string(v1.empty()));
    println("Size: " + std::to_string(v1.size()));
    
    println("pushBack");
    for (int i = 0; i<16; i++) v1.pushBack(i);
    v1.print();
    println("Empty: " + std::to_string(v1.empty()));
    println("Size: " + std::to_string(v1.size()));
    
    println("Insert");
    v1.insert(3,15);
    v1.print();
    
    println("At");
    println(v1.at(3));
    
    println("Overloaded []");
    println(v1[3]);
    
    println("Overloaded [] assignment");
    v1[3]=12;
    v1.print();
    
    println("Erase");
    v1.erase(3);
    v1.print();
    
    println("Copy Constructor");
    MyVector<int> v2(v1);
    MyVector<int> v3 = v1;
    
    v2[3]=10;
    v3.insert(4,11);
    
    v2.print();
    v3.print();
    
    return 0;    
}

```
The above testing code first prints to the console each element of the class it is testing, and then the output of the corresponding test. Each functionality is tested, and the contents of the vector are printed to the console to show functionality. 

![[Pasted image 20240528183132.png]]
The above screenshot shows that each required function has been implemented properly.
### 6. Alternate solutions if attempted
Initially, the copy constructor simply set the new instance's data array to the current instance's data array, with the line `data = vin.data`, this meant that editing any copies would edit all the copies, including the original. This was fixed.
Also, the [ ] operator overload initially returned the value at the index, but to further emulate the standard vector, it was made to return a pointer.

For class #data-structures 