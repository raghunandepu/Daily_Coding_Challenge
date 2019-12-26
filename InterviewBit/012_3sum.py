import sys

A = [-1, 2, 1, -4]
B = 2

def threeSumClosest(A, B):
  A.sort()
  closestSum = sys.maxsize
  for i in range(len(A) -2):
    left = i+1
    right = len(A) -1
    while left < right:
      curentSum = A[i] + A[left] + A[right]
      
      if abs(B - curentSum) < abs(B - closestSum):
        closestSum = curentSum
        
      if curentSum > B:
        right -= 1
      else:
        left += 1
  return closestSum
  
  
print(threeSumClosest(A,B))