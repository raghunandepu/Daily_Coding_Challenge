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
def solve(string, n):
    currentLargest = [0, 1]
    for i in range(1,n):
        odd = palindrome(string, i-1, i+1)
        even = palindrome(string, i-1, i)
        largest = max(odd, even, key=lambda x: x[1] - x[0])
        currentLargest = max(largest, currentLargest, key=lambda x: x[1]-x[0])
        
    return len(string[currentLargest[0]:currentLargest[1]])
        

def palindrome(string, leftIdx, rightIdx):
    n = len(string)

    while leftIdx >=0 and rightIdx < n:
        if string[leftIdx] != string[rightIdx]:
            break
        leftIdx -= 1
        rightIdx += 1
    return [leftIdx+1, rightIdx]

t = int(input())
for tc in range(t):
    n = int(input())
    string = input()
    result = solve(string, n)
    print (result)