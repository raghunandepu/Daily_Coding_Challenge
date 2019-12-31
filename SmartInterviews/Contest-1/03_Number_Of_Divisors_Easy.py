#https://www.hackerrank.com/contests/smart-interviews-14a/challenges/si-number-of-divisors
"""
Given a number, find the number of divisors of that number.

Input Format

First line of input contains T - number of test cases. Its followed by T lines, each containing a single number N.

Constraints

30 points 
1 <= T <= 100 
1 <= N <= 106 

70 points 
1 <= T <= 100 
1 <= N <= 109 

Output Format

For each test case, print the number of divisors of N, separated by newline. 

Sample Input 0

5
8
16808
9
23
97158
Sample Output 0

4
16
3
2
8"""

from math import sqrt
def solve(n):
    count = 0
    i = 1
    while( i <= int(sqrt(n))):
        if (n % i == 0):
            if (n / i == i):
                count += 1
            else:
                count += 2
        i += 1
    return count

t = int(input())
for tc in range(t):
    n = int(input())
    result = solve(n)
    print (result)