"""
Binary Search
https://www.algoexpert.io/questions/Binary%20Search
​
Write a function that takes in a sorted array of integers as well as a target integer. The function should use the Binary Search algorithm to find if the target number is contained in the array and should return its index if it is, otherwise -1.
​
Sample input: [0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33
Sample output: 3"""

#  Solution 1: Recursive
# O(log(n)) time | O(log(n)) space due to recursive call stack

# def binarySearch(array, target):
#   return binarySearchHelper(array, target, 0, len(array) - 1)
  
# def binarySearchHelper(array, target, left, right):
#   if left > right:
#     return -1
#   middle = (left +right) //2 # rounding off the digit
#   potentialMatch = array[middle]
#   if target == potentialMatch:
#     return middle
#   elif target < potentialMatch:
#     return binarySearchHelper(array, target, left, middle-1)
#   elif target > potentialMatch:
#     return binarySearchHelper(array, target, middle+1, right)
  
# array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
# target = 72
 
# print(binarySearch(array, target))

# Solution 2:
# Iterative: O(log(n)) time | O(1) space
def binarySearch(array, target):
  left = 0
  right = len(array) -1
  while left <= right:
    middle = (left + right) // 2
    potentialMatch = array[middle]
    if target == potentialMatch:
      return middle
    elif target < potentialMatch:
      right = middle - 1
    else:
      left = middle + 1
  return -1

array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
target = 33
 
print(binarySearch(array, target))