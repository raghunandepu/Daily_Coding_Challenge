"""Find Three Largest Numbers
​
Write a function that takes in an array of integers and returns a sorted array of the three largest integers in the input array. Note that the function should return duplicate integers if necessary; for example, it should return [10, 10, 12] for an input array of [10, 5, 9, 10, 12].
​
Sample input: [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
Sample output: [18, 141, 541]
​
"""
# Time : O(n) | Space: O(1)
# Hint : Try traversing the input array and updating the three largest numbers if necessary by shifting them accordingly.

def findThreeLargestNumbers(array):
  threeLargest = [None, None, None]
  for num in array:
    updateLargest(threeLargest, num)
  return threeLargest

def updateLargest(threeLargest, num):
  if threeLargest[2] == None or num > threeLargest[2]:
    shiftAndUpdate(threeLargest, num, 2) #Todo
  elif threeLargest[1] == None or num > threeLargest[1]:
    shiftAndUpdate(threeLargest, num, 1) # Todo
  elif threeLargest[0] == None or num > threeLargest[0]:
    shiftAndUpdate(threeLargest, num, 1) # todo
    
def shiftAndUpdate(array, num, idx):
  # indices [0, 1, 2]
  # array [x, y, z] will be shifted as [y, z, num] when index is 2
  for i in range(idx+1):
    if i == idx:
      array[i] = num
    else:
      array[i] = array[i+1]
  
array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]

print (findThreeLargestNumbers(array))