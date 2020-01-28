# https://www.hackerrank.com/contests/smart-interviews/challenges/si-zig-zag-bottom-up-level-order-of-tree/problem
"""
Given an array of unique elements, construct a Binary Search Tree and print the Level Order of the tree in a zig-zag fashion, not top-down, but bottom-up. Assume root is at level-1, zig-zag means that nodes at even levels will be printed left to right and the nodes at odd levels will be printed from right to left. 

Input Format

First line of input contains T - number of test cases. Its followed by 2T lines. First line of each test case contains N - number of nodes in the BST. The next line contains N unique integers - value of the nodes. 

Constraints

1 <= T <= 1000 
1 <= N <= 1000 
0 <= ar[i] <= 10000 

Output Format

For each test case, print the bottom-up Level Order Traversal of the Binary Search Tree in zig-zag fashion, separated by newline.

Sample Input 0

3
5
1 2 3 4 5 
5
3 2 4 1 5 
7
4 5 15 0 1 7 17 
Sample Output 0

5 4 3 2 1 
5 1 2 4 3 
7 17 15 1 0 5 4 """

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

def height(root):
    if root is None:
        return 0
    lheight = height(root.left)
    rheight = height(root.right)
    if lheight > rheight:
        return 1 + lheight
    else:
        return 1 + rheight

def levelOrder(root, level, flag):
    if root is None:
        return
    if level == 1:
        print(root.info, end=" ")
    else:
      # Traverse accordingly in zig zag manner for odd and even levels(height)
        if (flag is True):
            levelOrder(root.left, level - 1, flag)
            levelOrder(root.right, level - 1, flag)
        else:
            levelOrder(root.right, level - 1, flag)
            levelOrder(root.left, level - 1, flag)
            
            
def printSpiral(root):
    h = height(root)
    flag = True if h % 2 == 0 else False
    for i in range(h,0,-1):
        levelOrder(root, i, flag)
        flag = not flag
        
tree = BST()
t = int(input())
for tc in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    root = Node(arr[0])
    for i in range(1,n):
        tree.insert(root, Node(arr[i]))
    printSpiral(root)
    print()