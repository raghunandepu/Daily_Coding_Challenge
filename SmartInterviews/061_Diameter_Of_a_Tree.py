# https://www.hackerrank.com/contests/smart-interviews/challenges/si-diameter-of-a-tree/problem

"""
Given an array of unique elements, construct a Binary Search Tree and find the diameter of the tree. Diameter is defined as the number of nodes on the longest path between 2 nodes of the tree. 

Input Format

First line of input contains T - number of test cases. Its followed by 2T lines. First line of each test case contains N - number of nodes in the BST. The next line contains N unique integers - value of the nodes. 

Constraints

1 <= T <= 1000 
1 <= N <= 5000 
0 <= ar[i] <= 10000 

Output Format

For each test case, print the diameter of the Binary Search Tree, separated by newline. 

Sample Input 0

3
5
1 2 3 4 5 
5
2 4 3 1 5 
7
4 5 15 0 1 7 17 
Sample Output 0

5
4
6
"""
import sys
 

class Node:
    def __init__(self, info):
        self.info = info
        self.right = None
        self.left = None

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

def height(root):
    global diameter
    
    if root is None:
        return 0
    
    lheight = height(root.left)
    rheight = height(root.right)
    
    # ans for this problem will be sum of left height, right height and 1.
    diameter = max(diameter,  1 + lheight + rheight)
    
    if lheight > rheight:
        return 1 + lheight
    else:
        return 1 + rheight
    


def getDiameter(root):
    if root is None:
        return 0
    height(root)

tree = BST()
t = int(input())
for tc in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    root = Node(arr[0])
    for i in range(1, n):
        tree.insert(root, Node(arr[i]))
    diameter = -sys.maxsize  - 1 # max negative value
    getDiameter(root)
    print(diameter)
