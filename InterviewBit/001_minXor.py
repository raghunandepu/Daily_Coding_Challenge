
def findMinXor(A):
    s = sorted(A)
    min_xor = s[0] ^ s[1]
    for i in range(0, len(A)-1):
        val = s[i] ^ s[i+1]
        min_xor = min(min_xor,val)
    return min_xor
  
A = [12, 4, 6, 2]
print(findMinXor(A))