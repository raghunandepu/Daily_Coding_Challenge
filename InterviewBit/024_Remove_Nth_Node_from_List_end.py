# https://www.interviewbit.com/problems/remove-nth-node-from-list-end/

"""
Remove Nth Node from List End
Asked in:  
HCL
Amazon

Given a linked list, remove the nth node from the end of list and return its head.

For example,
Given linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5.

 Note:
If n is greater than the size of the list, remove the first node of the list.
Try doing it using constant additional space."""

# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def removeNthFromEnd(self, A, B):
        def length_of_list(A):
            count = 0
            temp = A
            while temp:
                count += 1
                temp = temp.next
            return count
        
        n = B
        list_len = length_of_list(A)
        
        # if n is greater than list length, remove first node
        if n >= list_len:
            A = A.next
        
        else:
            count = 0
            curr = A
            
            # We need to remove (list_len - n + 1)th element from begining
            while count != list_len - n - 1:
                curr = curr.next
                count += 1
            if curr.next is not None:
                curr.next = curr.next.next
        return A