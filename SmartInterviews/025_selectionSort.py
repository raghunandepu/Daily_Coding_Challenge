def selectionSort(array):
    swappedIdx = []
    for i in range(len(array)-1, -1, -1):
        maxIdx = i
        for j in range(0, i):
            if array[j] >= array[maxIdx]:
                maxIdx = j
               
        swappedIdx.append(maxIdx)
        array[i], array[maxIdx] = array[maxIdx], array[i]
        
    return swappedIdx[:n-1]
    

t = int(input())
for tc in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print (*selectionSort(arr))