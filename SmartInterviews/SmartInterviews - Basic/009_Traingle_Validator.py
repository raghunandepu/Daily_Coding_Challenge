# https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-triangle-validator

"""
Given sides of a triangle, check whether the triangle is valid.

Input Format

Input contains three integers A, B, C - Sides of the triangle.

Constraints

1 <= A, B, C <= 109

Output Format

Print "Yes" if you can construct a triangle with the given three sides, "No" otherwise.

Sample Input 0

4 3 5
Sample Output 0

Yes
Explanation 0

Self Explanatory"""

a, b, c = map(int, input().split())
def solve(a, b, c):
    if (a+b <= c) or (a+c <= b) or (b+c <= a):
        return "No"
    return "Yes"

print (solve(a, b, c))