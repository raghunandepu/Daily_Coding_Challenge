# https://www.hackerrank.com/contests/smart-interviews/challenges/si-compute-factorial/problem

"""Given a number N, print N!.

Input Format

First line of input contains T - number of test cases. Its followed by T lines, each containing a single number N. 

Constraints

1 <= T <= 1000000 
0 <= N <= 1000000 

Output Format

For each test case, print N!. Since the result can be very large, print N! % 1e9+7. 

Sample Input 0

3
5
20
50
Sample Output 0

120
146326063
318608048"""

# O(n) time| O(n) space
# Approach: Take the max element in test case and compute fatorials till that number
# Then in O(1) time, we can pull factorial for other test cases
# We need to do this way because of contrains N and T (N*T = 10^12 which is greater than 10^9)

M = 1e9+7
def factorial(n):
    if n == 0:
        return 1
    fact = [0 for i in range(n+1)]
    fact[0] = 1
    fact[1] = 1
    for i in range(2, n+1):
        fact[i] = int((i % M * fact[i-1] % M) % M)
    return fact

t = int(input())
arr = [0 for i in range(t)]
for i in range(t):
    arr[i] = int(input())
n = max(arr)

result = factorial(n)
#print (result)
for ele in arr:
    print(result[ele])