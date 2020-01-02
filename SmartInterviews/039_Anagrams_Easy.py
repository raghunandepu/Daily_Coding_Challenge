# https://www.hackerrank.com/contests/smart-interviews/challenges/si-check-anagrams/

"""
Given 2 strings, check if they are anagrams. An anagram is a rearrangement of the letters of one word to form another word. In other words, some permutation of string A must be same as string B.

Input Format

First line of input contains T - number of test cases. Its followed by T lines, each line containing 2 space separated strings.

Constraints

10 points 
1 <= T <= 100 
1 <= len(S) <= 103 
'a' <= S[i] <= 'z' 

40 points 
1 <= T <= 100 
1 <= len(S) <= 105 
'a' <= S[i] <= 'z' 

Output Format

For each test case, print True/False, separated by newline. 

Sample Input 0

4
a a
b h
stop post
hi hey
Sample Output 0

True
False
True
False"""

def anagramCheck(s1, s2):
    if len(s1) != len(s2):
        return False
    dict1 = {}
    
    for c1 in s1:
        if c1 not in dict1:
            dict1[c1] = 1
        else:
            dict1[c1] += 1
    
    for c2 in s2:
        if c2 not in dict1:
            return False
        else:
            dict1[c2] -= 1
    
    for val in dict1.values():
        if val != 0:
            return False
    return True
        

t = int(input())
for tc in range(t):
    s1, s2 = map(str, input().split())
    result = anagramCheck(s1, s2)
    print (result)