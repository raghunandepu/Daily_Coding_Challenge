# https://www.interviewbit.com/problems/search-for-a-range/

"""
Search for a Range
Asked in:  
Google
Microsoft

Given a sorted array of integers A(0 based index) of size N, find the starting and ending position of a given integar B in array A.

Your algorithm’s runtime complexity must be in the order of O(log n).

Return an array of size 2, such that first element = starting position of B in A and second element = ending position of B in A, if B is not found in A return [-1, -1].



Input Format

The first argument given is the integer array A.
The second argument given is the integer B.
Output Format

 Return an array of size 2, such that first element = starting position of B in A and second element = ending position of B in A, if B is not found in A return [-1, -1].
Constraints

1 <= N <= 10^6
1 <= A[i], B <= 10^9
For Example

Input 1:
    A = [5, 7, 7, 8, 8, 10]
    B = 8
Output 1:
    [3, 4]
Explanation 1:
    First occurence of 8 in A is at index 3
    Second occurence of 8 in A is at index 4
    ans = [3, 4]

Input 2:
    A = [5, 17, 100, 111]
    B = 3
Output 2:
    [-1, -1]"""


class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers

          
    def searchRange(self, A, B):
        finalRange = [-1, -1]
        self. alteredBinarySearch(A, B, 0, len(A) - 1, finalRange, True)
        self. alteredBinarySearch(A, B, 0, len(A) - 1, finalRange, False)
        return finalRange
    
    def alteredBinarySearch(self, A, B, left, right, finalRange, goLeft):
        while left <= right:
            mid = (left + right) // 2
            if A[mid] < B:
                left = mid + 1
            elif A[mid] > B:
                 right = mid - 1
    
            else:
                if goLeft:
                    if mid == 0 or A[mid - 1] != B:
                        finalRange[0] = mid
                        return
                    else:
                        right = mid - 1
                else:
                    if mid == len(A) -1  or A[mid + 1] != B:
                        finalRange[1] = mid
                        return
                    else:
                        left = mid + 1
    
        