# Cisco Interview Question

"""
Problem Statement:

Given two strings A and B, return whether or not A can be shifted some number of times to get B.
 
For example, if A is abcde and B is cdeab, return true. If A is abc and B is acb, return false.
 
# Solution:

If the strings are not the same length, then we can immediately return false"

cleaner way to solve this might be to concatenate one of the strings to itself (like a + a), and try looking for the other string in this concatenated string. If the string is shifted, we should find it in the concatenated string."""

def isShifted(a,b):
  if len(a) != len(b):
    return False
  return b in a + a