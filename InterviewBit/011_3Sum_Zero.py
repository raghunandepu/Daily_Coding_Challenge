# https://www.interviewbit.com/problems/3-sum-zero/

"""
3 Sum Zero
Asked in:  
Facebook
Google

Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.

Note:

 Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
The solution set must not contain duplicate triplets. For example, given array S = {-1 0 1 2 -1 -4}, A solution set is:
(-1, 0, 1)
(-1, -1, 2) """

# @param A : list of integers
# @return a list of list of integers

# O(n^2) time | O(n) space

def threeSum(A):
    targetSum = 0
    A.sort()
    triplets = []
    for i in range(len(A) -2):
        if A[i] >0:
            break # since we do not check if all are positive numbers
        if i > 0 and A[i] == A[i-1]:
            continue
        left = i+1
        right = len(A) -1
        while left < right:
            currentSum = A[i] + A[left] + A[right]
            if currentSum == targetSum:
                triplets.append([A[i], A[left],A[right]])
                # Logic begin to avoid duplicate triplets
                while left < right and  A[left] == A[left+ 1]:
                  left += 1
                while left < right and  A[right] == A[right - 1]:
                  right -= 1
                # Logic end to avoid duplicate triplets
                left += 1
                right -= 1 
            elif currentSum < targetSum:
                left += 1
            elif currentSum > targetSum:
                right -= 1
    return triplets

A = [ 1, -4, 0, 0, 5, -5, 1, 0, -2, 4, -4, 1, -1, -4, 3, 4, -1, -1, -3 ]

print (threeSum(A))