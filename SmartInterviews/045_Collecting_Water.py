# https://www.hackerrank.com/contests/smart-interviews/challenges/si-collecting-water/problem
""""
You are given the heights of N buildings. All the buildings are of width 1 and are adjacent to each other with no empty space in between. Assume that its raining heavily, and as such water will be accumulated on top of certain buildings. Your task is to find the total amount of water accumulated.

Input Format

First line of input contains T - number of test cases. Its followed by 2T lines, the first line contains N - the number of buildings. The second line contains N elements denoting the height of the buildings. 

Constraints

30 points
1 <= T <= 1000 
1 <= N <= 1000 
1 <= a[i] <= 1000 

70 points
1 <= T <= 1000 
1 <= N <= 100000 
1 <= a[i] <= 1000 

Output Format

For each test case, print the units of water accumulated, separated by newline.

Sample Input 0

2
7
1 6 2 4 5 7 9 
5
3 2 7 4 7 
Sample Output 0

7
4
Explanation 0

Test Case 1
Water accumulated on top of Building-1 : 0
Water accumulated on top of Building-2 : 0
Water accumulated on top of Building-3 : 4
Water accumulated on top of Building-4 : 2
Water accumulated on top of Building-5 : 1
Water accumulated on top of Building-6 : 0
Water accumulated on top of Building-7 : 0
Total = 0 + 0 + 4 + 2 + 1 + 0 + 0 = 7 


Test Case 2
Water accumulated on top of Building-1 : 0
Water accumulated on top of Building-2 : 1
Water accumulated on top of Building-3 : 0
Water accumulated on top of Building-4 : 3
Water accumulated on top of Building-5 : 0
Total = 0 + 1 + 0 + 3 + 0 = 4 
"""
# complexity: O(n), O(n)
def maxWater(arr, n):
    res = 0
    # left[i] contains height of tallest bar to the 
    # left of i'th bar including itself. Similary calculate right[i]
    left = [0] * n
    right = [0] *n 
    
    left[0] = arr[0]
    for i in range(1,n):
        left[i] = max(left[i-1], arr[i])
    
    right[n-1] = arr[n-1]
    for j in range(n-2, -1, -1):
        right[j] = max(right[j+1], arr[j])
        
    # Calculate the accumulated water element by element 
    # consider the amount of water on i'th bar, the 
    # amount of water accumulated on this particular 
    # bar will be equal to min(left[i], right[i]) - arr[i]
    
    for k in range(n):
        res += min(left[k], right[k]) - arr[k]
        
    return res

t = int(input())
for tc in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print (maxWater(arr, n))
    