# https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-number-reverse/problem

"""Given a number - N, reverse the number.

Input Format

Input contains a integer - N.

Constraints

-1018<= N <= 1018

Output Format

Print the reversed number.

Sample Input 0

1344
Sample Output 0

4431

"""

# This code handles negative numbers as well


n = int(input())

def reverseNumber(n):
    reverse = 0
    
    if n == 0:
        return 0
    
    elif n > 0:
        while (n > 0):
            reminder = int (n % 10)
            reverse = (reverse * 10) + reminder
            n = n // 10
        return reverse
    
    elif n < 0:
        n = -1 * n
        while (n > 0):
            reminder = int (n % 10)
            reverse = (reverse * 10) + reminder
            n = n // 10
        return (-1) * reverse

