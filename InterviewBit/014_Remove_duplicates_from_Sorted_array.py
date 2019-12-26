# https://www.interviewbit.com/problems/remove-duplicates-from-sorted-array/
"""
Asked in:  
United Healthgroup
Amazon
Google
Microsoft
Expedia
Bookmark Suggest Edit
Remove duplicates from Sorted Array
Given a sorted array, remove the duplicates in place such that each element appears only once and return the new length.

Note that even though we want you to return the new length, make sure to change the original array as well in place

Do not allocate extra space for another array, you must do this in place with constant memory.

 Example: 
Given input array A = [1,1,2],
Your function should return length = 2, and A is now [1,2]. 

"""
# Time Complexity : O(n)
# Auxiliary Space : O(1)

class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        n = len(A)
        if n == 0 or n == 1:
            return n
        
        j = 0 # To store index for the unique element
        
        # If current element is 
        # not equal to next 
        # element then store that 
        # current element at index j
        for i in range(0, n-1):
            if A[i] != A[i+1]:
                A[j] = A[i]
                j += 1
        # Store the last element 
        # as whether it is unique 
        # or repeated, it hasn't 
        # stored previously        
        A[j] = A[n-1]
        j+= 1
    
        return A and j