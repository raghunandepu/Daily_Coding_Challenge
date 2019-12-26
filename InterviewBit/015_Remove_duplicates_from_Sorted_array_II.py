# https://www.interviewbit.com/problems/remove-duplicates-from-sorted-array-ii/
"""
Remove Duplicates from Sorted Array II
Asked in:  
Expedia
Microsoft
Bookmark Suggest Edit
Remove Duplicates from Sorted Array

Given a sorted array, remove the duplicates in place such that each element can appear atmost twice and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

Note that even though we want you to return the new length, make sure to change the original array as well in place

For example,
Given input array A = [1,1,1,2],

Your function should return length = 3, and A is now [1,1,2]."""

# pretty much same as previous problem https://www.interviewbit.com/problems/remove-duplicates-from-sorted-array/

# Time: O(n), space: O(1)

class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        n = len(A)
        if n < 3:
            return A and n
        pos = 1
        for i in range(1, n-1):
            if A[i-1] != A[i+1]:
                A[pos] = A[i]
                pos += 1
        A[pos] = A[n-1]
        
        return A and pos+1
