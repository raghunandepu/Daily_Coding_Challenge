"""
Problem:
This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
Bonus: Can you do this in one pass?

"""

# Solution 1
"""
def findPairs(arr, sum):
  # Traverses through list twice to compare one element with the rest and find the sum
  for i in range(0, len(arr)):
    for j in range(0, len(arr)):
      if sum == arr[i] + arr[j]:
        return True
  return False
"""

# Solution 2

def findPairs(arr, sum):
  
  #Traverse through the list
  for i in range(0, len(arr)):
    if sum-i in arr:
      return True
  return False


# Test
A = [10, 15, 3, 7]
print (findPairs(A, 17))


