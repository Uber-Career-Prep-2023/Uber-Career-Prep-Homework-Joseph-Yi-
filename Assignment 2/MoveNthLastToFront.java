/*  Space complexity is O(1)
    the only extra space is the space needed for dummy variables to 
    traverse through the list

    Time complexity is O(n)
    you will have to potentiall traverse through the entire list thus it is O(n)

    This problem took me about 15 minutes
 * 
 */

public class MoveNthLastToFront {
    
    public Node moveNthLastToFront(Node head, int n) {
        if (head == null || n <= 0) {
            return head;
        }

        Node first = head;
        Node second = head;
        
        // moves first n locations up
        for (int i = 0; i < n && first != null; i++) 
            first = first.next;
        
        // checks if first is valid
        if (first == null) 
            return head;
        
        // moves second to the nth last element
        while (first.next != null) {
            first = first.next;
            second = second.next;
        }

        // removes the nth last from position and moves to front
        Node target = second.next;
        second.next = target.next;
        target.next = head;
        return target;
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
