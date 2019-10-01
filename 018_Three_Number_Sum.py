"""
Three Number Sum
https://www.algoexpert.io/questions/Three%20Number%20Sum
​
Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. The function should find all triplets in the array that sum up to the target sum and return a two-dimensional array of all these triplets. The numbers in each triplet should be ordered in ascending order, and the triplets themselves should be ordered in ascending order with respect to the numbers they hold. If no three numbers sum up to the target sum, the function should return an empty array.
​
Sample input: [12, 3, 1, 2, -6, 5, -8, 6], 0
Sample output: [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]
"""
# Solution:
# HINT: Try sorting the array and traversing it once. At each number, place a left pointer on the number immediately to the right of your current number and a right pointer on the final number in the array. Check if the current number, the left number, and the right number sum up to the target sum. 

# Time: O(n**2), Space: O(n)
def threeNumberSum(array, targetSum):
  array.sort()
  triplets = []
  for i in range(len(array)-2):
    left = i +1
    right = len(array)-1
    while left < right:
      currentSum = array[i] + array[left] + array[right]
      if currentSum == targetSum:
        triplets.append([array[i], array[left], array[right]])
        left += 1
        right -= 1
      elif currentSum < targetSum:
        left += 1
      elif currentSum > targetSum:
        right -=1
  return triplets

array = [12, 3, 1, 2, -6, 5, -8, 6]
print (threeNumberSum(array, 0))