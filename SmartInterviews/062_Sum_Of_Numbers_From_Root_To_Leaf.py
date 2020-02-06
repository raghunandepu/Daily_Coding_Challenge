# https://www.hackerrank.com/contests/smart-interviews/challenges/si-sum-of-numbers-from-root-to-leaf-paths/copy-from/1320395667

"""
Given an array of unique elements, construct a Binary Search Tree and print the sum of all the numbers formed along the path from the root node to the leaf nodes. 

Input Format

First line of input contains T - number of test cases. Its followed by 2T lines. First line of each test case contains N - number of nodes in the BST. The next line contains N unique integers - value of the nodes. 

Constraints

1 <= T <= 1000 
1 <= N <= 1000 
0 <= ar[i] <= 10000 

Output Format

For each test case, print the sum, separate each traversal by newline. Since the output can be very large, print output % 1000000007. 

Sample Input 0

3
5
1 2 3 4 5
5
3 2 4 1 5
7
4 5 15 2 1 7 17
Sample Output 0

12345
666
497095"""

M = 1e9+7
class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        
class BST:
    def __init__(self):
        self.root = None
        
    def insert(self, root, node):
        if root is None:
            root = node
        else: 
            if root.info < node.info:
                if root.right is None:
                    root.right = node
                else:
                    self.insert(root.right, node)
            else:
                if root.left is None:
                    root.left = node
                else:
                    self.insert(root.left, node)

def rootToLeafSum(root, val):
    if root is None:
        return 0
    
    # update value
    val = int((int(str(val) + str(root.info)))%M)
    
    if root.left is None and root.right is None:
        return int(int(val) % M)
    
    return (rootToLeafSum(root.left, val) + rootToLeafSum(root.right, val))


tree = BST()
t = int(input())
for tc in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    root = Node(arr[0])
    for i in range(1,n):
        tree.insert(root, Node(arr[i]))
    print(rootToLeafSum(root, val=0))