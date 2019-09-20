# Duplicates in an array problem overview

"""The problem is that we want to find duplicates in a one-dimensional array of integers in O(N) running time where the integer values are smaller than the length of the array!"""
# Solution:

""" 
  Approach 1) We can use brute force approach (comparing items with all the rest) but it takes O(N**2) run time
  Approach 2) We can use hashmaps. Traverse the given array and try to insert each item in a hastable with the value as the key. If you can not insert the item, it means it is a duplicate.
  Problem with this approach: It is not in-place algorithm"""

# Approach 3

# Using absolute values approach, we can acheive this in O(N)
# check the sign of arr[abs(arr(i))] . If it is positive, flip the sign, it means there is a value with that index already. During traversal, if we encounter - sign again, it means it is a reapetition.

def duplicates(nums):
  for num in nums:
    if nums[abs(num)] >= 0:
      nums[abs(num)] = -nums[abs(num)]
    else:
      print("Repetition found: ", abs(num))

if __name__ == "__main__":
  nums = [2,6, 3, 5, 1, 4, 2, 1]
  duplicates(nums)
  
  

  