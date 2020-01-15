# https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-prime-or-not/problem

"""
Given a positive integer - N. Check whether the number is prime or not.

Input Format

Input contains positive integer - N.

Constraints

1 <= N <= 109

Output Format

Print "Yes" if the number is prime, "No" otherwise.

Sample Input 0

11
Sample Output 0

Yes"""


N = int(input())

def checkPrime(n):
    if N == 1:
        return "No"
    for i in range(2,int(pow(N, 0.5))+1):
        if N % i == 0:
            return "No"
    return "Yes"
    
print (checkPrime(N))