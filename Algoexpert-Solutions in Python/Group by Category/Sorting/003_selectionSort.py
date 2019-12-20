
# O(n**2) time | O(1) space
def selectionSort(array):
  swappedIdx = []
  for i in range(len(array)):
    minIdx = i
    for j in range(i+1, len(array)):
      if array[minIdx] > array[j]:
        minIdx = j
    swap(i, minIdx, array)
    swappedIdx.append(minIdx)
  return array
    
def swap(i, j, array):
  array[i], array[j] = array[j], array[i]

array = [-3, 0, 7, 5, 4, 0, -3]
print (selectionSort(array))