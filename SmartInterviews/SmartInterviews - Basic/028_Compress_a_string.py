# https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-compress-a-string/copy-from/1319389840

"""
Given a String, compress the given string. See example for more details.

Input Format

Input contains string of lowercase and uppercase characters - S.

Constraints

1 <= len(S) <= 100

Output Format

Print the compressed string.

Sample Input 0

aaaBBBBhhhekkL
Sample Output 0

a3B4h3e1k2L1
Explanation 0

In the given string, a is repeating for 3 times - after compression a3.
Similarly, B is repeating for 4 times - B4
h is repeating for 3 times - h3
e is repeating for 1 times - e1
k is repeating for 2 times - k2
L is repeating for 1 times - L1"""

s = input()
def encode(s):
    """
    This solution compresses without checking. Known as the RunLength Compression algorithm.
    """
    
    # Begin Run as empty string
    result = ""
    n = len(s)
    
    # Check for length 0
    if n == 0:
        return ""
    
    # Check for length 1
    if n == 1:
        return s + "1"
    
    #Intialize Values
    count = 1
    i = 1
    
    for i in range(1,n):
        if s[i] == s[i-1]:
            count += 1
        else:
            result += s[i-1] + str(count)
            count = 1
        
    result += s[i] + str(count) # for the last character 
    
    return result          

print (encode(s))


