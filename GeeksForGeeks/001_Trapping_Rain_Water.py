# https://www.geeksforgeeks.org/trapping-rain-water/
"""
Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

Examples:

Input: arr[]   = {2, 0, 2}
Output: 2
Structure is like below
| |
|_|
We can trap 2 units of water in the middle gap.

Input: arr[]   = {3, 0, 0, 2, 0, 4}
Output: 10
Structure is like below
     |
|    |
|  | |
|__|_| 
We can trap "3*2 units" of water between 3 an 2,
"1 unit" on top of bar 2 and "3 units" between 2 
and 4. """

# Solution 1: Brute Force
# A Simple Solution is to traverse every array element and find the highest bars on left and right sides. Take the smaller of two heights. The difference between the smaller height and height of the current element is the amount of water that can be stored in this array element. Time complexity of this solution is O(n2)

def maxWater(arr, n):
  res = 0
  for i in range(1, n-1):
    # Find the max element on its left
    left = arr[i]
    for j in range(i):
      left = max(left, arr[j])
    
    # Find the max element on its right
    right = arr[i]
    for k in range(i+1, n):
      right = max(right, arr[k])
      
    res += min(left, right) - arr[i]
    
  return res

if __name__ == "__main__":
  arr = [0, 1, 0, 2, 1, 0,  1, 3, 2, 1, 2, 1]
  n = len(arr)
  print(maxWater(arr, n))
  
# Solution 2: 
# An Efficient Solution is to pre-compute highest bar on left and right of every bar in O(n) time. Then use these pre-computed values to find the amount of water in every array element.

def findWater(arr, n):
  # left[i] contains height of tallest bar to the 
  # left of i'th bar including itself 
  left = [0] * n
  
  # Right [i] contains height of tallest bar to 
  # the right of ith bar including itself
  right = [0] * n
  
  water = 0
  
  # Fill left array
  left[0] = arr[0]
  for i in range(1, n):
    left[i] = max(left[i-1], arr[i])
    
  # Fill right array
  right[n-1] = arr[n-1]
  for j in range(n-2, -1, -1):
    right[j] = max(right[j+1], arr[j])
    
  # Calculate the accumulated water element by element 
    # consider the amount of water on i'th bar, the 
    # amount of water accumulated on this particular 
    # bar will be equal to min(left[i], right[i]) - arr[i] .
  
  for i in range(n):
    water += min(left[i], right[i]) - arr[i]
    
  return water

# Driver program 
  
arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1] 
n = len(arr) 
print("Maximum water that can be accumulated is", findWater(arr, n)) 