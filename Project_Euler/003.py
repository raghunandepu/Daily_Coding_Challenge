# https://projecteuler.net/problem=3

"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?"""

# Solution:
# Approach: 
# To determine if a number n is prime, we need to:
# 1. check whether n is evenly divisible by 2
# 2. check whether n is evenly divisible by one of the uneven numbers from 3 to sqrt(n) + 1
# 3. if neither 1 nor 2 apply, n is prime

# To find the largest prime factor of n, we repeatedly divide n by its smallest prime factor
# until we can't divide it further.

import math

def find_Smallest_Prime_Factor(n):
  upperBound = int(math.sqrt(n) + 1)
  for i in range(2, upperBound):
    if n % i  == 0:
      return i
  return n
  
def find_Largest_Prime_Factor(n):
  while True:
    smallestFactor = find_Smallest_Prime_Factor(n)
    if smallestFactor < n:
       n //= smallestFactor
    else:
      return n
    
result = find_Largest_Prime_Factor(600851475143)
print (result)