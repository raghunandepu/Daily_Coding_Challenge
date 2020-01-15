# https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-a-sparse-matrix/problem

"""
Given a matrix of size N x M. Print whether it is a sparse matrix. A matrix containing 0 value in more than half of its elements, then it is called a sparse matrix.

Input Format

First line of input contains N, M - size of the matrix. Its followed by N lines each containing M intergers - elements of the matrix.

Constraints

1 <= N, M <= 100 
0 <= ar[i] <= 109

Output Format

Print "Yes" if given matrix is Sparse matrix, otherwise print "No".

Sample Input 0

2 3
5 0 0
0 8 0
Sample Output 0

Yes"""

N, M = map(int, input().split())
A = [[int(x) for x in input().split()] for y in range(N)]

def sparseCheck(A, N, M):
    total_count = N * M
    sparse_count = 0
    for i in range(N):
        for j in range(M):
            if A[i][j] == 0:
                sparse_count += 1
    if sparse_count > (total_count // 2):
        return "Yes"
    return "No"

print (sparseCheck(A, N, M))
        