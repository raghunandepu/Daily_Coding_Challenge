# https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-compute-fibonacci-number/problem

# Fibanocci Number:
"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.
Given N, calculate F(N)"""

# Recursive approach:
"""class Solution:
    def fib(self, N: int) -> int:
        if N <= 1:
            return N
        return self.fib(N-1) + self.fib(N-2)
      
Time complexity = O(2**N)"""

# Solution: Iterative approach with memoization (storing previous result) which is better than recursive approach.

def fibanocci(N: int) -> int:
  if N < 2:
    return N
  fib = [0 for i in range(N+1)]
  fib[0] = 0
  fib[1] = 1
  for i in range(2, N+1):
      fib[i] = fib[i-1] + fib[i-2]
      i+=1
  return fib[N]
  
print (fibanocci(4))

"""
Complexity Analysis:
-------------------- 
Time complexity: O(N) -  Each number, starting at 2 up to and including N, is visited, computed and then stored for O(1).

Space complexity: O(N) - The size of the data structure is proportionate to N."""