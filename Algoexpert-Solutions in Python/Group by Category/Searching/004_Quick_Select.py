# https://www.algoexpert.io/questions/Quickselect

"""
Quick Select
​
Write a function that takes in an array of distinct integers as well as an integer k and returns the kth smallest number in that array in linear time, on average. The array could be sorted, but isn't necessarily so.
​
Sample input: [8, 5, 2, 9, 7, 6, 3], 3
Sample output: 5
​
"""
# O(n) time and O(1) space
# as we will stop sorting when element is found.

def quickselect(array, k):
  position = k - 1
  return quickselectHelper(array, 0, len(array)-1, position)

def quickselectHelper(array, startIdx, endIdx, position):
  while True:
    if startIdx > endIdx:
      raise Exception("Your algorithm should never arrive here!")
    pivotIdx = startIdx
    leftIdx = startIdx + 1
    rightIdx = endIdx
    
    while leftIdx <= rightIdx:
      if array[leftIdx] > array[pivotIdx] and array[rightIdx] < array[pivotIdx]:
        swap(leftIdx, rightIdx, array)
      if array[leftIdx] <= array[pivotIdx]:
        leftIdx += 1
      if array[rightIdx] >= array[pivotIdx]:
        rightIdx -= 1
    swap(pivotIdx, rightIdx, array)
    
    # until now, this is like a regular quick sort.
    # Instead of calling quicksort on both subarrays, we can check the new position of our pivot number is at the correct position, kth smallest number in the array.
    
    if rightIdx == position:
      return array[rightIdx]
    elif rightIdx < position:
      startIdx = rightIdx + 1   # discard the left subarray
    else:
      endIdx = rightIdx - 1
    

def swap(i, j, array):
  array[i], array[j] = array[j], array[i]
  
array = [8, 5, 2, 9, 7, 6, 3]
k = 3

print (quickselect(array, k))
        
      

