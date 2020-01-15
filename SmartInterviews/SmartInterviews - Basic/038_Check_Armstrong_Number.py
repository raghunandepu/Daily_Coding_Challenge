# https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-check-armstrong-number/submissions/code/1319444420

"""
Check whether a given number is Armstrong number.

Input Format

Input contains a integer - N.

Constraints

0 <= N <= 109

Output Format

Print "Yes" if the number is Armstrong number, "No" otherwise.

Sample Input 0

153
Sample Output 0

Yes
Explanation 0

13 + 53 + 33 = 153"""


n = int(input())

def checkArmstrongNumber(n):
    n = str(n)
    sum = 0
    for char in n:
        x = int(char)
        sum += (x * x * x)

    if sum == int(n):
        return "Yes"
    return "No"
        
print (checkArmstrongNumber(n))