# https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-long-factorial/problem
"""
Given Number N. Print N!

Input Format

The input contains a number - N.

Constraints

0 <= N <= 20

Output Format

Print factorial of N.

Sample Input 0

3
Sample Output 0

6
Explanation 0

Self Explanatory"""


# Same as normal factorial in Python 
n = int(input())
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
print (factorial(n))