"""
Given a matrix of size N x M. Print column-wise sum, separated by a newline.

Input Format

The first line of input contains N, M - the size of the matrix. Its followed by N lines each containing M integers - elements of the matrix.

Constraints

1 <= N, M <= 100 
-106 <= ar[i] <= 106 


Output Format

Print the column wise sum, separated by newline.

Sample Input 0

2 2
5 -1
19 8
Sample Output 0

24
7
Explanation 0

Self Explanatory."""

def columnSum(a, N, M):
    sum = 0
    for i in range(M):
        for j in range(N):
           # Sum of the column i
            sum += a[j][i]
        print (sum)
        sum = 0 # Reset Sum before going to next column
    
            
N, M = map(int, input().split())
a = [[int(x) for x in input().split()] for _ in range(N)]
columnSum(a, N, M)

