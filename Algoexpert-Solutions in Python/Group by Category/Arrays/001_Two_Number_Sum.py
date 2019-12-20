# https://www.algoexpert.io/questions/Two%20Number%20Sum
"""Two Number Sum
​
Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. If any two numbers in the input array sum up to the target sum, the function should return them in an array. If no two numbers sum up to the target sum, the function should return an empty array. Assume that there will be at most one pair of numbers summing up to the target sum.
​
Sample input: [3, 5, -4, 8, 11, 1, -1, 6], 10
Sample output: [-1, 11]
​"""

def twoNumberSum(array, targetSum):
    array.sort()
    leftIdx = 0
    rightIdx = len(array) - 1
    while leftIdx < rightIdx:
        currentSum = array[leftIdx] + array[rightIdx]
        if currentSum == targetSum:
            return [array[leftIdx], array[rightIdx]]
        elif currentSum < targetSum:
            leftIdx += 1
        elif currentSum > targetSum:
            rightIdx -= 1

    return []