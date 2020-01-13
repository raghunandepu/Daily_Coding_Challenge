# https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-compute-a-power-b/submissions/code/1319356869
"""
Given two integers a and b. compute a power b.

Input Format

Input contains two positive integers a and b.

Constraints

1 <= a <=100 
0 <= b <=9

Output Format

Print a power b.

Sample Input 0

2 3
Sample Output 0

8
"""

# O(logn)

a, b = map(int, input().split())
def power(a,b):
    if b == 0:
        return 1
    temp = power(a, b//2)
    if int(b % 2) == 0:
        return temp * temp
    else:
        return temp * temp  * a

print (power(a,b))