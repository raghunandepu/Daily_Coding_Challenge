# https://www.hackerrank.com/contests/smart-interviews/challenges/si-binary-representation

"""
Given a positive integer, print its binary representation. 

Input Format

First line of input contains T - number of test cases. Its followed by T lines, each line containing a single integer. 

Constraints

1 <= T <= 10000 
0 <= N <= 109 

Output Format

For each test case, print binary representation, separated by new line. 

Sample Input 0

5
10
15
7
1
120
Sample Output 0

1010
1111
111
1
1111000"""

from math import log
t = int(input())
for c in range(t):
    n = int(input())
    
    if n == 0:
      print(0)
    else:
      result = []
      for i in range(0, int(log(n,2))+1):
        result += str(n & 1)
        n >>= 1
      print (''.join(reversed(result)))