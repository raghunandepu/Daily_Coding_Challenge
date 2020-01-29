# https://www.hackerrank.com/contests/smart-interviews/challenges/si-bottom-up-level-order-of-tree/problem

"""Given an array of unique elements, construct a Binary Search Tree and print the Level Order of the tree, not top-down, but bottom-up.

Input Format

First line of input contains T - number of test cases. Its followed by 2T lines. First line of each test case contains N - number of nodes in the BST. The next line contains N unique integers - value of the nodes. 

Constraints

1 <= T <= 1000 
1 <= N <= 1000 
0 <= ar[i] <= 10000 

Output Format

For each test case, print the bottom-up Level Order of the Binary Search Tree, separate each level by newline. Separate the output of different test cases with an extra newline.

Sample Input 0

3
5
1 2 3 4 5 
5
3 2 4 1 5 
7
4 5 15 0 1 7 17 
Sample Output 0

5 
4 
3 
2 
1 

1 5 
2 4 
3 

7 17 
1 15 
0 5 
4 """

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

def levelOrder(root):
    if root is None:
        return
    queue = []
    return_list = []
    queue.append(root)
    while len(queue) > 0:
        ans = []
        l = len(queue)
        for i in range(l):
            node = queue.pop(0)
            ans.append(node.info)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        return_list.append(ans)
    return return_list


            
tree = BST()
t = int(input())
for tc in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    root = Node(arr[0])
    for i in range(1, n):
        tree.insert(root, Node(arr[i]))
    result = levelOrder(root)
    # Traverse from top down, storing the nodes at each level and then reversing to print bottom-up
    result = result[::-1] 
    for row in result:
        print(' '.join(map(str, row)))
    print()
