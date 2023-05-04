public class DoublyLinkedList {

    // creates new Node with data val at front; returns new head
    public Node insertAtFront(Node head, int val) {
        return null;
    }

    // creates new Node with data val at end
    public void insertAtBack(Node head int val) {

    }

    // creates new Node with data val after Node loc
    public void insertAfter(Node head, int val, Node loc) {

    }

    // removes first Node; returns new head
    public Node deleteFront(Node head) {
        return null;
    }

    // removes last Node
    public void deleteBack(Node head) {

    }

    // deletes Node loc; returns head
    public Node deleteNode(Node head, Node loc) {

    }

    // returns length of the list
    public int length(Node head) {

    }

    // reverses the linked list iteratively
    public Node reverseIterative(Node head) {
        return null;
    }

    // reverses the linked list recursively (Hint: you will need a helper function)
    public Node reverseRecursive(Node head) {
        return null;
    }

    public class Node {

		private int val;
		private Node next;
        private Node prev;

		public Node(int val, Node prev, Node next){
			this.val = val;
			this.next = next;
		}
	}
}