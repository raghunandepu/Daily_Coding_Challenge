# https://www.algoexpert.io/questions/Powerset

"""

​
Powerset
​
Write a function that takes in an array of unique integers and returns its powerset. The powerset P(X) of a set X is the set of all subsets of X. For example, the powerset of [1,2] is [[], [1], [2], [1,2]]. Note that the sets in the powerset do not need to be in any particular order.
​
Sample input: [1, 2, 3]
Sample output: [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]"""

# Solution 1: Using iterative way

# O(n*2^n) time | O(n*2^n) space

# for n elements, there are 2 ^n subsets.

def powerset(array):
    subsets = [[]]
    for ele in array:
        for i in range(len(subsets)):
            currentSubset = subsets[i]
            subsets.append(currentSubset + [ele])
    return subsets
  
# Solution 2: Recursive way
# O(n*2^n) time | O(n*2^n) space - Same as iterative
def powerset2(array, idx=None):
    if idx is None:
        idx = len(array) - 1
    if idx < 0:
        return [[]]
    ele = array[idx]
    subsets = powerset2(array, idx - 1)
    
    #Same logic as in solution 1
    for i in range(len(subsets)):
        currentSubset = subsets[i]
        subsets.append(currentSubset + [ele])
    return subsets