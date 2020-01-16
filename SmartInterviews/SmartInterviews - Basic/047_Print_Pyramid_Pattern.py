# https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-print-pyramid-pattern/problem

"""

Print pyramid pattern. See example for more details.

Input Format

First line of input contains a single integer N - the size of the pyramid.

Constraints

1 <= N <= 50

Output Format

For the given integer, print pyramid pattern.

Sample Input 0

5
Sample Output 0

    *
   ***
  *****
 *******
*********
"""



#http://asimpleprogramme.blogspot.com/2018/01/how-to-write-c-program-to-print-pyramid.html
n = int(input())

def pattern(n):
    
    for i in range(1,n+1):
        for j in range(-n+1,i):
            if abs(j) -i < 0:
                print("*", end ='')
            else:
                print(' ', end='')
        print()
            
        
pattern(n)