# https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-toggle-case-of-characters/problem

"""
Given a string, toggle case of each character in the given string.

Input Format

Input contains a string - S.

Constraints

1 <= len(S) <= 100

Output Format

Print the toggled string.

Sample Input 0

abdBd
Sample Output 0

ABDbD
Explanation 0

Self Explanatory"""

# The ASCII table is constructed in such way that the binary representation of lowercase letters is almost identical of binary representation of uppercase letters.

#Toggling Case
# The integer with 6th LSB as 1 is 32 (0010 0000). Therefore, bitwise XORing of a character with 32 will toggle the 6th LSB of character and hence, will toggle its case. If character is upper case, it will be converted to lower case and vice versa.

# string = input()
def toggleCase(string):
    for i in range(len(string)):
        print (chr(ord(string[i]) ^ 32), end ='')
toggleCase(string)

