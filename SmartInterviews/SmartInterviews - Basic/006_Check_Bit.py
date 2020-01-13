# https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-check-bit/problem
"""In a given integer - N, check whether the ith bit is set or not.

Input Format

Input contains integers - N and i.

Constraints

-1018 <= N <= 1018 
0 <= i <= 63

Output Format

Print "true" if ith bit is set in the given integer N, "false" otherwise.

Sample Input 0

10 1
Sample Output 0

true
Explanation 0

Self Explanatory.
"""

N, i = map(int, input().split())

def checkBit(N, i):
    if (N & (1 << i)) !=0:
        return "true"
    return "false"

print (checkBit(N, i))