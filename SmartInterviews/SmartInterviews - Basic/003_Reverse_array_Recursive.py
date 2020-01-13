# https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-reverse-array/submissions/code/1319344746

"""
Print array in reverse order.
Note: Try solving this using recursion. Do not use any inbuilt functions/libraries for your main logic.

Input Format

First line of input contains N - the size of the array and second line contains the elements of the array.

Constraints

1 <= N <= 100 
0 <= ar[i] <= 1018 


Output Format

Print array in reverse order.

Sample Input 0

5
2 19 8 15 4
Sample Output 0

4 15 8 19 2
Explanation 0

Self Explanatory"""


def reverseList(arr, n, start, end):
    if start >= end:
        return
    arr[start], arr[end] = arr[end], arr[start]
    reverseList(arr, n, start+1, end-1)
        
n = int(input())
arr = list(map(int, input().split()))
start = 0
end = n-1
reverseList(arr, n , start, end)
for ele in arr:
    print (ele, end=' ')