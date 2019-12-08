# https://www.hackerrank.com/contests/smart-interviews/challenges/si-trailing-zeros
# Count the number of trailing 0s in factorial of a given number. 
# Reference: https://www.geeksforgeeks.org/prime-factor/

t = int(input())
for p in range(t):
  n = int(input())
  count = 0
  i = 5
  while (n/i >= 1):
    count += int(n/i)
    i *= 5
  print (count)
