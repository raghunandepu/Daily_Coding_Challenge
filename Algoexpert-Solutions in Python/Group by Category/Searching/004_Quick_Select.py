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


def quickselect(array, k):
    array.sort()
    return array[k-1]
  
array = [8, 5, 2, 9, 7, 6, 3]
k = 3

print (quickselect(array, k))