# https://www.hackerrank.com/contests/smart-interviews/challenges/si-find-first-repeating-character/

"""
Given a string of characters, find the first repeating character.

Input Format

First line of input contains T - number of test cases. Its followed by T lines, each line contains a single string of characters. 

Constraints

1 <= T <= 1000 
'a' <= str[i] <= 'z'
1 <= len(str) <= 104

Output Format

For each test case, print the first repeating character, separated by newline. If there are none, print '.'. 

Sample Input 0

3
smartinterviews
algorithms
datastructures
Sample Output 0

s
.
a"""

def findRepeatingChar(s):
    for i,c in enumerate(s):
        if c in s[i+1:]:
            return c
    return "."

t = int(input())
for tc in range(t):
    s = input()
    result = findRepeatingChar(s)
    print (result)