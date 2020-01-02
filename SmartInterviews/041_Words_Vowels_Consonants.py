# https://www.hackerrank.com/contests/smart-interviews/challenges/si-words-vowels-and-consonants/

"""
Given a sentence containing only uppercase/lowercase english alphabets and spaces, you have to count the number of words, vowels and consonants.

Input Format

First line of input contains T - number of test cases. Its followed by T lines, each line contains a single sentence.

Constraints

1 <= T <= 1000 
1 <= len(sentence) <= 104 

Output Format

For each test case, print the number of words, vowels and consonants, separated by newline. 

Sample Input 0

4
Hi
Hello World
  Exception  
Hi there
Sample Output 0

1 1 1
2 3 7
1 4 5
2 3 4
Explanation 0

Self Explanatory"""

def solve(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    words = s.split()
    wordCount = len(words)
    vowelCount = 0
    consonantCount = 0
    for c in s:
        if c != ' ':
            if c in vowels:
                vowelCount += 1
            else:
                consonantCount += 1
                
    return str(wordCount)+ " " +str(vowelCount)+ " " +str(consonantCount)

t = int(input())
for tc in range(t):
    s = input()
    result = solve(s)
    print (result)