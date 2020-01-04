# https://www.geeksforgeeks.org/sum-of-fibonacci-numbers-in-a-range/
"""Given a range [l, r], the task is to find the sum fib(l) + fib(l + 1) + fib(l + 2) + ….. + fib(r) where fib(n) is the nth Fibonacci number.

Examples:

Input: l = 2, r = 5
Output: 11
fib(2) + fib(3) + fib(4) + fib(5) = 1 + 2 + 3 + 5 = 11



Input: l = 4, r = 8
Output: 50"""

def fibanocci(N):
  if N < 2:
    return N
  fib = [0 for i in range(N+1)]
  fib[0] = 0
  fib[1] = 1
  for i in range(2, N+1):
    fib[i] = fib[i-1] + fib[i-2]
    i += 1
  return fib[N]

def calculateSum(l, r): 
  
  # Using our deduced result 
  sum = fibanocci(r + 2) - fibanocci(l + 1)
  return sum
  
# Driver code 
l = 4
r = 8 
print(calculateSum(l, r))