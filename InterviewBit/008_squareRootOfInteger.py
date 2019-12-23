# https://www.interviewbit.com/problems/square-root-of-integer/

"""
Square Root of Integer
Asked in:  
Facebook
Amazon
Microsoft

Given an integer A.

Compute and return the square root of A.

If A is not a perfect square, return floor(sqrt(A)).

DO NOT USE SQRT FUNCTION FROM STANDARD LIBRARY



Input Format

The first and only argument given is the integer A.
Output Format

Return floor(sqrt(A))
Constraints

1 <= A <= 10^9
For Example

Input 1:
    A = 11
Output 1:
    3

Input 2:
    A = 9
Output 2:
    3
"""

import math
def sqrt(A):
  
    # Base cases
    if (A == 0 or A == 1):
      return A
    
    low = 1
    high = A
    while (low <= high):
        mid = (low + high) // 2
        
        x = mid * mid
        if x == A: 
            return mid
          
        # Since we need floor, we update  
        # answer when mid*mid is smaller 
        # than A, and move closer to sqrt(A)  
        if x < A:
            low = mid + 1
            ans = mid
        else:
            high = mid - 1
    return ans
  
  
A = 11
print (sqrt(A))