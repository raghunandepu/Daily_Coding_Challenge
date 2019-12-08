t = int(input())
for p in range(t):
  print (f'Case #{p+1}')
  n = int(input())
  
  for i in range(n):
    print (' '*(n-1-i)+'*'*(i+1))