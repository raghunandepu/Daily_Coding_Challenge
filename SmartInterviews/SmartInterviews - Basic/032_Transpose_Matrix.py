# https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-transpose-matrix/problem

"""
Given a matrix of size N x M. Print transpose of the matrix.

Input Format

First line of input contains N, M - the size of the matrix. Its followed by N lines each containing M integers - elements of the matrix.

Constraints

1 <= N, M <= 100 
-109 <= ar[i] <= 109 


Output Format

Print the transposed matrix.

Sample Input 0

2 2
5 -1
19 8
Sample Output 0

5 19
-1 8"""

N, M = map(int, input().split())
A = [[int(x) for x in input().split()]for _ in range(N)]

def solve(A, N, M):
    C = [[0 for _ in range(N)] for _ in range(M)]  # reverse size of input
    for i in range(M): # looping through columns
        for j in range(N): # looping through rows
            C[i][j] = A[j][i]
    return C

result = solve(A, N, M)
for row in result:
    print (' '.join(list(map(str, row))))