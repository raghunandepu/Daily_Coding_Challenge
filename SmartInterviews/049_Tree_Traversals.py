# https://www.hackerrank.com/contests/smart-interviews/challenges/si-tree-traversals/problem

"""
Given an array of unique elements, construct a Binary Search Tree and print the PreOrder, InOrder and PostOrder Traversals of the tree.

Input Format

First line of input contains T - number of test cases. Its followed by 2T lines. First line of each test case contains N - number of nodes in the BST. The next line contains N unique integers - value of the nodes. 

Constraints

1 <= T <= 1000 
1 <= N <= 1000 
0 <= ar[i] <= 10000 

Output Format

For each test case, print the PreOrder, InOrder and PostOrder Traversals of the Binary Search Tree, separate each traversal by newline. Separate the output of different test cases with an extra newline.

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
1 2 3 4 5 
5 4 3 2 1 

3 2 1 4 5 
1 2 3 4 5 
1 2 5 4 3 

4 0 1 5 15 7 17 
0 1 4 5 7 15 17 
1 0 7 17 15 5 4 """

class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
# A utility function to insert a new node with the given key 

       
def insert(root, node):
    if root is None:
        root = node
    else:
        if root.info < node.info:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)

def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.info, end = " ")
        inOrder(root.right)

def preOrder(root):
    if root:
        print(root.info, end = " ")
        preOrder(root.left)
        preOrder(root.right)
        
def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.info, end = " ")
                    
            

t = int(input())
for tc in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    root = Node(arr[0])
    for i in range(1,n):
        insert(root, Node(arr[i]))
    preOrder(root)
    print()
    inOrder(root)
    print()
    postOrder(root)
    print()
    print()