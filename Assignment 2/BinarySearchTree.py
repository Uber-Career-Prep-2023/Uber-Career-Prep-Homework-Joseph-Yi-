class Node:
   def __init__(self, value=None, left=None, right=None):
      self.val = value
      self.left = left
      self.right = right


class BinarySearchTree:
   
   # returns the minimum value in the BST
   int min():

   # returns the maximum value in the BST
   int max():

   # returns a boolean indicating whether val is present in the BST
   bool contains(int val):

   # For simplicity, do not allow duplicates. If val is already present, insert is a no-op
   # creates a new Node with data val in the appropriate location
   void insert(int val):

   # deletes the Node with data val, if it exists
   int delete(int val) 
