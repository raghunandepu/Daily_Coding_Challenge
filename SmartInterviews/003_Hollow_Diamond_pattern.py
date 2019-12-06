n = int(input())
for i in range(n):
        print(' '*(n-i-1)+'*', end='')
        if i>=1:
                print(' '*(2*i-1)+'*', end='')
        print()
for i in range(n-1):
        print(' '*(i+1)+'*', end='')
        if i!=n-2:
                print(' '*(2*n-2*i-5)+'*', end='')
                print()