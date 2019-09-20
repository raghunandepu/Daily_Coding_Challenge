# Problem
# Reference: https://leetcode.com/problems/valid-phone-numbers/
"""Given a text file file.txt that contains list of phone numbers (one per line), write a one liner bash script to print all valid phone numbers.

You may assume that a valid phone number must appear in one of the following two formats: (xxx) xxx-xxxx or xxx-xxx-xxxx. (x means a digit)

You may also assume each line in the text file must not contain leading or trailing white spaces.

Example:

Assume that file.txt has the following content:

987-123-4567
123 456 7890
(123) 456-7890
Your script should output the following valid phone numbers:

987-123-4567
(123) 456-7890"""


----------
# Solution
# Read from the file file.txt and output all valid phone numbers to stdout.
grep -e '\(^[0-9]\{3\}-[0-9]\{3\}-[0-9]\{4\}$\)' -e '\(^([0-9]\{3\})[ ][0-9]\{3\}-[0-9]\{4\}$\)' file.txt


# Explanation:
"""
1. In Bash, we use \ to escape next one trailing character;
2. ^ is used to denote the beginning of a line
3. $ is used to denote the end of a line
4. {M} is used to denote to match exactly M times of the previous occurence/regex
5. (...) is used to group pattern/regex together

Back to this problem: it requires us to match two patterns, for better readability, I used -e and separate the two patterns into two regexes, the first one matches this case: xxx-xxx-xxxx and the second one matches this case: (xxx) xxx-xxxx"""