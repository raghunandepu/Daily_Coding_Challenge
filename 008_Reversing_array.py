"""
The problem is that we want to reverse a T[] array in O(N) linear time complexity and we want the algorithm to be in-place as well!

For example: input is [1,2,3,4,5] then the output is [5,4,3,2,1]"""

# Solution:
# In place algorithms that reverses array in O(N) with no extra space

def array_reversal(arr):
  
  # pointer to the first item
  start_index = 0
  # pointer to the last time
  end_index = len(arr) - 1
  
  # while the end index is greater than the start index
  while end_index > start_index:
    #swap two items
    arr[start_index], arr[end_index] = arr[end_index], arr[start_index]
    
    #increment the start index
    start_index += 1
    
    # decrement the end index
    end_index -= 1
    
  return arr

if __name__ == "__main__":
  arr = [1, 2, 3, 4, 5]
  print (array_reversal(arr))