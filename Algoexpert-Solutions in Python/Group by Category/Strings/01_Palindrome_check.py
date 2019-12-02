"""Palindrome Check (Easy)
​
Write a function that takes in a non-empty string and that returns a boolean representing whether or not the string is a palindrome. A palindrome is defined as a string that is written the same forward and backward.
​
Sample input: "abcdcba"
Sample output: True (it is a palindrome)"""

# Solution 4: Best solution 
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

#Other Solutions:

# Solution 1: We create an empty string and add each character from last, then compare with original.

# O(n**2) time due to traversal from last for n chars and adding them again to reversed string | O(n) space
"""def isPalindrome(string):
  reversedString = ""
  
  #Traversing through reversed index from last
  for i in reversed(range(len(string))):
    reversedString += string[i]
  return reversedString == string
print(isPalindrome("abccba"))"""

# Solution 2:
# We use array rather than creating a new string
# O(n) time | O(n) space
"""def isPalindrome(string):
  reversedChars = []
  for i in reversed(range(len(string))):
    reversedChars.append(string[i])
  return string == "".join(reversedChars)

print(isPalindrome("abccba"))"""

# Solution 3:
# Using recursive way - Compare first and last character and also do recursive check on the middle string
# O(n) time | O(n) space due to call stack (recursive)
"""def isPalindrome(string, i= 0):
  j = len(string) - 1 - i
  return True if i >=j else string[i] == string[j] and isPalindrome(string, i + 1)

print(isPalindrome("abccbaw"))"""

