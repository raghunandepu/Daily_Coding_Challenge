"""
Given an array A[], write a function that segregates even and odd numbers. The functions should put all even numbers first, and then odd numbers.

Example:

Input  = {12, 34, 45, 9, 8, 90, 3}
Output = {12, 34, 8, 90, 45, 9, 3}
In the output, the order of numbers can be changed, i.e., in the above example, 34 can come before 12 and 3 can come before 9."""
# https://www.geeksforgeeks.org/segregate-even-and-odd-numbers/

# Solution:
"""
Algorithm: segregateEvenOdd()
1) Initialize two index variables left and right:  
            left = 0,  right = size -1 
2) Keep incrementing left index until we see an odd number.
3) Keep decrementing right index until we see an even number.
4) If lef < right then swap arr[left] and arr[right]"""

def segreateEvenOdd(arr):
  left, right = 0, len(arr)-1
  while left < right:
    while (arr[left] % 2 == 0 and left < right):
      left += 1
    while (arr[right] %2 == 1 and left < right):
      right -= 1
    if (left < right):
      arr[left], arr[right] = arr[right], arr[left]
      left += 1
      right -= 1
  return arr

# Driver function to test above function 
arr = [12, 34, 45, 9, 8, 90, 3] 

segreateEvenOdd(arr) 
print ("Array after segregation ")
for i in range(0, len(arr)):
  print (arr[i], end=' ')
print()