# https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-find-duplicate-element-in-array/problem

"""
Find a duplicate element in the given array of integers. There will be only a single duplicate element in the array.
Note: Do not use any inbuilt functions/libraries for your main logic.

Input Format

First line of input contains size of the array - N and second line contains the elements of the array.

Constraints

2 <= N <= 100
0 <= ar[i] <= 109 


Output Format

Print the duplicate element from the given array.

Sample Input 0

6
5 4 10 9 21 10
Sample Output 0

10
Explanation 0

Self Explanatory"""

def solve(arr, n):
    
    # populating counts in dictionary
    res = {}
    for ele in arr:
        if ele in res:
            res[ele] += 1
        else:
            res[ele] = 1
    
    for k in res.keys():
        if res[k] != 1:
            break
    return k
            

n = int(input())
arr = list(map(int, input().split()))
print (solve(arr, n))