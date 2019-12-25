def quickSort(array):
  quickSortHelper(array, 0, len(array) -1)
  return array
  
  
def quickSortHelper(array, startIdx, endIdx):
  if startIdx >= endIdx:
    return
  pivotIdx = startIdx
  leftIdx = startIdx + 1
  rightIdx = endIdx
  while rightIdx >= leftIdx:
    if array[leftIdx] > array[pivotIdx] and array[rightIdx] < array[pivotIdx]:
      swap(leftIdx, rightIdx, array)
    if array[leftIdx] <= array[pivotIdx]:
      leftIdx += 1
    if array[rightIdx] >= array[pivotIdx]:
      rightIdx -= 1
  swap(pivotIdx, rightIdx, array) # swap pivot with right when left pointer crosses right.
  
  leftSubarrayIsSmaller = rightIdx - 1 - startIdx < endIdx - (rightIdx + 1)
  if leftSubarrayIsSmaller:
    quickSortHelper(array, startIdx, rightIdx - 1) # we apply QS first on left subarray
    quickSortHelper(array, rightIdx + 1, endIdx) # Then on right sub array
    
  else:
    quickSortHelper(array, rightIdx + 1, endIdx)
    quickSortHelper(array, startIdx, rightIdx - 1)
    
def swap(i,j, array):
  array[i], array[j] = array[j], array[i]


array = [8, 5, 2, 9, 5, 6, 3]
print (quickSort(array))
  
    
      
    
  