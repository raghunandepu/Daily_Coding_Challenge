# https://www.interviewbit.com/problems/counting-triangles/
"""
You are given an array of N non-negative integers, A0, A1 ,…, AN-1.
Considering each array element Ai as the edge length of some line segment, count the number of triangles which you can form using these array values.

Notes:

You can use any value only once while forming each triangle. Order of choosing the edge lengths doesn’t matter. Any triangle formed should have a positive area.

Return answer modulo 109 + 7.

For example,

A = [1, 1, 1, 2, 2]

Return: 4"""

class Solution:
    # @param A : list of integers
    # @return an integer
    def nTriang(self, A):
        M = 1e9 + 7
        count = 0
        A.sort()
        for end in range(len(A)-1, -1, -1):
            start = 0
            k = end -1
            while start < k:
                if A[start] + A[k] <= A[end]:
                    start += 1
                else:
                    count += k - start
                    k -= 1
        return int(count % M)

