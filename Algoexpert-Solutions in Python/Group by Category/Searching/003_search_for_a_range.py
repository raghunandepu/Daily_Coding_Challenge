# https://www.algoexpert.io/questions/Search%20For%20Range
"""
Search For Range

# Asked in Google, Microsoft
​
Write a function that takes in a sorted array of integers as well as a target integer. The function should use a variation of the Binary Search algorithm to find a range of indices in between which the target number is contained in the array and should return this range in the form of an array. The first number in the output array should represent the first index at which the target number is located while the second number should represent the last index at which the target number is located. The function should return [-1, -1] if the number is not contained in the array.
​
Sample input: [0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73], 45
Sample output: [4, 9]"""

# Solution 1: Recursive way of binary search
# O(log(n)) time | O(log(n)) space due to recursive call stacks

"""def searchForRange(array, target):
  finalRange = [-1, -1]
  alteredBinarySearch(array, target, 0, len(array) - 1, finalRange, True)
  alteredBinarySearch(array, target, 0, len(array) - 1, finalRange, False)
  return finalRange

def alteredBinarySearch(array, target, left, right, finalRange, goLeft):
  if left > right:
    return
  mid = (left + right) // 2
  if array[mid] < target:
    alteredBinarySearch(array, target, mid+1, right, finalRange, goLeft)
  elif array[mid] > target:
    alteredBinarySearch(array, target, left, mid-1, finalRange, goLeft)
  
  else:
    if goLeft:
      if mid == 0 or array[mid - 1] != target:
        finalRange[0] = mid
      else:
        alteredBinarySearch(array, target, left, mid-1, finalRange, goLeft)
        
    else:
      if mid == len(array) -1  or array[mid + 1] != target:
        finalRange[1] = mid
      else:
        alteredBinarySearch(array, target, mid+1, right, finalRange, goLeft)"""
        
        
# Solution 2:
# Iterative way of altered binary search

# O(log(n)) time | O(1)

def searchForRange(array, target):
  finalRange = [-1, -1]
  alteredBinarySearch(array, target, 0, len(array) - 1, finalRange, True)
  alteredBinarySearch(array, target, 0, len(array) - 1, finalRange, False)
  return finalRange

def alteredBinarySearch(array, target, left, right, finalRange, goLeft):
  while left <= right:
    mid = (left + right) // 2
    if array[mid] < target:
      left = mid + 1
    elif array[mid] > target:
      right = mid - 1
    
    else:
      if goLeft:
        if mid == 0 or array[mid - 1] != target:
          finalRange[0] = mid
          return
        else:
          right = mid - 1
          
      else:
        if mid == len(array) -1  or array[mid + 1] != target:
          finalRange[1] = mid
          return
        else:
          left = mid + 1
          

        
      
    
  
  