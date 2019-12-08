#https://www.hackerrank.com/contests/smart-interviews/challenges/si-rotation-of-matrix
t = int(input())
for p in range(t):
    print (f'Test Case #{p+1}:') 
    n = int(input()) # size of the matrix. 2 stands for 2X2
    a = [[int(x) for x in input().split()] for _x in range(n)] # elements of matrix as in input
    a = [[str(a[j][i]) for j in range(n)] for i in range(n)] # swapping diagonal elements first
    a = list(map(reversed, a)) # then reversing elements in each row
    for row in a:
           print(' '.join(row))
           