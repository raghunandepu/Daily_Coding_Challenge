# https://www.hackerrank.com/contests/smart-interviews/challenges/si-print-hollow-diamond-pattern/submissions/code/1318367747
"""Print hollow diamond pattern using '*'. See examples for more details.

Input Format

First line of input contains T - number of test cases. Its followed by T lines, each line contains a single odd integer N - the size of the diamond. 

Constraints

1 <= T <= 100 
3 <= N <= 201 

Output Format

For each test case, print the test case number as shown, followed by the diamond pattern, separated by newline. 

Sample Input 0

4
3
7
5
15"""

t = int(input())
for tc in range(t):
    n = int(input())
    print (f'Case #{tc+1}:')
    for i in range(0, n//2 +1):
        if (i==0 or i == n-1):
            print(' '*(n//2)+'*')
        else:
            print(' '*(n//2 -i)+'*'+' '*(2*i -1)+'*')
    for i in range(n//2 -1,0,-1):
        print(' '*(n//2 -i)+'*'+' '*(2*i -1)+'*')
    print(' '*(n//2)+'*')

                
