# https://www.hackerrank.com/contests/smart-interviews/challenges/si-reverse-the-sentence/problem
"""
Given a sentence, reverse the entire sentence word-by-word. 
Note: Solve using stack or in-place swap. Do not simply scan, split and print in reverse order.

Input Format

First line of input contains T - number of test cases. Its followed by T lines, each contains a sentence S of space separated words of lowercase english alphabet. All the words are separated by a single space. 

Constraints

1 <= T <= 1000 
1 <= len(S) <= 1000 

Output Format

For each test case, print the reversed sentence, separated by newline. 

Sample Input 0

3
hello world
a b c d
data structures and algorithms
Sample Output 0

world hello
d c b a
algorithms and structures data
Explanation 0

Self Explanatory"""

def solve(s):
    s = s.split()
    left = 0
    right = len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return s

    
t = int(input())
for tc in range(t):
    s = input()
    result = solve(s)
    print (*result)

