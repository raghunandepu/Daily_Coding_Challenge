"""Palindrome Check
​
Write a function that takes in a non-empty string and that returns a boolean representing whether or not the string is a palindrome. A palindrome is defined as a string that is written the same forward and backward.
​
Sample input: "abcdcba"
Sample output: True (it is a palindrome)"""

# O(n) time | O(1) space
def isPalindrome(string):
  start_index = 0
  end_index = len(string) - 1
  while start_index < end_index:
    if string[start_index] != string[end_index]:
      return False
    start_index += 1
    end_index -= 1
  return True
		
print(isPalindrome("abccba"))