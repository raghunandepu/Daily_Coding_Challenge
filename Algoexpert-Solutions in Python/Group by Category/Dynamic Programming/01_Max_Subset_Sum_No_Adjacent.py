# https://www.algoexpert.io/questions/Max%20Subset%20Sum%20No%20Adjacent

"""
Maximum Subset Sum With No Adjacent Elements
​
Write a function that takes in an array of positive integers and returns an integer representing the maximum sum of non-adjacent elements in the array. If a sum cannot be generated, the function should return 0.
​
Sample input: [75, 105, 120, 75, 90, 135]
Sample output: 330 (75, 120, 135)"""

# Solution 1:

# Hint 1: Try building an array of the same length as the input array. At each index in this new array, store the maximum sum that can be generated using no adjacent numbers located between index 0 and the current index.

# Hint2: Can you come up with a formula that relates the max sum at index i to the max sums at indices i - 1 and i - 2?


# O(n) time | O(n) space

def maxSubsetSumNoAdjacent(array):
  if not len(array):
    return 0
  elif len(array) == 1:
    return array[0]
  maxSums = array[:] # Taking a copy of original array to build maxSum array
  maxSums[1] = max(array[0], array[1])
  for i in range(2, len(array)):
    maxSums[i] = max(maxSums[i-1], maxSums[i-2] + array[i])
  return maxSums[-1]

array = [75, 105, 120, 75, 90, 135]
print (maxSubsetSumNoAdjacent(array))

# Solution 2:
# Do you really need to store the entire array mentioned in Hint #1, or can you somehow store just the max sums that you need at any point in time?

# O(n) | O(1)
def maxSubsetSumNoAdjacent2(array):
  if not len(array):
    return 0
  elif len(array) == 1:
    return array[0]
  second = array[0]
  first = max(array[0], array[1])
  for i in range(2, len(array)):
    current = max(first, second + array[i])
    second = first
    first = current
  return first

array = [75, 105, 120, 75, 90, 135]
print (maxSubsetSumNoAdjacent2(array))
  