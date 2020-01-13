# https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-compute-n/problem

"""
Given a non-negative number - N. Print N!

Input Format

Input contains a number - N.

Constraints

0 <= N <= 10

Output Format

Print Factorial of N.

Sample Input 0

5
Sample Output 0

120
Explanation 0

Self Explanatory"""

n = int(input())
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
print (factorial(n))