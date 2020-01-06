# https://www.geeksforgeeks.org/sum-of-fibonacci-numbers-in-a-range/
"""Given a range [l, r], the task is to find the sum fib(l) + fib(l + 1) + fib(l + 2) + ….. + fib(r) where fib(n) is the nth Fibonacci number.

Examples:

Input: l = 2, r = 5
Output: 11
fib(2) + fib(3) + fib(4) + fib(5) = 1 + 2 + 3 + 5 = 11



Input: l = 4, r = 8
Output: 50"""

# Solution:
"""
Efficient approach: The idea is to find the relationship between the sum of Fibonacci numbers and nth Fibonacci number and use Binet’s Formula to calculate its value.

Relationship Deduction

F(i) refers to the ith Fibonacci number.
S(i) refers to sum of Fibonacci numbers till F(i).
We can rewrite the relation F(n + 1) = F(n) + F(n – 1) as below:
F(n – 1) = F(n + 1) – F(n)
Similarly,
F(n – 2) = F(n) – F(n – 1)
…
…
…
F(0) = F(2) – F(1)

Adding all the equations, on left side, we have
F(0) + F(1) + … + F(n – 1) which is S(n – 1)
Therefore,
S(n – 1) = F(n + 1) – F(1)
S(n – 1) = F(n + 1) – 1
S(n) = F(n + 2) – 1

In order to find S(n), simply calculate the (n + 2)th Fibonacci number and subtract 1 from the result.
Therefore,
S(l, r) = S(r) – S(l – 1)
S(l, r) = F(r + 2) – 1 – (F(l + 1) – 1)
S(l, r) = F(r + 2) – F(l + 1)"""

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