# https://www.interviewbit.com/problems/3-sum/
"""
3 Sum
Asked in:  
Facebook
Amazon
Microsoft

Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. 
Return the sum of the three integers.

Assume that there will only be one solution

Example: 
given array S = {-1 2 1 -4}, 
and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2)"""

# O(n^2) time | O(n) space
import sys

A = [-1, 2, 1, -4]
B = 2

def threeSumClosest(A, B):
  A.sort()
  closestSum = sys.maxsize
  for i in range(len(A) -2):
    left = i+1
    right = len(A) -1
    while left < right:
      curentSum = A[i] + A[left] + A[right]
      
      if abs(B - curentSum) < abs(B - closestSum):
        closestSum = curentSum
        
      if curentSum > B:
        right -= 1
      else:
        left += 1
  return closestSum
  
  
print(threeSumClosest(A,B))