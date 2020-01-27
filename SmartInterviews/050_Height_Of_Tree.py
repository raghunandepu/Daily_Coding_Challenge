# https://www.hackerrank.com/contests/smart-interviews/challenges/si-height-of-tree/problem

"""
Given an array of unique elements, construct a Binary Search Tree and find the height of the tree.

Input Format

First line of input contains T - number of test cases. Its followed by 2T lines. First line of each test case contains N - number of nodes in the BST. The next line contains N unique integers - value of the nodes. 

Constraints

1 <= T <= 1000 
1 <= N <= 1000 
0 <= ar[i] <= 10000 

Output Format

For each test case, print the height of the Binary Search Tree, separated by newline.

Sample Input 0

3
5
1 2 3 4 5 
5
3 2 4 1 5 
7
4 5 15 0 1 7 17 
Sample Output 0

4
2
3"""

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
    if root:
        lDepth = height(root.left)
        rDepth = height(root.right)
        if lDepth > rDepth:
            return 1 + lDepth
        else:
            return 1 + rDepth
    return -1

tree = BST()
t = int(input())
for tc in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    root = Node(arr[0])
    for i in range(1, n):
        tree.insert(root, Node(arr[i]))
    print(height(root))

