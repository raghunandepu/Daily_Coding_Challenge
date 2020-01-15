# https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-cubes-sum/problem

"""
Given positive integer - N, print the sum of cubes of 1st N natural numbers.

Input Format

Input contains a positive integer - N.

Constraints

1 <= N <= 102

Output Format

Print the sum of cubes of 1st N natural numbers.

Sample Input 0

4
Sample Output 0

100"""

n = int(input())

def cubeSum(n):
    x = (n / 2) * (n+1)  # Doing division first to avoid integer overflow
    return int (x * x)

print (cubeSum(n))