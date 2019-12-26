# https://www.hackerrank.com/contests/smart-interviews/challenges/si-triplet-with-sum-k/problem

"""
You are given an integer array and a number K. You have to tell if there exists i,j,k in the given array such that ar[i]+ar[j]+ar[k]=K, i≠j≠k. 

Input Format

First line of input contains T - number of test cases. Its followed by 2T lines, the first line contains N and K - the size of the array and the number K. The second line contains the elements of the array. 

Constraints

30 points
1 <= T <= 100 
3 <= N <= 100 

70 points
1 <= T <= 100 
3 <= N <= 1000 

General
-100000 <= A[i] <= 100000 
0 <= K <= 100000 

Output Format

For each test case, print "true" if the arrays contains such elements, false otherwise, separated by new line. 

Sample Input 0

3
5 60
1 20 40 100 80 
12 54
12 45 52 65 21 645 234 -100 14 575 -80 112 
3 15
5 5 5
Sample Output 0

false
true
true
Explanation 0
"""
# O(n^2) time | O(n) space

def threeNumberSum(arr, K):
    arr.sort()
    for i in range(n):
        left = i + 1
        right = n - 1
        while left < right:
            currentSum = arr[i] + arr[left] + arr[right]
            if currentSum == K:
                return "true"
            elif currentSum > K:
                right -= 1
            else:
                left += 1
    return "false"

t = int(input())
for tc in range(t):
    n, K = map(int, input().split())
    arr = list(map(int, input().split()))
    result = threeNumberSum(arr, K)
    print (result)