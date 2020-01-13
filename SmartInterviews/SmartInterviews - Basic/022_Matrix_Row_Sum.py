# https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-matrix-row-sum/problem

"""
Given a matrix of size N x M. Print row-wise sum, separated by a newline.
Note: Try to solve this without declaring/storing the matrix.

Input Format

First line of input contains N, M - the size of the matrix. Its followed by N lines each containing M integers - elements of the matrix.

Constraints

1 <= N, M <= 100 
-106 <= ar[i] <= 106 


Output Format

Print the row-wise sum, separated by a newline.

Sample Input 0

2 3
5 -1 3
19 8 -5
Sample Output 0

7
22"""

def rowSum(a, N, M):
    sum =0
    for i in range(N):
        for j in range(M):
            # calculating the sum for each row i
            sum += a[i][j]
        print (sum)
        sum =0 # Resetting the sum before next row begins
    
    
N, M = map(int, input().split())
a = [[int(x) for x in input().split()] for _ in range(N)]
rowSum(a, N, M)