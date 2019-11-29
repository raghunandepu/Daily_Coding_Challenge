"""Group Anagrams
​
Write a function that takes in an array of strings and returns a list of groups of anagrams. Anagrams are strings made up of exactly the same letters, where order doesn't matter. For example, "cinema" and "iceman" are anagrams; similarly, "foo" and "ofo" are anagrams. Note that the groups of anagrams don't need to be ordered in any particular way.
​
Sample input: ["yo", "act", "flop", "tac", "cat", "oy", "olfp"]
Sample output: [["yo", "oy"], ["flop", "olfp"], ["act", "tac", "cat"]]"""

# Time: O(w * n * log(n)) | O(wn) space
def groupAnagrams(words):
  anagrams = {}
  for word in words:
    sortedWord = "".join(sorted(word))
    if sortedWord in anagrams:
      anagrams[sortedWord].append(word)
    else:
      anagrams[sortedWord] = [word]
  return list(anagrams.values())

words = ["yo", "act", "flop", "tac", "cat", "oy", "olfp"]  
print (groupAnagrams(words))
