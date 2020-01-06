# https://www.hackerrank.com/contests/smart-interviews/challenges/si-largest-palindromic-substring/problem

"""
Given a string, find the length of the largest palindromic substring.

Input Format

First line of input contains T - number of test cases. Its followed by 2T lines. The first line contains N - the size of the string and the second line contains a string of size N, containing only lowercase english alphabets. 

Constraints

30 points 
1 <= T <= 200 
1 <= len(S) <= 102 
'a' <= S[i] <= 'z' 

70 points 
1 <= T <= 200 
1 <= len(S) <= 103 
'a' <= S[i] <= 'z' 

Output Format

For each test case, print the length of the largest palindromic substring, separated by newline. 

Sample Input 0

5
8
pfyafafd
9
sllwffoqq
6
yoogvb
4
hcch
23
mzmqnnrkurfmmfrukrnnqsm
Sample Output 0

3
2
2
4
18"""


# Solution 1:
# O(N^2 * N)
# N^2 for two loops and N for palindrome

"""def solve(string, n):
    count = 0
    for i in range(n):
        for j in range(i, n):
            substring = string[i:j+1]
            isPalindrome = palindrome(substring)
            if isPalindrome:
                count = max(count, len(substring))
    return count
        

def palindrome(substring):
    n = len(substring)
    low = 0
    high = n -1
    while low < high:
        if substring[low] != substring[high]:
            return False
        low += 1
        high -= 1
    return True

t = int(input())
for tc in range(t):
    n = int(input())
    string = input()
    result = solve(string, n)
    print (result)"""
    

# Solution 2:
# O(n^2): By checking substring of even and odd (Expand Around Center)
def solve(A, n):
    if n == 0:
        return None
    longest_pal = ""
    for i in range(n):
        p1 = expandAroundCenter(A, i, i)
        if len(p1) > len(longest_pal):
            longest_pal = p1

        p2 = expandAroundCenter(A, i, i+1)
        if len(p2) > len(longest_pal):
            longest_pal = p2
    return len(longest_pal)


def expandAroundCenter(A, left, right):
    n = len(A)
    while left >=0 and right < n:
        if A[left] != A[right]:
            break
        left -=1
        right += 1
    return A[left+1: right]

t = int(input())
for tc in range(t):
    n = int(input())
    string = input()
    result = solve(string, n)
    print (result)

t = int(input())
for tc in range(t):
    n = int(input())
    string = input()
    result = solve(string, n)
    print (result)