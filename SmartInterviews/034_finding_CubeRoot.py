# https://www.hackerrank.com/contests/smart-interviews/challenges/si-finding-cuberoot/submissions/code/1318720922

"""
Find the cube root of the given number. Assume that all the input test cases will be a perfect cube.

Input Format

First line of input contains T - number of test cases. Its followed by T lines, each containing a single integer. 

Constraints

30 points 
1 <= T <= 103 
-109 <= N <= 109 

70 points 
1 <= T <= 106 
-1018 <= N <= 1018 

Output Format

For each test case, print the cube root of the number, separated by newline.

Sample Input 0

5
-27
-125
1000
6859
-19683
Sample Output 0

-3
-5
10
19
-27"""


def cubeRoot(n):
    if n > 0:
        low = 1
        high = n
    else:
        low = n
        high = 1
        
    while (low <= high):
        mid = (low + high) // 2
        x = mid ** 3
        if x == n:
            return mid
        if x < n:
            low = mid + 1
        else:
            high = mid - 1

t = int(input())
for t in range(t):
    n = int(input())
    result = cubeRoot(n)
    print (result)
    