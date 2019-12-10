t = int(input())
for i in range(t):
    
    a, b = map(int, input().split())
    result = a
    if b == 0:
          print (result)
    else:   
      for i in range(b-1):
        result *= a
      print (result)