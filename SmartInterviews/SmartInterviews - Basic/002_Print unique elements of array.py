# https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-print-unique-elements-of-array

"""
Print unique elements of the array in the same order as they appear in the input. 
Note: Do not use any inbuilt functions/libraries for your main logic.

Input Format

First line of input contains a single integer N - the size of array and second line contains array elements.

Constraints

1 <= N <= 100
0 <= ar[i] <= 109 


Output Format

Print unique elements of the array.

Sample Input 0

7
5 4 10 9 21 4 10
Sample Output 0

5 9 21
Explanation 0

Self Explanatory."""

def solve(arr, n):
    res = {}
    for ele in arr:
        if ele in res:
            res[ele] += 1
        else:
            res[ele] = 1

    unique_elements = []
    for k in res.keys():
        if res[k] == 1:
            unique_elements.append(k)
    return unique_elements 

n = int(input())
arr = list(map(int, input().split()))
print (*solve(arr, n))

