#This is to exclude already sorted numbers at the end

def bubbleSort(array):
  isSorted = False
  counter = 0
  total_swaps = 0
  while not isSorted:
    isSorted = True
    for i in range(len(array)-1):
      if array[i] > array[i+1]:
        total_swaps += 1
        swap(i, i+1, array)
        isSorted = False
    counter += 1 # #This is to exclude already sorted numbers at the end
  return array

def swap(i, j, array):
	array[i], array[j] = array[j], array[i]
  
t = int(input())
for tc in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print (bubbleSort(arr))