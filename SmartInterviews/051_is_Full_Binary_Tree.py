# https://www.hackerrank.com/contests/smart-interviews/challenges/si-is-full-binary-tree

"""
Given an array of unique elements, construct a Binary Search Tree and check if its a Full Binary Tree [FBT]. A FBT is one in which each node is either a leaf or possesses exactly 2 child nodes. 

Input Format

First line of input contains T - number of test cases. Its followed by 2T lines. First line of each test case contains N - number of nodes in the BST. The next line contains N unique integers - value of the nodes. 

Constraints

1 <= T <= 1000 
1 <= N <= 1000 
0 <= ar[i] <= 10000 

Output Format

For each test case, print "True" if the Binary Search Tree is a FBT, "False" otherwise, separated by newline.

Sample Input 0

3
5
1 2 3 4 5 
11
8 3 30 15 40 18 12 17 25 1 7 
7
4 5 15 0 1 7 17 
Sample Output 0

False
True
False"""

# Approach:
# https://www.geeksforgeeks.org/check-whether-binary-tree-full-binary-tree-not/
"""To check whether a binary tree is a full binary tree we need to test the following cases:-



1) If a binary tree node is NULL then it is a full binary tree.
2) If a binary tree node does have empty left and right sub-trees, then it is a full binary tree by definition.
3) If a binary tree node has left and right sub-trees, then it is a part of a full binary tree by definition. In this case recursively check if the left and right sub-trees are also binary trees themselves.
4) In all other combinations of right and left sub-trees, the binary tree is not a full binary tree."""

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
                    
def isFullBT(root):
    if root is None:
        return True
    if root.left is None and root.right is None:
        return True
    if root.left is not None and root.right is not None:
        return isFullBT(root.left) and isFullBT(root.right)
    return False

tree = BST()
t = int(input())
for tc in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    root = Node(arr[0])
    for i in range(1, n):
        tree.insert(root, Node(arr[i]))
    print(isFullBT(root))