"""Bubble Sort
​https://www.algoexpert.io/questions/Bubble%20Sort

Write a function that takes in an array of integers and returns a sorted version of that array. Use the Bubble Sort algorithm to sort the array.
​
Sample input: [8, 5, 2, 9, 5, 6, 3]
Sample output: [2, 3, 5, 5, 6, 8, 9]"""

# Hint:
"""Traverse the input array, swapping any two numbers that are out of order and keeping track of any swaps that you make. Once you arrive at the end of the array, check if you have made any swaps; if not, the array is sorted and you are done; otherwise, repeat the steps laid out in this hint until the array is sorted."""

# Time: O(n**2) | Space: O(1)
def bubbleSort(array):
  isSorted = False
  counter = 0
  while not isSorted:
    isSorted = True
    for i in range(len(array)-1 - counter):
      if array[i] > array[i+1]:
        swap(i, i+1, array)
        isSorted = False
    counter += 1 # This is to exclude already sorted numbers at the end
  return array

def swap(i, j, array):
  array[i], array[j] = array[j], array[i]
  
array = [8, 5, 2, 9, 5, 6, 3]
print (bubbleSort(array))
      