def insertionSort(array):
    # Write your code here.
    result_index = []
    for i in range(1, len(array)):
        j = i
        while (j > 0 and array[j] < array[j-1]):
            swap(j, j-1, array)
            j -= 1
        result_index.append(j)
    return result_index

def swap (i, j, array):
    array[i], array[j] = array[j], array[i]
    
t = int(input())
for tc in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(*insertionSort(arr)) # '*' - To print the elements without list seperated by space