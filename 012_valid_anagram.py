# Anagram problem overview
"""Construct an algorithm to check whether two words (or phrases) are anagrams or not!"""

# SOLUTION:
# We are using dictionary here to store count of each letter for string 1.
# For string2, if the same letter exists in dictionary already, we reduce the counter of that letter. At the end, values of each letter/key should be 0 otherwise it is not an anagram.

def anagram_check(s1, s2):
  if len(s1) != len(s2):
    return False
  dict1 = {}
  for i in s1:
    if i not in dict1:
      dict1[i] = 1
    else:
      dict1[i] += 1
  
  for j in s2:
    if j not in dict1:
      return False
    else:
      dict1[j] -= 1
  
  for val in dict1.values():
    if val !=0:
      return False
  return True

if __name__ == '__main__':
  s1 = 'anagram'
  s2 = 'nagaram'

  print (anagram_check(s1, s2))