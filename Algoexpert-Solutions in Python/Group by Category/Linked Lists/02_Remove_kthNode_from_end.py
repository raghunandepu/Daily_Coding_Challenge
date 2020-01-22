# https://www.algoexpert.io/questions/Remove%20Kth%20Node%20From%20End
"""
Remove Kth Node From End
​
Write a function that takes in the head of a Singly Linked List and an integer k (assume that the list has at least k nodes). The function should remove the kth node from the end of the list. Note that every node in the Singly Linked List has a "value" property storing its value as well as a "next" property pointing to the next node in the list or None (null) if it is the tail of the list.
​
Sample input: 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9, 4
Sample output: 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 7 -> 8 -> 9
​
"""
# O(N), O(1)
# where N is the number of nodes
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
        
def removeNthNodeFromEnd(head, n):
  counter = 1
  first = head
  second = head
  while counter <= n:
    second = second.next
    counter += 1
  if second is None:
    # it means we need to remove the first node which is at nth position from last
    head.value = head.next.value
    head.next = head.next.next
    return
    
  # here we are checking second.next not second
  while second.next is not None:
    #first is pointing to the node right before the one we want to delete
    first = first.next
    second = second.next
  first.next = first.next.next 
  
  
  
    
    
    

