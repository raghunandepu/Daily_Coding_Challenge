# https://www.hackerrank.com/contests/smart-interviews/challenges/si-compute-a-power-b/copy-from/1318369538
"""Given 2 numbers - a and b, evaluate ab. 

Input Format

First line of input contains T - number of test cases. Its followed by T lines, each line containing 2 numbers - a and b, separated by space. 

Constraints

30 points 
1 <= T <= 1000 
0 <= a <= 106 
0 <= b <= 103 

70 points 
1 <= T <= 1000 
0 <= a <= 106 
0 <= b <= 109 

Output Format

For each test case, print ab, separated by new line. Since the result can be very large, print result % 1000000007 

Sample Input 0

4
5 2
1 10
2 30
10 10
Sample Output 0

25
1
73741817
999999937"""

from math import log
M = int(1e9+7)
t = int(input())
for tc in range(t):
    a,b=map(int,input().split())
    if b==0:
        print(1)
        continue
    ans = 1
    x = a
    for i in range(0,int(log(b,2))+1):
        if b&1:
            ans=(ans*x)%M
        x=(x*x)%M
        b>>=1
    print(ans)
    
