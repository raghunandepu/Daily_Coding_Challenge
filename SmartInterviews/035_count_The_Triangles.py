# https://www.hackerrank.com/contests/smart-interviews/challenges/si-count-the-triangles/problem
"""
You have a collection of N rods. Each rod has a unique mark on it. You are given the lengths of each rod. You have to tell how many different triangles can be formed using these rods.

Input Format

First line of input contains T - number of test cases. Its followed by 2T lines, the first line contains N - the number of rods. The second line contains the lengths of the rods. 

Constraints

40 points 
1 <= T <= 100 
1 <= N <= 100 
1 <= A[i] <= 100000 

60 points 
1 <= T <= 100 
1 <= N <= 1000 
1 <= A[i] <= 100000 

Output Format

For each test case, print the total number of different triangles possible, separated by new line. 

Sample Input 0

2
6
20 67 72 83 23 59 
6
4 2 10 12 8 10 
Sample Output 0

14
10"""

def countTriangles(arr):
    count = 0
    arr.sort()
    for i in range(0,n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if (arr[i] + arr[j]) > arr[k]:
                    count += 1
                else:
                    break
    return count
            
            

t = int(input())
for tc in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    result = countTriangles(arr)
    print (result)