# https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-narcissistic-numbers/problem

"""
Given N, check whether it is a Narcissistic number or not. A narcissistic number is a number that is the sum of its own digits each raised to the power of the number of digits

Input Format

Input contains a integer - N.

Constraints

0 <= N <= 109

Output Format

Print "Yes" if the number is Narcissistic number, "No" otherwise.

Sample Input 0

8208
Sample Output 0

Yes
Explanation 0

84 + 24 + 04 + 84 = 8208"""


n = int(input())

def checkNarcissistic(n):
    n = str(n)
    sum = 0
    l = len(n)
    for char in n:
        x = int(char)
        sum += pow(x, l)

    if sum == int(n):
        return "Yes"
    return "No"

print (checkNarcissistic(n))