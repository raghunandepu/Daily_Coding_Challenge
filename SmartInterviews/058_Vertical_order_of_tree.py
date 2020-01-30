# https://www.hackerrank.com/contests/smart-interviews/challenges/si-vertical-order-of-tree/problem

"""Given an array of unique elements, construct a Binary Search Tree and print the tree in a Vertical Order, starting from the left-most node. Print the nodes in each vertical in sorted order.

Input Format

First line of input contains T - number of test cases. Its followed by 2T lines. First line of each test case contains N - number of nodes in the BST. The next line contains N unique integers - value of the nodes. 

Constraints

1 <= T <= 1000 
1 <= N <= 1000 
0 <= ar[i] <= 10000 

Output Format

For each test case, print the Vertical Levels of the Binary Search Tree, separate each level by newline. Separate the output of different test cases with an extra newline.

Sample Input 0

3
5
1 2 3 4 5 
5
3 1 2 5 4 
7
4 5 15 0 1 7 17 
Sample Output 0

1 
2 
3 
4 
5 

1 
2 3 4 
5 

0 
1 4 
5 7 
15 
17 """


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

def getVerticalOrder(root, hd, d):
    """
    Utility function to store vertical order in dictionary 'd'  
    'hd' is horizontal distance of current node from root 
    'hd' is initially passed as 0 """
    
    if root is None:
        return
    
    # Store current node in map 'd' 
    try:
        d[hd].append(root.info)
    except:
        d[hd] = [root.info]
        
     # Store nodes in left subtree 
    getVerticalOrder(root.left, hd -1, d)
    
    # Store nodes in right subtree
    getVerticalOrder(root.right, hd + 1, d)
    


def printVerticalOrder(root):
    """
    The main function to print vertical order of a binary 
    tree ith given root
    """
    d = {} # dictionary
    hd = 0
    getVerticalOrder(root, hd, d)
    
    # Traverse the map and print nodes at every horizontal distance (hd)
    for index, value in enumerate(sorted(d)):
        for ele in sorted(d[value]):
            print (ele, end=" ")
        print()
    

tree = BST()
t = int(input())
for tc in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    root = Node(arr[0])
    for i in range(1,n):
        tree.insert(root, Node(arr[i]))
    printVerticalOrder(root)
    print()

