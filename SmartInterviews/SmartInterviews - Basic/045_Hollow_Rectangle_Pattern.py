# https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-hollow-rectangle-pattern/problem

"""
Print hollow rectangle pattern using '*'. See example for more details.

Input Format

Input contains two integers W and L. W - width of the rectangle, L - length of the rectangle.

Constraints

2 <= W <= 50 2 <= L <= 50

Output Format

For the given integers W and L, print the hollow rectangle pattern.

Sample Input 0

5 4
Sample Output 0

*****
*   *
*   *
*****
"""

n,m = map(int, input().split())
def print_rectangle(n, m) : 
      
    for i in range(1, m+1) : 
        for j in range(1, n+1) : 
            if (i == 1 or i == m or
                j == 1 or j == n) : 
                print("*", end="")             
            else : 
                print(" ", end="")             
          
        print()
        
print_rectangle(n, m)