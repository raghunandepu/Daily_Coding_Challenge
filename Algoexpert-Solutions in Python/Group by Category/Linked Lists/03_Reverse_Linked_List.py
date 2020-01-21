# https://www.algoexpert.io/questions/Reverse%20Linked%20List

"""
Reverse Linked List
​
Write a function that takes in the head of a Singly Linked List (assume that the list has at least 1 node; in other words, the head will never be a null value). The function should reverse the list and return its new head. Note that every node in the Singly Linked List has a "value" property storing its value as well as a "next" property pointing to the next node in the list or None (null) if it is the tail of the list."""
# Medium
# Time: O(n) where n is the length of the LL | Space: O(1)

# Approach: Remember to use three variables here, first pointer points to null first.
"""----
class Node:
  def __init__(self, value):
    self.next = None
 ---   """
def reverseLinkedList(head):
  p1 = None
  p2 = head
  while p2 is not None:
    p3 = p2.next 
    p2.next = p1
    p1 = p2
    p2 = p3
  return p1
    