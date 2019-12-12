# https://www.hackerrank.com/contests/smart-interviews/challenges/si-time-of-the-year

"""Given the number of seconds elapsed since epoch [01-01-1970 00:00:00 Thursday], you need to find the current date, along with the day.

Input Format

First line of input contains T - number of test cases. Its followed by T lines, each line contains the number of seconds elapsed since epoch. 

Constraints

1 <= T <= 10000 
0 <= S <= 109

Output Format

For each test case, print the date in DD-MMM-YYYY format, followed by the day, separated by newline. 

Sample Input 0

10
86399
86400
2592000
2678400
8639999
8640000
31535999
31536000
68169599
68169600
Sample Output 0

01-JAN-1970 Thursday
02-JAN-1970 Friday
31-JAN-1970 Saturday
01-FEB-1970 Sunday
10-APR-1970 Friday
11-APR-1970 Saturday
31-DEC-1970 Thursday
01-JAN-1971 Friday
28-FEB-1972 Monday
29-FEB-1972 Tuesday"""
  
import time

t = int(input())
for tc in range(t):
    print(time.strftime("%d-%^b-%Y %A", time.gmtime(int(input()))))