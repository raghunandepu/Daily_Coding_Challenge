# https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-natural-numbers-sum/problem

"""
Given positive integer - N, print the sum of 1st N natural numbers.

Input Format

Input contains a positive integer - N.

Constraints

1 <= N <= 104

Output Format

Print the sum of 1st N natural numbers.

Sample Input 0

4
Sample Output 0

10"""


n = int(input())

def solve(n):
    return n * (n+1) // 2
    
print (solve(n))