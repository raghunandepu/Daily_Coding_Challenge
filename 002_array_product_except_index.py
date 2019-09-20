"""
This problem was asked by Uber.
 
Given an array of integers, return a new array such that each element at index i of the new array is the product of
all the numbers in the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. 
If our input was [3, 2, 1], the expected output would be [2, 3, 6].
Follow-up: what if you can't use division?
"""

# Solution
# Reference: https://www.interviewcake.com/question/python3/product-of-other-numbers 
"""
The product of all the integers except the integer at each index can be broken down into two pieces:

the product of all the integers before each index and
the product of all the integers after each index.
"""

def get_array_product_except_index(arr):
  if len(arr) < 2:
     raise IndexError('To get the product, we need atlest 2 elements in the list')
   
   # We make a list with length of input to hold the products
  products_expect_index = [None] * len(arr)
   
  # For each integer, we find the product of all the integers
  # before it (left half) and store the total product so far 
  # setting it 1 as there are no elements before first element to multiply
  
  product_so_far = 1
  for i in range(len(arr)):
    products_expect_index [i] = product_so_far
    product_so_far *= arr[i]


  # For each integer, we find the product of all the integers
  # after it. Since each index in product already has the 
  # product of all the integers before it, now we'are storing the total product of all other integers

  # We traverse through the list backwards and calcuate the product using the already calucated product above.
  product_so_far = 1
  for i in range(len(arr) -1, -1, -1):
    products_expect_index[i] *= product_so_far
    product_so_far *= arr[i]
    
  return products_expect_index
   
  
   
arr = [1, 2, 3, 4, 5]
print ("Input :  ", arr)
print ("Output: ", get_array_product_except_index(arr))

"""
Complexity: 

O(n) time and
O(n) space. 

We make two passes through our input a list, and the list we build always has the same length as the input list.

"""