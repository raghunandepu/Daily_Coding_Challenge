"""Caesar Cipher Encryptor
​
Given a non-empty string of lowercase letters and a non-negative integer value representing a key, write a function that returns a new string obtained by shifting every letter in the input string by k positions in the alphabet, where k is the key. Note that letters should "wrap" around the alphabet; in other words, the letter "z" shifted by 1 returns the letter "a".
​
Sample input: "xyz", 2
Sample output: "zab"
"""

# Solution: Create an empty list. For each character in the given string, get the new index by appending the key and modulo len(alphabet). Get the corresponding char of new index from alphabet and append it to new list. Join the chars at end. 

# Note: Modulo (%) by len(alphabet) is needed to get 0 i.e first element when we reach the end of the alphabets.

# Time: O(n) | Space: O(n)

def caesarCipherEncryptor(string, key):
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  new_string = []
  for char in string.lower():
    idx = (alphabet.index(char) + key) % len(alphabet)
    new_string.append(alphabet[idx])
  return "".join(new_string)

print (caesarCipherEncryptor("xyz", 2))