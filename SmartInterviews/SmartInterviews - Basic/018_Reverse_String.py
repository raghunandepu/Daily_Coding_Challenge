# https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-reverse-string/problem

"""
Given a string, reverse the given string.

Input Format

Input contains a String - S.

Constraints

1 <= len(s) <= 100

Output Format

Print the reversed string.

Sample Input 0

fdsrd
Sample Output 0

drsdf
Explanation 0

Self Explanatory"""

s = input()
def reverseString(s) -> None:
    start = 0
    end = len(s)-1
    s_new = [] # Taking list here as string can't be modified directly
    for c in s:
        s_new.append(c)
 
    while end > start:
        s_new[start], s_new[end] = s_new[end], s_new[start]
        start += 1
        end -= 1
    return s_new

result = reverseString(s)
for c in result:
    print (c, end ='')