t = int(input())
for tc in range(t):
  n = int(input())
  arr = list(map(int, input().split()))
  counts = dict()
  for i in arr:
    try:
      counts[i] += 1
    except:
      counts[i] = 1
  for k in counts.keys():
    if counts[k] == 1:
      print(k)
      break