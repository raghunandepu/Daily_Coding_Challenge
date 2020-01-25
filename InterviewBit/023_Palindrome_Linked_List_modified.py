# https://www.interviewbit.com/problems/palindrome-list/
# Asked in Amazon, Microsoft

"""
Given a singly linked list, determine if its a palindrome. Return 1 or 0 denoting if its a palindrome or not, respectively.

Notes:

Expected solution is linear in time and constant in space.
For example,

List 1-->2-->1 is a palindrome.
List 1-->2-->3 is not a palindrome."""

import sys
class node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None
  
  def display(self):
    temp = self.head
    while temp:
      print(temp.data)
      temp = temp.next
  
  def count(self):
    counter = 0
    temp = self.head
    while temp:
      counter += 1
      temp = temp.next
    return counter
  
  def search(self, value):
    temp = self.head
    pos = 1
    while temp:
      if temp.data == value:
        print("The value found at", pos)
      temp = temp.next
      pos += 1
    print("Value not found in the linked list")
    
  def insert_at_beginning(self, data):
    self.temp = node(data)
    if self.head is None:
      self.head = self.temp
      return
    self.temp.next = self.head
    self.head = temp
    
  def insert_at_end(self, data):
    self.temp = node(data)
    if self.head is None:
      self.head = self.temp
      return
    self.p = self.head
    while self.p.next is not None:
      self.p = self.p.next
    self.p.next = self.temp
    
  def insert_after_given_node(self, data, item):
    self.p = self.head
    while self.p is not None:
      if self.p.data == item:
        self.temp = node(data)
        self.temp.next = self.p.next
        self.p.next = self.temp
        return
      self.p = self.p.next
    print ("Item not found")
  
  def insert_at_pos(self, data, pos):
    self.temp = node(data)
    if pos == 1:
      self.temp.next = self.head
      self.head = self.temp
    self.p = self.head
    while pos > 2 and self.p is not None:
      self.p = self.p.next
      pos -= 1
    if self.p is None:
      print ("Position exceeded the length of the list")
    else:
      self.temp.next = self.p.next
      self.p.next = self.temp
      
  def delete(self, data):
    if self.head is None:
      print ("list is empty")
      return
    if self.head.data == data:
      self.temp = self.head  # just storing the node in temp to be deleted
      self.head = self.head.next
      return
      
    self.p = None # mainting a prev pointer to connect later
    self.curr = self.head
    while self.curr is not None:
      if self.curr.data == data:
        self.temp = self.p.next
        self.p.next = self.temp.next
        return
        
      self.p = self.curr
      self.curr = self.curr.next
      
def reverse(head):
  prev = None
  curr = head
  while curr is not None:
    Next = curr.next 
    curr.next = prev
    prev = curr
    curr = Next
  head = prev
  return head

def compareList(head1, head2):
  while head1 is not None and head2 is not None:
    if head1.data == head2.data:
      head1 = head1.next
      head2 = head2.next
    else:
      return False
    
  if head1 is None and head2 is None:
    return True
  return False
  

# Time: O(n), space: 0(1) using two pointer technique
def isPalindrome(llist):
  head = llist.head
  slowptr = head
  fastptr = head
  slow_prev = None
  nextHalf = None
  midnode = None
  
  if head is not None and head.next is not None:
    while fastptr is not None and fastptr.next is not None:
      fastptr = fastptr.next.next 
      slow_prev = slowptr # saving slow prev pointer also here
      slowptr = slowptr.next
    
    if fastptr is not None:
      # it means we are checking for odd length palindrome
      midnode = slowptr
      slowptr = slowptr.next # next half starting
    
    nextHalf = slowptr
    slow_prev.next = None # cutting the first half
    nextHalf = reverse(nextHalf) # using reverse function created above
    result = compareList(head, nextHalf)
    nextHalf = reverse(nextHalf) # reverting back the reversed second half
    
    # Now we need to join back the second half with first half.
    if midnode is not None:
      slow_prev.next = midnode
      midnode.next = nextHalf
    else:
      slow_prev.next = nextHalf
  return result
        
        
if __name__=='__main__':
    llist=LinkedList()
    n=int(input())
    for i in range(n):
        llist.insert_at_end((input()))
    if isPalindrome(llist) is True:
        print("palindrome")
    else:
        print("Not palindrome")
        
        
        
  
      
    
