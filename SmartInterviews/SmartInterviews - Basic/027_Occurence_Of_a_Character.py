# https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-occurrence-of-a-character-1/problem

"""
Given a sentence and a character, count occurrence of the given character in the sentence. All characters in the sentence are lower case.

Input Format

First line of input contains a sentence - S and second line of input contains a lowercase character - ch.

Constraints

1 <= len(S) <= 100
'a' <= ch <= 'z'

Output Format

Print count of the given character in the sentence.

Sample Input 0

You're a good person.
o
Sample Output 0

4"""

s = input()
target_char = input()

def solve(s, target_char):
    count = 0
    for i in range(len(s)):
        if s[i] == target_char:
            count += 1
    return count

print (solve(s, target_char))