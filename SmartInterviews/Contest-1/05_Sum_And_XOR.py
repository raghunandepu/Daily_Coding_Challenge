# https://www.hackerrank.com/contests/smart-interviews-14a/challenges/si-sum-and-xor

"""Given a integer N, find the number of positive integers X such that X<=N and N+X = N^X (N xor X). 

Input Format

First line of input contains T - number of test cases. Its followed by T lines, each line contains a single integer N. 

Constraints

20 points 
1 <= T <= 103 
0 <= N <= 103 

80 points 
1 <= T <= 104 
0 <= N <= 1018 

Output Format

For each test case, print the count of X's, separated by new line.

Sample Input 0

2
5
10
Sample Output 0

1
3
Explanation 0

Test Case 1 
Possible values: 5+2 = 5^2.

Test Case 2 
Possible values: 10+1 = 10^1, 10+4=10^4, 10+5=10^5"""

def zeroBitCounter(n):
    count = 0
    while (n):
        if ((n & 1) == 0):
            count += 1
        n >>= 1
    return count

def solve(n):
    count = zeroBitCounter(n)
    return (1 << count) - 1

t = int(input())
for tc in range(t):
    n = int(input())
    result = solve(n)
    print (result)