# https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-digits-sum/problem

"""
Given non-negative integer - N, print the sum of digits of the given number.

Input Format

Input contains non-negative integer - N.

Constraints

0 <= length(N) <= 103

Output Format

Print the sum of digits of the given number.

Sample Input 0

164
Sample Output 0

11
Explanation 0

Self Explanatory"""


n = int(input())
def solve(n):
    sum = 0
    n = str(n)
    for ele in n:
        sum += int(ele)
    return sum

print (solve(n))