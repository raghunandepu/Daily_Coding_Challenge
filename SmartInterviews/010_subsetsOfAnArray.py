from itertools import combinations

# https://www.hackerrank.com/contests/smart-interviews/challenges/si-subsets-of-an-array
"""Given an array of unique integer elements, print all the subsets of the given array in lexicographical order. 

Input Format

First line of input contains T - number of test cases. Its followed by 2T lines, the first line contains N - the size of the array and second line contains the elements of the array. 

Constraints

1 <= T <= 100
1 <= N <= 10
0 <= A[i] <= 100

Output Format

For each test case, print the subsets of the given array in lexicographical order, separated by new line. Print an extra newline between output of different test cases.

Sample Input 0

3
3
5 15 3 
2
57 96 
4
3 15 8 23 
Sample Output 0

3 
3 5 
3 5 15 
3 15 
5 
5 15 
15 

57 
57 96 
96 

3 
3 8 
3 8 15 
3 8 15 23 
3 8 23 
3 15 
3 15 23 
3 23 
8 
8 15 
8 15 23 
8 23 
15 
15 23 
23 """

t = int(input())
for tc in range(t):
  n = int(input())
  arr = [int(x) for x in input().split()]
  result = []
  for i in range(1, n+1):
    for comb in combinations(arr,i):
      result.append(sorted(comb)) # sorting each combination
  for comb in sorted(result): # sorting the overall result of all combinations.
    print(' '.join(list(map(str,comb))))
  print(' ')