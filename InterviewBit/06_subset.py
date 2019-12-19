"""
https://www.interviewbit.com/problems/subset/

Asked in:  
Amazon
Microsoft

Given a set of distinct integers, S, return all possible subsets.

 Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
Also, the subsets should be sorted in ascending ( lexicographic ) order.
The list is not necessarily sorted.
Example :

If S = [1,2,3], a solution is:

[
  [],
  [1],
  [1, 2],
  [1, 2, 3],
  [1, 3],
  [2],
  [2, 3],
  [3],
]"""

def subsets(A):
    res_subsets = [[]]
    for ele in sorted(A):
        for i in range(len(res_subsets)):
            currentSubset = res_subsets[i]
            res_subsets.append(currentSubset +[ele])
    return sorted(res_subsets)
  
A = [ 15, 20, 12, 19, 4 ]
print (subsets(A))
  