class Node:
   def __init__(self, value=None, next=None):
      self.val = value
      self.next = next

# creates new Node with data val at front; returns new head
def insertAtFront(head, val):
   return Node(val, head)
   
# creates new Node with data val at end
def insertAtBack(head, val):
   

# creates new Node with data val after Node loc
def insertAfter(head, val, loc):


# removes first Node; returns new head
def deleteFront(head):
   

# removes last Node
def deleteBack(head):

# deletes Node loc; returns head
def deleteNode(head, loc):

# returns length of the list
def length(head):

# reverses the linked list iteratively
def reverseIterative(head):

# reverses the linked list recursively (Hint: you will need a helper function)
def reverseRecursive(head):