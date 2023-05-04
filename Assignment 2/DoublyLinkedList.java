public class DoublyLinkedList {

    // creates new Node with data val at front; returns new head
    public Node insertAtFront(Node head, int val) {
        Node newNode = new Node(val, null, head);

        if(head != null)
            head.prev = newNode;
        return newNode;
    }

    // creates new Node with data val at end
    public void insertAtBack(Node head, int val) {
        Node newNode = new Node(val, null, null);

        if(head == null)
            head = newNode;

        Node current = head;
        while(current.next != null)
            current = current.next;
        
        current.next = newNode;
        newNode.prev = current;
        
    }

    // creates new Node with data val after Node loc
    public void insertAfter(Node head, int val, Node loc) {
        if(head == null || loc == null)
            return;

        Node newNode = new Node(val, loc, loc.next);
        if(loc.next != null)
            loc.next.prev = newNode;
        
        loc.next = newNode;
    }

    // removes first Node; returns new head
    public Node deleteFront(Node head) {
        if(head == null)
            return head;
        
        Node newNode = head.next;
        if (newNode != null)
            newNode.prev = null;
        
            head.next = null;
            return newNode;
    }

    // removes last Node
    public void deleteBack(Node head) {
        if(head == null)
            return;
        if(head.next == null){
            head = null;
            return;
        }

        Node current = head;
        while(current.next != null)
            current = current.next;

        // removes the last element
        current.prev.next = null;
        
    }

    // deletes Node loc; returns head
    public Node deleteNode(Node head, Node loc) {
        if(head == null || loc == null)
            return head;


        return head;
    }

    // returns length of the list
    public int length(Node head) {
        int size = 0;
        Node current = head;
        while(current != null){
            size ++;
            current = current.next;
        }

        return size;
    }

    // reverses the linked list iteratively
    public Node reverseIterative(Node head) {
        if(head == null || head.next == null)
            return head;
        
        Node current = head;
        while(current != null){

            //adds new node to the front
            Node temp = current.next;
            current.next = current.prev;
            current.prev = temp;

            //checks for the end of the list
            if(temp == null){
                head = current;
            }

            // moves to next node
            current = temp;
        }

        return head;
    }

    // reverses the linked list recursively (Hint: you will need a helper function)
    public Node reverseRecursive(Node head) {
        if(head == null || head.next == null)
            return head;
        
        Node newNode = reverseRecursive(head.next);
        
        // cutting connections
        head.next.prev = null;
        head.next = null;

        // flipping order
        head.prev = newNode;
        newNode.next = head;

        return newNode;
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