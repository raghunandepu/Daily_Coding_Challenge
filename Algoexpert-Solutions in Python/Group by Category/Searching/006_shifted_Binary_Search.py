# https://www.algoexpert.io/questions/Shifted%20Binary%20Search
"""
Shifted Binary Search
​
Write a function that takes in a sorted array of integers as well as a target integer. The caveat is that the numbers in the array have been shifted by some amount; in other words, they have been moved to the left or the right by one or more positions. For example, [1, 2, 3, 4] might become [3, 4, 1, 2]. The function should use a variation of the Binary Search algorithm to find if the target number is contained in the array and should return its index if it is, otherwise -1.
​
Sample input: [45, 61, 71, 72, 73, 0, 1, 21, 33, 45], 33
Sample output: 8"""

# Recursive way: O(logn) time | O(logn) space
def shiftedBinarySearch(array, target):
  return shiftedBinarySearchHelper(array, target, 0, len(array)-1)

def shiftedBinarySearchHelper(array, target, leftIdx, rightIdx):
  if leftIdx > rightIdx:
    return -1
  mid = (leftIdx + rightIdx) // 2
  potentialMatch = array[mid]
  leftNum = array[leftIdx]
  rightNum = array[rightIdx]
  if target == potentialMatch:
    return mid
  elif leftNum <= potentialMatch:
    if target < potentialMatch and target >= leftNum:
      return shiftedBinarySearchHelper(array, target, leftIdx, mid -1) # explore only left half of the array
    else:
      return shiftedBinarySearchHelper(array, target, mid+1, rightIdx)
  else:
    if target > potentialMatch and target <= rightNum:
      return shiftedBinarySearchHelper(array, target, mid+1, right)
    else:
      return shiftedBinarySearch(array, target, leftIdx, mid - 1)
    
    
# Iterative way: O(logn) time | O(1) space
def shiftedBinarySearch(array, target):
  return shiftedBinarySearchHelper(array, target, 0, len(array)-1)

def shiftedBinarySearchHelper(array, target, leftIdx, rightIdx):
  while left <= right:
    mid = (leftIdx + rightIdx) // 2
    potentialMatch = array[mid]
    leftNum = array[leftIdx]
    rightNum = array[rightIdx]
    if target == potentialMatch:
      return mid
    elif leftNum <= potentialMatch: # if left half is sorted
      if target < potentialMatch and target >= leftNum:
        rightIdx = mid - 1 # explore only left half of the array
      else:
        leftIdx = mid + 1
    else: # if left half is not sorted, check right half
      if target > potentialMatch and target <= rightNum:
        leftIdx = mid + 1
      else:
        rightIdx = mid - 1
  return -1
  