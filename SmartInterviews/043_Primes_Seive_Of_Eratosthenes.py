# Find all primes from 1 to N included.

# Time complexity: O(n*log(logn)) for sleeve of eratoshenes
# Refer for theory: https://www.geeksforgeeks.org/sieve-of-eratosthenes/

import math
def primesgenerator(n):
  primes = [True for _ in range(n+1)]
  primes[0] = primes[1] = False # Since we know 0 and 1 are not prime numbers
  for i in range(2, int(math.sqrt(n))+1):
    if primes[i] is True:
      for j in range(i*i, n+1, i):
        primes[j] = False
  
  result = []
  for k, ele in enumerate(primes):
    if ele is True:
      result.append(k)
  return result
  
result = primesgenerator(30)
result = ' '.join(map(str, result))
print (result)
  