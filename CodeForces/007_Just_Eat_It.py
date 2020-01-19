# https://codeforces.com/contest/1285/problem/B

"""
B. Just Eat It!
time limit per test1 second
memory limit per test256 megabytes
inputstandard input
outputstandard output
Today, Yasser and Adel are at the shop buying cupcakes. There are 𝑛
n
 cupcake types, arranged from 1
1
 to 𝑛
n
 on the shelf, and there are infinitely many of each type. The tastiness of a cupcake of type 𝑖
i
 is an integer 𝑎𝑖
a
i
. There are both tasty and nasty cupcakes, so the tastiness can be positive, zero or negative.

Yasser, of course, wants to try them all, so he will buy exactly one cupcake of each type.

On the other hand, Adel will choose some segment [𝑙,𝑟]
[
l
,
r
]
 (1≤𝑙≤𝑟≤𝑛)
(
1
≤
l
≤
r
≤
n
)
 that does not include all of cupcakes (he can't choose [𝑙,𝑟]=[1,𝑛]
[
l
,
r
]
=
[
1
,
n
]
) and buy exactly one cupcake of each of types 𝑙,𝑙+1,…,𝑟
l
,
l
+
1
,
…
,
r
.

After that they will compare the total tastiness of the cupcakes each of them have bought. Yasser will be happy if the total tastiness of cupcakes he buys is strictly greater than the total tastiness of cupcakes Adel buys regardless of Adel's choice.

For example, let the tastinesses of the cupcakes be [7,4,−1]
[
7
,
4
,
−
1
]
. Yasser will buy all of them, the total tastiness will be 7+4−1=10
7
+
4
−
1
=
10
. Adel can choose segments [7],[4],[−1],[7,4]
[
7
]
,
[
4
]
,
[
−
1
]
,
[
7
,
4
]
 or [4,−1]
[
4
,
−
1
]
, their total tastinesses are 7,4,−1,11
7
,
4
,
−
1
,
11
 and 3
3
, respectively. Adel can choose segment with tastiness 11
11
, and as 10
10
 is not strictly greater than 11
11
, Yasser won't be happy :(

Find out if Yasser will be happy after visiting the shop.

Input
Each test contains multiple test cases. The first line contains the number of test cases 𝑡
t
 (1≤𝑡≤104
1
≤
t
≤
10
4
). The description of the test cases follows.

The first line of each test case contains 𝑛
n
 (2≤𝑛≤105
2
≤
n
≤
10
5
).

The second line of each test case contains 𝑛
n
 integers 𝑎1,𝑎2,…,𝑎𝑛
a
1
,
a
2
,
…
,
a
n
 (−109≤𝑎𝑖≤109
−
10
9
≤
a
i
≤
10
9
), where 𝑎𝑖
a
i
 represents the tastiness of the 𝑖
i
-th type of cupcake.

It is guaranteed that the sum of 𝑛
n
 over all test cases doesn't exceed 105
10
5
.

Output
For each test case, print "YES", if the total tastiness of cupcakes Yasser buys will always be strictly greater than the total tastiness of cupcakes Adel buys regardless of Adel's choice. Otherwise, print "NO". 
"""

# Not accepted for pretest 2

class JustEatIt :
  def solve(self, arr, n):
    for i in range(n):
      if arr[i] < 0 :
        return "NO"
    return "YES"
          
    
if __name__ == '__main__':
  t = int(input())
  for tc in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    tastiness = JustEatIt()
    result = tastiness.solve(arr, n)
    print (result)

