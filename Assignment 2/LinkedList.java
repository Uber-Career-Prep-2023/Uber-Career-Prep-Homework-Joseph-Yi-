
public class LinkedList {
	
	// creates new Node with data val at front; returns new head
	public Node insertAtFront(Node head, int val) {
		return new Node(val, head);
	}

	// creates new Node with data val at end
	public void insertAtBack(Node head, int val) {

		if(head == null)
			head = new Node(val, head);
		
		Node current = head;
		while(current.next != null) {
			current = current.next;
		}

		current.next = new Node(val, null);
	}

	// creates new Node with data val after Node loc
	public void insertAfter(Node head, int val, Node loc) {
		if(head == null || loc == null)
			return;
		
		loc.next = new Node(val, loc.next);
	}

	// removes first Node; returns new head
	public Node deleteFront(Node head) {

		if(head == null)
			return head;

		Node rem = head;
		head = head.next;
		rem.next = null;
		return head;
	}

	// removes last Node
	public void deleteBack(Node head) {
		if(head == null)
			return;
		else if(head.next == null)
			head = null;
		else {
			//finds last node
			Node current = head.next;
			Node before = head;
			while(current != null) {
				
				if(current.next == null) {
					
					before.next = null;
				}
				current = current.next;
				before = before.next;
			}
		}
	}

	// deletes Node loc; returns head
	public Node deleteNode(Node head, Node loc) {
		
		//handles special cases
		if(head == null || loc == null)
			return head;
		
		if(head.val == loc.val) {
			Node toRem = head;
			head = head.next;
			toRem.next = null;
			return head;
		}
		
		//finds target
		Node current = head.next;
		Node prev = head;
		while(current != null) {
			
			//removes target node
			if(current.val == loc.val) {

				prev.next = current.next;
				current.next = null;
				return head;
			}
			current = current.next;
			prev = prev.next;
		}

		return head;
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

 	// reverses the linked list iteratively
	public Node reverseIterative(Node head) {
		Node prev = null;
		Node curr = head;

		while(curr != null) {
			Node next = curr.next;
			curr.next = prev;
			prev = curr;
			curr = next;
		}

		return prev;
	}
	
	// reverses the linked list recursively (Hint: you will need a helper function)
	public Node reverseRecursive(Node head) {

		if(head == null || head.next == null)
			return head;

		Node reverse = reverseRecursive(head.next);
		
		// flips the connections
		head.next.next = head;
		head.next = null;

		return reverse;
	}

	private class Node {

		private int val;
		private Node next;

		public Node(int val, Node next){
			this.val = val;
			this.next = next;
		}
	}
}
