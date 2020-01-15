# https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-print-half-diamond-pattern/problem

"""
Print half diamond pattern using '*'. See example for more details.

Input Format

Input contains a single integer N.

Constraints

1 <= N <= 50

Output Format

For the given integer, print the half diamond pattern.

Sample Input 0

3
Sample Output 0

*
**
***
**
*"""


n = int(input())
def pattern(n):
    for i in range(0, n):
        for j in range(0, i+1):
            print ('*', end = '')
        print()
    for i in range(n, 0, -1):
        for j in range(0, i-1):
            print("*", end = '')
        print()
pattern(n)