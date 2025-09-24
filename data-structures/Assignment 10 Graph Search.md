Jaskin Kabir 801186717
## Problem 1: 
### 1.Problem description
Given the adjacency list of a graph, find the smallest number of nodes that must be traversed to travel between two given nodes.
### 2.Initial solution description
This problem could be solved by using the Breadth First Search algorithm. My first step was to implement the BFS algorithm. Once I had done this, I thought the minimum distance could be found by counting the number of steps the BFS algorithm takes to find the ending node after starting from the beginning node. However, I realized this was incorrect, as it was counting all nodes visited by the algorithm rather than the nodes required to visit before reaching the end. 

The approach was then switched to use a dictionary of distances from the starting point to each node explored by the algorithm. If the target node is reached during the construction of the dictionary, return the distance from v1. If the target node is never reached, return -1.
### 3.AI prompts used
None
### 4. Code explanation. Emphasize high level intuition (include code)
The BFS algorithm is implemented iteratively using a queue to store the nodes that must be visited and an unordered map to store the nodes that have already been visited and their distance from the starting node. At the beginning, the first node is marked as visited, and its distance from the start is stored as 0. Then, it will iteratively visit all neighbors of each node in the queue and push its neighbors to the queue until either every single node is visited or until the target node is found. 

```cpp
int numHops(unordered_map<string, vector<string>>& aList, string v1, string v2) {
    // Implement BFS
    
    queue<string> toBeExplored;
    unordered_map<string, int> distanceFromV1;
    
    distanceFromV1[v1]=0;
    toBeExplored.push(v1);
    
    
    while (!toBeExplored.empty()) {
        string curVertex = toBeExplored.front();
        toBeExplored.pop();
        
        for (string neighbor : aList[curVertex]) {
            
            if (!(distanceFromV1.find(neighbor) == distanceFromV1.end())) continue;
            
            distanceFromV1[neighbor]=distanceFromV1[curVertex]+1;
            
            if (neighbor == v2) return distanceFromV1[curVertex]+1;
            
            toBeExplored.push(neighbor);
            
        }
        
    }
    
    return -1;
}```

### 5.Code testing (Include test code)
The following testing code was given as part of the assignment. Its output can be seen below as well.
```cpp
    for (char v1='A'; v1<'J'; v1++) {
         for (char v2='A'; v2<'J'; v2++) {
             if (v1==v2) continue;
            cout << "Number of hops between cities " << v1 << " and " << v2 << " is " << numHops(adjList, string(1, v1), string(1, v2)) << endl; // Should be 3 
         }
    }

	return 0;
```
![[Pasted image 20240618212413.png]]
By removing the connection between I and H, and then calling the function for every combination of cities, the feature of returning -1 if there is no valid path could be tested. The code to implement this test and its corresponding output can be seen below:
```cpp
int main() {
	unordered_map<string, vector<string>> adjList{ {"A", {"C", "E"}},
	   											{"C", {"A", "I"}}, 
												{"I", {"C", /*"H",*/ "B","D"}},
												{"H", {"I"}},
												{"D", {"I", "B", "G"}},
												{"B", {"E", "F", "G", "D", "I"}},
												{"G", {"B", "D"}},
												{"F", {"B"}},
												{"E", {"A", "B"}} //H-I-B-E; D-I-C-A
												};

	for (char v1='A'; v1<'J'; v1++) {
         for (char v2='A'; v2<'J'; v2++) {
             if (v1==v2) continue;
            cout << "Number of hops between cities " << v1 << " and " << v2 << " is " << numHops(adjList, string(1, v1), string(1, v2)) << endl;
         }
    }

	return 0;
}
```
![[Pasted image 20240618212806.png]]
This output shows that all the paths that relied on the connection between I and H to be completed are now impossible.
### 6.Alternate solutions if attempted
```cpp
int numHopsBad(unordered_map<string, vector<string>>& aList, string v1, string v2) {
    // Implement BFS
    
    queue<string> toBeExplored;
    unordered_map<string, bool> visitedNodes;
    
    visitedNodes[v1]=true;
    toBeExplored.push(v1);
    
    int hops = 0;
    
    while (!toBeExplored.empty()) {
        string curVertex = toBeExplored.front();
        toBeExplored.pop();
        cout << curVertex;
        
        for (string neighbor : aList[curVertex]) {
            
            if (visitedNodes[neighbor]) continue;
            
            if (neighbor == v2) return hops;
            
            visitedNodes[neighbor] = true;
            toBeExplored.push(neighbor);
            
        }
        
        hops++;
    }
    
    return -1;   
}
```
## Problem 2: Find If Path Exists in Graph
### 1.Problem description:
Given the number of nodes in a graph, and a list of connections between two nodes in a graph, determine if there exists a path between two given nodes.
### 2.Initial solution description
Since the BFS algorithm implemented above already tries to find a path from a start node to an end node and returns -1 if it doesn't find one, the above code can simply be copied into this new code and adapted to work with integers. 

However, that function works on an adjacency list stored in an unordered map, but the problem gives the adjacency list as a list of connections. In order to use the BFS code for this problem, the list must be converted into an unordered map.

My intuition for this process was to iterate over the connection list and add the neighboring node into the starting node's list of connected nodes in the adjacency map. 
### 3.AI prompts used
"make a function to print an unordered map"
### 4. Code explanation. Emphasize high level intuition (include code)

```cpp
class Solution {

public:
    int numHops(unordered_map<int, vector<int>>& aList, int v1, int v2) {

        // Implement BFS

        queue<int> toBeExplored;

        unordered_map<int, int> distanceFromV1;

        distanceFromV1[v1]=0;

        toBeExplored.push(v1);

        int hops = 0;

        while (!toBeExplored.empty()) {

            int curVertex = toBeExplored.front();

            toBeExplored.pop();

            for (int neighbor : aList[curVertex]) {

                if (!(distanceFromV1.find(neighbor) == distanceFromV1.end())) continue;

                distanceFromV1[neighbor]=distanceFromV1[curVertex]+1;

                toBeExplored.push(neighbor);

            }

        }

        if (distanceFromV1.find(v2) == distanceFromV1.end()) return -1;

        return distanceFromV1[v2];

}

  
  

    bool validPath(int n, vector<vector<int>>& edges, int source, int destination) {

        unordered_map<int, vector<int>> adjMap;

        for (vector<int>& edge: edges) {

            adjMap[edge[0]].push_back(edge[1]);

            adjMap[edge[1]].push_back(edge[0]);

        }

        //printUnorderedMap(adjMap);

        return !(numHops(adjMap, source, destination)==-1);

    }

};
```
### 5.Code testing (Include test code)
The following code was used for debugging, while leetcode was used for rigorous testing
```cpp
int main() {
    
    Solution s;
    vector<vector<int>> edges = {{0,1},{1,2},{2,0}};
    cout << s.validPath(3, edges, 0,2) << '\n';
}
```
![[Pasted image 20240618215352.png]]
### 6.Alternate solutions if attempted

For class #data-structures 