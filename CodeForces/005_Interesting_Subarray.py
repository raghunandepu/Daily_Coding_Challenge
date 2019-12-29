#http://m3.codeforces.com/contest/1270/problem/B

class InteresingSubarray:
  def solve(self, arr, n):
    m = min(arr)
    M = max(arr)
    diff = M - m
    result = []
    if diff >= n:
      print ("YES")
      result.append(arr.index(m))
      result.append(arr.index(M)+1)
      return result
    else:
      return "NO"
    
if __name__ == '__main__':
  t = int(input())
  for tc in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    intsubarr = InteresingSubarray()
    result = intsubarr.solve(arr, n)
    if result == "NO":
      print (result)
    else:
      print (*result)
  
  
  