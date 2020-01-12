# https://www.geeksforgeeks.org/search-in-row-wise-and-column-wise-sorted-matrix/

"""Input : mat[4][4] = { {10, 20, 30, 40},
                      {15, 25, 35, 45},
                      {27, 29, 37, 48},
                      {32, 33, 39, 50}};
              x = 29
Output : Found at (2, 1)

Input : mat[4][4] = { {10, 20, 30, 40},
                      {15, 25, 35, 45},
                      {27, 29, 37, 48},
                      {32, 33, 39, 50}};
              x = 100
Output : Element not found"""

# Complexity: O(N+M) where n is the number of rows and M is the number of columns

def search(matrix, target):
  
  # Choosing top right element to begin search
  n = len(matrix) # rows
  i = 0
  j = len(matrix[0]) - 1
  
  while (i < n and j >=0 ):
    if matrix[i][j] == target:
      print ("Element found at:", i,",",j)
      return 1
    
    if matrix[i][j] > target:
      j -= 1
    else:
      i += 1
  print ("Element not found")
  return 0
  
  
  # Driver Code 
mat = [ [10, 20, 30, 40], 
        [15, 25, 35, 45], 
        [27, 29, 37, 48], 
        [32, 33, 39, 50] ] 
search(mat, 29) 