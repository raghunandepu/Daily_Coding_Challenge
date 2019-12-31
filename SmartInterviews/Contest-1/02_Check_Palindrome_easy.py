# https://www.hackerrank.com/contests/smart-interviews-14a/challenges/si-check-palindrome
"""
Given a string, check if its a palindrome.

Input Format

First line of input contains T - number of test cases. Its followed by 2T lines, the first line contains N - the size of the string. The second line contains a string of N characters. 

Constraints

1 <= T <= 1000 
1 <= N <= 1000 
'a' <= str[i] <= 'z' 

Output Format

For each test case, print "Yes" if the string is a palindrome, "No" otherwise, separated by new line.

Sample Input 0

2
5
madam
6
tester
Sample Output 0

Yes
No
Explanation 0

Self Explanatory"""

def solve(n, str):
    left = 0
    right = n - 1
    while left < right:
        if str[left] != str[right]:
            return "No"
        left += 1
        right -= 1
    return "Yes"

        

t = int(input())
for tc in range(t):
    n = int(input())
    string = input()
    result = solve(n, string)
    print (result)