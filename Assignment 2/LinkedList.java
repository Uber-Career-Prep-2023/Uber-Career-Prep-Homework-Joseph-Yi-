
public class LinkedList {
	
	// creates new Node with data val at front; returns new head
	public Node insertAtFront(Node head, int val) {
		return new Node(val, head);
	}

	// creates new Node with data val at end
	public void insertAtBack(Node head int val) {

		if(head == null)
			return new Node(val, head);
		
		Node current = head;
		while(current.next != null) {
			current = current.next;
		}

		current.next = new Node(val, null);
	}

	// creates new Node with data val after Node loc
	public void insertAfter(Node head, int val, Node loc) {

	}

	// removes first Node; returns new head
	public Node deleteFront(Node head) {

		if(head == null)
			return head;

		Node rem = head;
		head = head.next;
		to
	}

	// removes last Node
	public void deleteBack(Node head) {

	}

	// deletes Node loc; returns head
	public Node deleteNode(Node head, Node loc) {

	}
	
	// returns length of the list
	public int length(Node head) {
		
		int num = 0;
		Node current = head;

		//counts number of elements
		while(current != null) {
			num++;
			current = current.next;
		}
		return num;
	}

	public Node reverseIterative(Node head) // reverses the linked list iteratively
	public Node reverseRecursive(Node head) // reverses the linked list recursively (Hint: you will need a helper function)

	private class Node {

		private int val;
		private Node next;

		public Node(int val, Node next){
			this.val = val;
			this.next = next;
		}
	}
}
