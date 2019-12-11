"""t = int(input())
for tc in range(t):
    arr = [int(x) for x in input().split()]
    a = arr[0]
    b = arr[1]
    max = a if a > b else b
    while True:
        if ((max % a == 0) and (max % b ==0)):
            lcm = max
            break
        max += 1
    hcf = int(((a * b) / int(lcm)))
    print (f'{lcm} {hcf}')
        """
def hcf(a,b):
  if b==0:
    return a
  else:
    return hcf(b, a%b) 

def lcm(a,b):
  return a*b // hcf(a,b)  
        
t = int(input())
for tc in range(t):
    arr = [int(x) for x in input().split()]
    a = arr[0]
    b = arr[1]
    hcf_result = hcf(a,b)
    lcm_result = lcm(a,b)
    print(f'{lcm_result} {hcf_result}')

   
      