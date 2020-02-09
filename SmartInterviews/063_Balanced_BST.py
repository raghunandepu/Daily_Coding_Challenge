# https://www.hackerrank.com/contests/smart-interviews/challenges/si-is-balanced-tree
"""
Given an array of unique elements, construct a Binary Search Tree and check if its balanced. A tree is said to be balanced if for every node, the difference between the height of its child nodes is not greater than 1. 

Input Format

First line of input contains T - number of test cases. Its followed by 2T lines. First line of each test case contains N - number of nodes in the BST. The next line contains N unique integers - value of the nodes. 

Constraints

1 <= T <= 1000 
1 <= N <= 1000 
0 <= ar[i] <= 10000 

Output Format

For each test case, print "Yes" if the Binary Search Tree is balanced, "No" otherwise, separated by newline. 

Sample Input 0

3
5
1 2 3 4 5 
5
3 2 4 1 5 
7
4 5 15 0 1 7 17 
Sample Output 0

No
Yes
No"""

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
                if root.info > node.info:
                    if root.left is None:
                        root.left = node
                    else:
                        self.insert(root.left, node)

# utility class to pass height object                       
class Height:
    def __init__(self):
        self.height = 0

def isBalanced(root, height):
    
    # lh and rh to store height of  
    # left and right subtree 
    lh = Height()
    rh = Height()
    
    
    if root is None:
        return "Yes"

    
    # l and r are used to check if left 
    # and right subtree are balanced
    l = isBalanced(root.left, lh)
    r = isBalanced(root.right, rh)
    
    height.height = max(lh.height, rh.height) + 1
    
    # height of tree is maximum of  
    # left subtree height and 
    # right subtree height plus 1
    if abs(lh.height - rh.height) <= 1:
        return l and r 
    return "No"

tree = BST()
height = Height()

t = int(input())
for tc in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    root = Node(arr[0])
    for i in range(1, n):
        tree.insert(root, Node(arr[i]))
    print (isBalanced(root, height))