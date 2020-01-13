# https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-sum-of-two-matrices/problem

"""
Given two matrices A and B of size N x M. Print sum(A+B) of matrices(A, B).
Note: Try solving it by declaring only a single matrix.

Input Format

First line of input contains N, M - size of the matrices. Its followed by 2*N lines each containing M integers - elements of the matrices. First N lines for matrix A and its followed by N lines for matrix B.

Constraints

1 <= N, M <= 100 
-106 <= ar[i] <= 106 


Output Format

Print sum(A+B) of matrices(A, B).

Sample Input 0

2 3
5 -1 3
19 8 4
4 5 -6
1 -2 12
Sample Output 0

9 4 -3
20 6 16
Explanation 0

Self Explanatory."""

def solve(N, M, A, B):
    C = [[0 for x in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            C[i][j] = A[i][j] + B[i][j]
    return C

N,M = map(int, input().split())

A = [[int(x) for x in input().split()] for _ in range(N)] 
B = [[int(x) for x in input().split()] for _ in range(N)] 

result = solve(N, M, A, B)
for row in result:
    print (' '.join(list(map(str, row))))

