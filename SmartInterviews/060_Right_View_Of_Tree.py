# https://www.hackerrank.com/contests/smart-interviews/challenges/si-right-view-of-tree/problem

"""
Given an array of unique elements, construct a Binary Search Tree and print the right-view of the tree. Right view of a Tree is the set of nodes visible when tree is viewed from right side. 

Input Format

First line of input contains T - number of test cases. Its followed by 2T lines. First line of each test case contains N - number of nodes in the BST. The next line contains N unique integers - value of the nodes. 

Constraints

1 <= T <= 1000 
1 <= N <= 1000 
0 <= ar[i] <= 10000 

Output Format

For each test case, print the right-view of the Binary Search Tree, separated by newline. 

Sample Input 0

3
5
1 2 3 4 5 
5
3 2 4 1 5 
7
4 5 15 0 1 7 17 
Sample Output 0

1 2 3 4 5 
3 4 5 
4 5 15 17 """

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

"""Steps to follow:
1. Do level order traversal
2. Print last element in each level"""

def levelOrder(root):
    if root is None:
        return
    queue = []
    queue.append(root)
    
    while len(queue) > 0:
        l = len(queue)
        for i in range(l):
            node = queue.pop(0)
            
            # Print last element in each level
            if i == (l -1):
                print (node.info, end =" ")
                
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)


            
tree = BST()
t = int(input())
for tc in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    root = Node(arr[0])
    for i in range(1, n):
        tree.insert(root, Node(arr[i]))
    levelOrder(root)
    print()