# https://www.interviewbit.com/problems/matrix-search/

"""
Matrix Search
Given a matrix of integers A of size N x M and an integer B.

Write an efficient algorithm that searches for integar B in matrix A.

This matrix A has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than or equal to the last integer of the previous row.
Return 1 if B is present in A, else return 0.

Note: Rows are numbered from top to bottom and columns are numbered from left to right.



Input Format

The first argument given is the integer matrix A.
The second argument given is the integer B.
Output Format

Return 1 if B is present in A, else return 0.
Constraints

1 <= N, M <= 1000
1 <= A[i][j], B <= 10^6
For Example

Input 1:
    A = 
    [ [1,   3,  5,  7],
      [10, 11, 16, 20],
      [23, 30, 34, 50]  ]
    B = 3
Output 1:
    1

Input 2:
    A = [   [5, 17, 100, 111]
            [119, 120,  127,   131]    ]
    B = 3
Output 2:
    0
"""
# Approach: Using Binary search 
class Solution:
  def searchInMatrix(self, matrix, target):
    if not matrix or target is None:
      return 0
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    low = 0
    high = rows * cols - 1
    
    while low <= high:
      mid = (low + high) // 2
      num = matrix[mid // cols] [int(mid % cols)] # mid/cols give row num, mid % col give col num
      if num == target:
        return 1
      elif num < target:
        low = mid + 1
      else:
        high = mid - 1
    return 0
  
if __name__ == "__main__":
  matrixSearch = Solution()
  A = [[1]]
  B = 1
  result = matrixSearch.searchInMatrix(A, B)
  print (result)
    