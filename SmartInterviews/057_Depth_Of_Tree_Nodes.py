# https://www.hackerrank.com/contests/smart-interviews/challenges/si-depth-of-tree-nodes/problem

"""
Given an array of unique elements, construct a Binary Search Tree and for every node, print the depth of that node.

Input Format

First line of input contains T - number of test cases. Its followed by 2T lines. First line of each test case contains N - number of nodes in the BST. The next line contains N unique integers - value of the nodes. 

Constraints

For each test case, print the depth of every node of the Binary Search Tree, separated by newline.

1 <= T <= 1000 
1 <= N <= 1000 
0 <= ar[i] <= 10000 

Output Format

For each test case, print N integers, where the ith integer denotes the depth of A[i] in the Binary Search Tree, separated by newline.

Sample Input 0

3
5
1 2 3 4 5 
5
3 2 4 1 5 
7
4 5 15 0 1 7 17 
Sample Output 0

0 1 2 3 4 
0 1 1 2 2 
0 1 2 1 2 3 3 """

class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.depth = 0

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, root, node, depth):
        if root is None:
            root = node
            root.depth = depth
        else:
            if root.info < node.info:
                if root.right is None:
                    root.right = node
                    node.depth = depth + 1
                else:
                    self.insert(root.right, node, depth + 1)
            else:
                if root.left is None:
                    root.left = node
                    node.depth = depth + 1
                else:
                    self.insert(root.left, node, depth + 1)

def search(root, key): 
      
    # Base Cases: root is null or key is present at root 
    if root is None:
        return 0
    if root.info == key:
        return root.depth
  
    # Key is greater than root's key 
    if root.info < key: 
        return search(root.right,key) 
    
    # Key is smaller than root's key 
    return search(root.left,key)

tree = BST()
t  = int(input())
for tc in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    root = Node(arr[0])
    for i in range(1, n):
        tree.insert(root, Node(arr[i]),0)
    for e in arr:
        result = search(root, e )
        print(result, end=" ")
    print()