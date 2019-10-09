"""
Caesar Cipher Encryptor
​
Given a non-empty string of lowercase letters and a non-negative integer value representing a key, write a function that returns a new string obtained by shifting every letter in the input string by k positions in the alphabet, where k is the key. Note that letters should "wrap" around the alphabet; in other words, the letter "z" shifted by 1 returns the letter "a".
​
Sample input: "xyz", 2
Sample output: "zab"
"""

def caesarCipherEncryptor(string, key):
  newLetter = []
  newKey = key % 26
  for letter in string:
    newLetter.append(getNewLetter(letter, newKey))
  return "".join(newLetter)

def getNewLetter(letter, key):
  newLetterCode = ord(letter) + key
  return chr(newLetterCode) if newLetterCode <= 122 else chr(96 + newLetterCode % 122)

string = "xyz"
key = 2
print (caesarCipherEncryptor(string, key))