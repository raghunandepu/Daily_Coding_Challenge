from itertools import combinations

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