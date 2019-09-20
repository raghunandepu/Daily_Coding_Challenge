""""A palindrome is a string that reads the same forward and backward"

For example: radar or madam

Our task is to design an optimal algorithm for checking whether a given string is palindrome or not! """

# Solution:
# We compare first index of string with last index of string using two pointers
# O(1) space

def palindrome_check(s):
  left_index = 0
  right_index = len(s)-1
  while (left_index < right_index):
    if s[left_index] != s[right_index]:
      return False
    left_index += 1
    right_index -= 1
  return True

if __name__ == "__main__":
  s = "madam"
  print (palindrome_check(s))
  
  # Another solution in python
  """def is_palindrome(s):
    return s==''.join(s[::-1])
  print (is_palindrome("abc"))"""