# https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-binary-search-on-array/problem

"""
Implement binary search. Given a sorted array, search key in the array. If key not found print "false", otherwise print "true".

Input Format

First line of input contains two integers N and K. N is the size of array and K is the key. Second line contains array elements.

Constraints

1 <= N <= 102 
0 <= ar[i] <= 109

Output Format

Print "true" if key is present in the array. Otherwise, print false.

Sample Input 0

5 19
2 19 23 35 38
Sample Output 0

true
Explanation 0

Self Explanatory"""


N, K = map(int, input().split())
arr = list(map(int, input().split()))

def binarySearch(arr, N, K):
    low = 0
    high = N - 1
    while low <= high:
        mid = (low + high) // 2
        if K == arr[mid]:
            return "true"
        if K > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return "false"

print (binarySearch(arr, N, K))