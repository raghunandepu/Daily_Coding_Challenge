# Solution

"""
Given a 2D square matrix, print the matrix in a spiral order. Refer examples for more details. From interviews point of view, after you scan the matrix in a 2D array, try to print the matrix in a spiral order without using any extra space. 


Input Format

First line of input contains T - number of test cases. First line of each test case contains N - size of the matrix [NxN]. Its followed by N lines each containing N integers - elements of the matrix. 

Constraints

1 <= T <= 100 
1 <= N <= 100 
-100 <= ar[i][j] <= 100 

Output Format

For each test case, print the matrix in a spiral order, separated by newline. 

Sample Input 0

4
1
1
2
1 2
4 3
3
1 2 3
8 9 4
7 6 5
5
-44 25 -52 69 -5 
17 22 51 27 -44 
-79 28 -78 1 -47 
65 -77 -14 -21 -6 
-96 43 -21 -20 90 
Sample Output 0

1 
1 2 3 4 
1 2 3 4 5 6 7 8 9 
-44 25 -52 69 -5 -44 -47 -6 90 -20 -21 43 -96 65 -79 17 22 51 27 1 -21 -14 -77 28 -78 
Explanation 0

Self Explanatory"""
# Complexity: Time complexity of the above solution is O(mn).

# Reference: https://www.geeksforgeeks.org/print-a-given-matrix-in-spiral-form/

# Approach: 
# The above problem can be solved using four for loops which prints all the elements. 
# Every for loop defines a single direction movement along with the matrix.
#  The first for loop represents the movement from left to right, whereas the second crawl represents the movement from top to bottom, the third represents the movement from the right to left, and the fourth represents the movement from bottom to up. The four variable along with their use is given below.

def solution(a, n):
    """
    k - starting row index 
    m - ending row index 
    l - starting column index 
    n - ending column index
    """
    k = 0
    l = 0
    m = len(a) # no of rows
    n = len(a[0]) 
    while (k < m and l <n):
        # Print the first row from 
        # the remaining rows 
        for i in range(l,n):
            print (a[k][i], end = " ")
        k += 1
        
        # Print the last column from 
        # the remaining columns
        for i in range(k, m):
            print (a[i][n-1], end = " ")
        n -= 1
        
        # Print the last row from 
        # the remaining rows 
        if (k < m):
            for i in range(n-1, (l-1), -1):
                print (a[m-1][i], end =" ")
            m -= 1
        
        # Print the first column from 
        # the remaining columns
        if (l < n) : 
            for i in range(m - 1, k - 1, -1) : 
                print(a[i][l], end = " ") 
              
            l += 1
            

t = int(input())
for tc in range(t):
    n = int(input())
    arr = []
    for row in range(n):
        row = list(map(int, input().split()))
        arr.append(row)
    result = solution(arr, n)
    print ('')