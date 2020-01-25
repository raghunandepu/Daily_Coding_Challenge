# https://codeforces.com/contest/1294/problem/A
"""
A. Collecting Coins
time limit per test2 seconds
memory limit per test256 megabytes
inputstandard input
outputstandard output
Polycarp has three sisters: Alice, Barbara, and Cerene. They're collecting coins. Currently, Alice has 𝑎
a
 coins, Barbara has 𝑏
b
 coins and Cerene has 𝑐
c
 coins. Recently Polycarp has returned from the trip around the world and brought 𝑛
n
 coins.

He wants to distribute all these 𝑛
n
 coins between his sisters in such a way that the number of coins Alice has is equal to the number of coins Barbara has and is equal to the number of coins Cerene has. In other words, if Polycarp gives 𝐴
A
 coins to Alice, 𝐵
B
 coins to Barbara and 𝐶
C
 coins to Cerene (𝐴+𝐵+𝐶=𝑛
A
+
B
+
C
=
n
), then 𝑎+𝐴=𝑏+𝐵=𝑐+𝐶
a
+
A
=
b
+
B
=
c
+
C
.

Your task is to find out if it is possible to distribute all 𝑛
n
 coins between sisters in a way described above.

You have to answer 𝑡
t
 independent test cases.

Input
The first line of the input contains one integer 𝑡
t
 (1≤𝑡≤104
1
≤
t
≤
10
4
) — the number of test cases.

The next 𝑡
t
 lines describe test cases. Each test case is given on a new line and consists of four space-separated integers 𝑎,𝑏,𝑐
a
,
b
,
c
 and 𝑛
n
 (1≤𝑎,𝑏,𝑐,𝑛≤108
1
≤
a
,
b
,
c
,
n
≤
10
8
) — the number of coins Alice has, the number of coins Barbara has, the number of coins Cerene has and the number of coins Polycarp has.

Output
For each test case, print "YES" if Polycarp can distribute all 𝑛
n
 coins between his sisters and "NO" otherwise."""
 
 # Working solution
 
class Collecting_Coins:
  def solve(self, a, b, c, n):
    resMax = max(max(a,b), c)
    if resMax == a:
      requiredCoins = 2*a - (b+c) # (Max -b) + (Max - c) coins required to share
    elif resMax == b:
      requiredCoins = 2*b - (a+c) # (Max -a) + (Max - c)
    else:
      requiredCoins = 2*c - (b+a) # (Max -b) + (Max - a)
      
    if n < requiredCoins:
      return "NO"
    else:
        result = (a + b + c + n) % 3
        if result == 0:
          return "YES"
    return "NO"    
  
if __name__ == '__main__':
  n = int(input())
  for i in range(n):
    a, b, c, n = map(int, input().split())
    collectCoins = Collecting_Coins()
    result = collectCoins.solve(a, b, c, n)
    print (result)