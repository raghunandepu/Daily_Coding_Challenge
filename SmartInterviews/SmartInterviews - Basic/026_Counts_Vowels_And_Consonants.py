# https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-count-vowels-and-consonants/problem

"""
Given a string, print count of vowels and consonants of the string.

Input Format

Input contains a string of upperscase and lowercase characters - S.

Constraints

1 <= len(S) <= 100

Output Format

Print count of vowels and consonants for the given string, separated by space.

Sample Input 0

abxbbiaaspw
Sample Output 0

4 7"""

s = input()

def solve(s):
    consonants = 0
    vowels = 0
    for ele in s:
        if ele not in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            consonants += 1
        else:
            vowels += 1
    print (str(vowels) +' '+str(consonants))

solve(s)