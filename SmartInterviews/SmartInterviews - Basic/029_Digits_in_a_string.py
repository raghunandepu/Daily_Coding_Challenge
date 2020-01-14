# https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-digits-in-a-string/copy-from/1319390026

"""
Given a string, check if it contains only digits.

Input Format

Input contains a string - S.

Constraints

1 <= len(S) <= 100

Output Format

Print "Yes" if string contains only digits, "No" otherwise.

Sample Input 0

123456786543
Sample Output 0

Yes"""

n = input()
def solve(n):
    for e in str(n):
        if ord(str(e)) not in range(48, 58): # ascii range of numbers [48, 57]
            return "No"
    return "Yes"
            

print (solve(n))