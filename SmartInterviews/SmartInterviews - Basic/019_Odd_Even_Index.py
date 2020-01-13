# https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-odd-even-index/problem
"""
Given a String, print all the letters present at odd index followed by the letters present at even index.

Input Format

Input contains a string - S.

Constraints

1 <= len(S) <= 100

Output Format

Print letters present at odd index followed by the letters present at even index.

Sample Input 0

afdg5tg
Sample Output 0

fgtad5g
Explanation 0

Self Explanatory"""

s = input()
def oddEvenIndex(s):
    
    for i in range(1, len(s), 2):
        print (s[i], end ='')
    for i in range(0,len(s),2):
        print (s[i], end ='')
    
        
oddEvenIndex(s)