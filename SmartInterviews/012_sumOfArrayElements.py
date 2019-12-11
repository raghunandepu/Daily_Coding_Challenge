# https://www.hackerrank.com/contests/smart-interviews/challenges/si-sum-of-array-elements
t = int(input())
for tc in range(t):
    n = int(input())
    arr = [int(x) for x in input().split()]
    result = 0
    for i in arr:
      result += i
    print (result)