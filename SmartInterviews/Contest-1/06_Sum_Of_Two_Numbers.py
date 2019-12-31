# https://www.hackerrank.com/contests/smart-interviews-14a/challenges/si-sum-of-2-numbers

"""
Given an array, check if there exists 2 elements of the array such that their sum is equal to the sum of the remaining elements of the array.

Input Format

First line of input contains T - number of test cases. Its followed by 2T lines, the first line contains N - the size of the array. The second line contains a N integers - elements of the array. 

Constraints

30 points 
1 <= T <= 100 
1 <= N <= 1000 
-106 <= A[i] <= 106 

70 points 
1 <= T <= 500 
1 <= N <= 10000 
-106 <= A[i] <= 106 

Output Format

For each test case, print "Yes" if such elements exists, "No" otherwise, separated by new line.

Sample Input 0

2
5
-3 5 8 2 -4 
6
5 -10 8 4 2 -3 
Sample Output 0

Yes
No
Explanation 0

Test Case 1 
Possible values: 8+(-4) = (-3)+5+2.

Test Case 2 
No 2 elements exists whose sum is equal to the sum of the remaining array elements."""

def solve(arr, n):
    s = set()
    sum = 0
    for i in range(n):
        sum += arr[i]
    if sum % 2 != 0:
        return "No"
    sum = sum // 2
    
    for i in range(n):
        target = sum - arr[i]
        if arr[i] not in s:
            s.add(arr[i])
        if target in s:
            return "Yes"
    return "No"

t = int(input())
for tc in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    result = solve(arr, n)
    print (result)