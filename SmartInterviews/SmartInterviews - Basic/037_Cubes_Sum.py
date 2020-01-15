# https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-squares-sum/problem

"""
Given N, print the sum of squares of 1st N natural numbers.

Input Format

Input contains positive integer - N.

Constraints

1 <= N <= 103

Output Format

Print the sum of squares of 1st N natural numbers.

Sample Input 0

15
Sample Output 0

1240"""


n = int(input())

def squaresSum(n):
    return int ((n) * (n+1) * (2*n +1)/6)

print (squaresSum(n))