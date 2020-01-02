# https://www.interviewbit.com/problems/palindrome-string/
"""
Palindrome String
Bookmark Suggest Edit
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Example:

"A man, a plan, a canal: Panama" is a palindrome.

"race a car" is not a palindrome.

Return 0 / 1 ( 0 for false, 1 for true ) for this problem"""


class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):
        s = []
        for c in A:
            if 'A' <= c <= 'Z' or 'a' <= c <= 'z' or '0' <= c <= '9':
                s.append(c)
        s = ''.join(s)
        s = s.lower()

        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return 0
            left += 1
            right -= 1
        return 1