# https://www.interviewbit.com/problems/longest-palindromic-substring/
"""
Longest Palindromic Substring
Asked in:  
Amazon
Microsoft
Groupon
Bookmark Suggest Edit
Given a string S, find the longest palindromic substring in S.

Substring of string S:

S[i...j] where 0 <= i <= j < len(S)

Palindrome string:

A string which reads the same backwards. More formally, S is palindrome if reverse(S) = S.

Incase of conflict, return the substring which occurs first ( with the least starting index ).

Example :

Input : "aaaabaaa"
Output : "aaabaaa"
"""

class Solution:
    # @param A : string
    # @return a strings
    def longestPalindrome(self, A):
        if len(A) == 0:
            return None
        longest_pal = ""
        for i in range(len(A)):
            p1 = self.expandAroundCenter(A, i, i)
            if len(p1) > len(longest_pal):
                longest_pal = p1
                
            p2 = self.expandAroundCenter(A, i, i+1)
            if len(p2) > len(longest_pal):
                longest_pal = p2
        return longest_pal
            
        
    def expandAroundCenter(self, A, left, right):
        while left >=0 and right < len(A):
            if A[left] != A[right]:
                break
            left -=1
            right += 1
        return A[left+1: right]
