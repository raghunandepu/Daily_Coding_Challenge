# https://www.hackerrank.com/contests/smart-interviews/challenges/si-is-complete-binary-tree/problem

"""
Given an array of unique elements, construct a Binary Search Tree and check if its a complete tree. In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. 

Input Format

First line of input contains T - number of test cases. Its followed by 2T lines. First line of each test case contains N - number of nodes in the BST. The next line contains N unique integers - value of the nodes. 

Constraints

1 <= T <= 1000 
1 <= N <= 1000 
0 <= ar[i] <= 10000 

Output Format

For each test case, print "Yes" if it is a Complete Binary Search Tree, "No" otherwise, separated by newline. 

Sample Input 0

3
5
1 2 3 4 5 
5
4 2 5 3 1 
7
4 5 15 0 1 7 17 
Sample Output 0

No
Yes
No"""

# https://www.geeksforgeeks.org/check-if-a-given-binary-tree-is-complete-tree-or-not/

# Approach: Using level order tree traversal
"""To understand the approach, let us first define the term ‘Full Node’. A node is ‘Full Node’ if both left and right children are not empty (or not NULL).
The approach is to do a level order traversal starting from the root. In the traversal, once a node is found which is NOT a Full Node, all the following nodes must be leaf nodes.
Also, one more thing needs to be checked to handle the below case: If a node has an empty left child, then the right child must be empty."""

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

def isCompleteBinaryTree(root):
    if root is None:
        return "Yes"
    
    # create an empty queue
    queue = []
    
    # We will set flag to True when a non-full node is seen 
    flag = False
    
    # Do level order traversal using queue
    queue.append(root)
    while (len(queue) > 0):
        tempNode = queue.pop(0)
        
        # Check if left child is present 
        if tempNode.left:
            # If we have seen a non-full node, and we see 
            # a node with non-empty left child, then the 
            # given tree is not a complete binary tree
            if flag == True:
                return "No"
            
            # Enqueue left child
            queue.append(tempNode.left)
            
        else:
            flag = True
            
        # Check if right child is present 
        if tempNode.right:
             # If we have seen a non full node, and we  
            # see a node with non-empty right child, then 
            # the given tree is not a compelete BT
            if flag == True:
                return "No"
            # Enqueue right child 
            queue.append(tempNode.right)
            
        else:
            flag = True
     
    # If we reach here, then the tree is complete BT 
    return "Yes"
                   

tree = BST()
t = int(input())
for tc in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    root = Node(arr[0])
    for i in range(1, n):
        tree.insert(root, Node(arr[i]))
    print(isCompleteBinaryTree(root))
        