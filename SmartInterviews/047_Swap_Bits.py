# https://www.hackerrank.com/contests/smart-interviews/challenges/si-swap-bits/problem

"""
Given a number, swap the adjacent bits in the binary representation of the number, and print the new number formed after swapping. 

Input Format

First line of input contains T - number of test cases. Each of the next T lines contains a number N. 

Constraints

1 <= T <= 100000 
0 <= N <= 109 

Output Format

For each test case, print the new integer formed after swapping adjacent bits, separated by new line. 

Sample Input

4
10
7
43
100

Sample Output

5
11
23
152

Explanation

Test Case 1

Binary Representation of 10: 000...1010
After swapping adjacent bits: 000...0101 (5)

Test Case 2

Binary Representation of 7: 000...0111
After swapping adjacent bits: 000...1011 (11)"""

# Reference : https://www.geeksforgeeks.org/swap-all-odd-and-even-bits/

# If we take a closer look at the example, we can observe that we basically need to right shift (>>) all even bits (In the above example, even bits of 23 are highlighted) by 1 so that they become odd bits (highlighted in 43), and left shift (<<) all odd bits by 1 so that they become even bits. 

def swapBits(n):
    # Get all even bits of n
    even_bits = n & 0xAAAAAAAA
    
    # Get all odd bits of n
    odd_bits = n & 0x55555555
    
    # Right shift of even bits
    even_bits >>= 1
    
    # Left shift of odd bits
    odd_bits <<= 1
    
    # Combine even and odd bits
    return (even_bits | odd_bits)

t = int(input())
for tc in range(t):
    n = int(input())
    print (swapBits(n))