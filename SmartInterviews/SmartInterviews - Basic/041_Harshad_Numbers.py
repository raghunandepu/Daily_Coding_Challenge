# https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-harshad-number/problem

"""
Determine whether the given number is a Harshad number. A Harshad number is an integer, that is divisible by the sum of its digits.

Input Format

Input contains a integer - N.

Constraints

1 <= N <= 109

Output Format

Print "Yes" if the number is harshad number, "No" otherwise.

Sample Input 0

18
Sample Output 0

Yes
Explanation 0

18 / (1 + 8) = 2
As 18 is divisible by the sum of its digits, it is harshad number."""

n = int(input())

def checkHarshadNumber(n):
    n = str(n)
    sum =0
    for char in n:
        sum += int(char)
    if int(int(n) % sum) == 0:
        return "Yes"
    return "No"

print (checkHarshadNumber(n))