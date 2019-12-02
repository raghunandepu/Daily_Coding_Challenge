# Linkedlist construction
"""
Linked List Construction
​
Write a class for a Doubly Linked List. The class should have a "head" and "tail" properties, both of which should point to either the None (null) value or to a Linked List node. Every node will have a "value" property as well as "next" and "prev" properties, both of which can point to either the None (null) value or another node. The class should support setting the head and tail of the linked list, inserting nodes before and after other nodes as well as at certain positions, removing given nodes and removing nodes with specific values, and searching for nodes with values. Only the searching method should return a value: specifically, a boolean.
​
Sample input:
1 -> 2 -> 3 -> 4 -> 5
Sample output (after setting 4 to head):
4 -> 1 -> 2 -> 3 -> 5
Sample output (after setting 6 to tail):
4 -> 1 -> 2 -> 3 -> 5 -> 6
Sample output (after inserting 3 before 6):
4 -> 1 -> 2 -> 5 -> 3 -> 6
Sample output (after inserting a new 3 after 6):
4 -> 1 -> 2 -> 5 -> 3 -> 6 -> 3
Sample output (after inserting a new 3 at position 1):
3 -> 4 -> 1 -> 2 -> 5 -> 3 -> 6 -> 3
Sample output (after removing nodes with value 3):
4 -> 1 -> 2 -> 5 -> 6
Sample output (after removing 2):
4 -> 1 -> 5 -> 6
Sample output (after searching for 5): True
"""

class DoublyLinkedList:
  def __init__ (self):
    self.head = None
    self.tail = None
   
   # O(1) time | O(1) space 
  def setHead(self, node):
    if self.head is None:
      self.head = node
      self.tail = node
      return
    self.insertBefore(self.head, node)
    
  # O(1) time | O(1) space
  def setTail(self, node):
    if self.tail is None:
      self.setHead(node)
      return
    self.insertAfter(self.tail, node)
  
  # O(1) time | O(1) space
  def insertBefore(self, node, nodeToInsert):
    # case when there is only one node
    if nodeToInsert == self.head and nodeToInsert == self.tail:
      return
    # removing it if node is already present
    self.remove(nodeToInsert)
    nodeToInsert.prev = node.prev
    nodeToInsert.next = node
    
    if node.prev is None:
      self.head = nodeToInsert
    else:
      node.prev.next = nodeToInsert
    node.prev = nodeToInsert
  
  # O(1) time | O(1) space
  def insertAfter(self, node, nodeToInsert):
    if nodeToInsert == self.head and nodeToInsert == self.tail:
      return
    self.remove(nodeToInsert)
    nodeToInsert.prev = node
    nodeToInsert.next = node.next
    
    
    if node.next is None:
      self.tail = nodeToInsert
    else:
      node.next.prev = nodeToInsert
    node.next = nodeToInsert
    
  # O(p) time  where p is position | O(1) space
  def insertAtPosition(self, position, nodeToInsert):
    if position == 1:
      self.setHead(nodeToInsert)
      return
    node = self.head
    currentPosition = 1
    while node is not None and currentPosition != position:
      node = node.next
      currentPosition += 1
    if node is not None:
      self.insertBefore(node, nodeToInsert)
    else:
      self.setTail(nodeToInsert)
  
  # O(n) time | O(1) space
  def removeNodesWithValue(self, value):
    # first we have to search for the given value and then remove it
    # combination of search and remove methods
    node = self.head
    while node is not None:
      nodeToRemove = node # inorder not to lose track of nodes, using nodeToRemove here to store node
      node = node.next
      if nodeToRemove.value == value:
        self.remove(nodeToRemove)
  
  # O(1) time | O(1) space
  def remove(self, node):
    # if node is equal to head
    if node == self.head:
      self.head = self.head.next
      
    # if node is equal to tail
    if node == self.tail:
      self.tail = self.tail.prev
      
    self.removeNodeBindings(node) # calling helpler method (see below) to remove node other than head or tail
  
  # O(n) time | O(1) space
  def containsNodeWithValue(self, value):
    node = self.head
    while node is not None and node.value != value:
      node = node.next
    return node is not None
  
  def removeNodeBindings(self, node):
    # updating previous nodes next pointer before removing it
    if node.prev is not None:
      node.prev.next = node.next # updating previous node's next pointer to current node's next 
    
    # Updating previous nodes next pointer to current prev before removing it
    if node.next is not None:
      node.next.prev = node.prev
    
    # Removin the bindings or connections now 
    node.prev = None
    node.next = None
    