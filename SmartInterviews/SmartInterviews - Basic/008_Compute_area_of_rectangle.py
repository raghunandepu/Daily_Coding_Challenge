# https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-compute-area-of-rectangle/submissions/code/1319355022

"""
Given the length and breadth of the rectangle. Print area of the rectangle.

Input Format

Input contains two positive integers L - length of the rectangle and B - breadth of the rectangle.

Constraints

1 <= L, B <=109

Output Format

Print area of the rectangle.

Sample Input 0

5 8
Sample Output 0

40
Explanation 0

Self Explanatory"""

l, b = map(int, input().split())

def solve(l,b):
    return l*b

print (solve(l,b))