# https://www.hackerrank.com/contests/smart-interviews-14a/challenges/si-even-split
"""Given a number N, check if you can split the number into 2 non-zero even parts.

Input Format

First line of input contains T - number of test cases. Its followed by T lines, each line contains a single integer N. 

Constraints

1 <= T <= 105 
0 <= N <= 1018 

Output Format

For each test case, print "Yes" if you can split the number into 2 non-zero even parts, "No" otherwise, separated by new line.

Sample Input 0

2
8
1
Sample Output 0

Yes
No
Explanation 0

Test Case 1 
You can split 8 as 4,4 or 6,2.

Test Case 2 
You cannot split 1 into 2 even parts."""

def solve(n):
    if n > 2 and n % 2 == 0:
        return "Yes"
    return "No"

t = int(input())
for tc in range(t):
    n = int(input())
    result = solve(n)
    print (result)