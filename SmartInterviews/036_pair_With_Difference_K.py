# https://www.hackerrank.com/contests/smart-interviews/challenges/si-pair-with-difference-k/submissions/code/1318788499

"""
You are given an integer array and a positive integer K. You have to tell if there exists a pair of integers in the given array such that ar[i]-ar[j]=K and i≠j. 

Input Format

First line of input contains T - number of test cases. Its followed by 2T lines, the first line contains N and K - the size of the array and the number K. The second line contains the elements of the array. 

Constraints

1 <= T <= 50 
2 <= N <= 100000 
1 <= K <= 100000 
-100000 <= A[i] <= 100000 

Output Format

For each test case, print "true" if the arrays contains such elements, false otherwise, separated by new line. 

Sample Input 0

2
5 60
1 20 40 100 80 
10 11
12 45 52 65 21 645 234 14 575 112 
Sample Output 0

true
false"""

# Time: (logn)
# Sorting + Two pointer technique

def pairWithDifference(n, arr, target):
    arr.sort()
    i, j = 0, 1
    while i < n and j < n:
        if i != j and arr[j] - arr[i] == target:
            return "true"
        elif arr[j] - arr[i] < target:
            j+= 1
        else:
            i+= 1
    return "false"

t = int(input())
for tc in range(t):
    n, target = map(int, input().split())
    arr = list(map(int, input().split()))
    result = pairWithDifference(n, arr, target)
    print (result)