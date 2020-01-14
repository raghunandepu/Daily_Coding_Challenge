# https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-vowels-in-a-string/problem

"""
Given a string, check if it contains only vowels.

Input Format

Input contains a string of lowercase and uppercase characters- S.

Constraints

1 <= len(S) <= 100

Output Format

Print "Yes" if string contains only vowels, "No" Otherwise.

Sample Input 0

askhtwsflk
Sample Output 0

No"""

s = input()
def vowelCheck(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for char in s:
        if char not in vowels:
            return "No"
    return "Yes"

print (vowelCheck(s))