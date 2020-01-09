# https://www.hackerrank.com/contests/smart-interviews/challenges/si-sum-of-subarrays

"""
Given an array of integers, answer queries of the form: [i, j] : Print the sum of array elements from A[i] to A[j], both inclusive.

Input Format

First line of input contains N - size of the array. The next line contains N integers - elements of the array. The next line contains Q - number of queries. Each of the next Q lines contains 2 space separated indexes: i and j. 

Constraints

30 points 
1 <= N,Q <= 10000

70 points 
1 <= N,Q <= 500000

General Constraints 
-109 <= A[i] <= 109
0 <= i <= j <= N-1

Output Format

For each query, print the sum of array elements from A[i] to A[j], both inclusive, separated by newline. 

Sample Input 0

10
1 30 13 -4 -5 12 -53 -12 43 100 
4
0 5
1 7
2 3
7 9
Sample Output 0

47
-19
9
131"""


# Solution 1:
# O(N * Q), O(1)  where N is the number of elements and Q for each query

"""def solve(arr, i, j):
    sum = 0 
    for k in range(i, j+1):
        sum += arr[i]
        i += 1
        
    return sum

n = int(input())
arr = list(map(int, input().split()))
queries_num = int(input())
for q in range(queries_num):
    i, j = map(int, input().split())
    result = solve(arr, i, j)
    print (result)"""
    
# Efficient solution using prefix sum (Cumulative sum)
# Time: O(N + Q)
# We need to calcuate cumulative sum array only once O(N) and constant operation for each query to retreive the sum from cumulative sum array.

def prefixSum(arr):
    """Function to calcuate cumulative sum of given array"""
    cumSumArr = [0 for _ in range(len(arr))]
    cumSumArr[0] = arr[0]
    for k in range(1,len(arr)):
        cumSumArr[k] = cumSumArr[k-1] + arr[k]
    return cumSumArr
        
def sumInRange(cumSumArr, arr, i, j):
    return cumSumArr[j] - cumSumArr[i] + arr[i]

n = int(input())
arr = list(map(int, input().split()))
cumSumArr = prefixSum(arr)   # O(N)
queries_num = int(input())
for q in range(queries_num):
    i, j = map(int, input().split())
    result = sumInRange(cumSumArr, arr, i, j)   # O(1) for each query, so total O(N+Q)
    print (result)

