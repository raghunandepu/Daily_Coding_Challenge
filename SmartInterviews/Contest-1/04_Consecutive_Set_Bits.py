# https://www.hackerrank.com/contests/smart-interviews-14a/challenges/si-consecutive-set-bits

"""
Given a number N, find the max number of consecutive set bits in the number.

Input Format

First line of input contains T - number of test cases. Its followed by T lines, each containing a single number N.

Constraints

1 <= T <= 10000 
0 <= N <= 1018 

Output Format

For each test case, print the max number of consecutive set bits, separated by newline. 

Sample Input 0

3
5
15
13
Sample Output 0

1
4
2
Explanation 0

Test Case 1 
Binary Representation of 5: 101 
Maximum Consecutive Set Bits: 1 

Test Case 2 
Binary Representation of 15: 1111 
Maximum Consecutive Set Bits: 4 

Test Case 3 
Binary Representation of 13: 1101 
Maximum Consecutive Set Bits: 2 """

def solve(n):
    count = 0
    while (n != 0):
        n = (n & (n << 1))
        count += 1
    return count

t = int(input())
for tc in range(t):
    n = int(input())
    result = solve(n)
    print (result)