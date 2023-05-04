/*  Space is O(1)
    the only extra space required are for temp dummy variables. 

    Time complexity is O(n)
    the function has to traverse through the entire list in order to 
    fine all possible duplicates. This makes the time dependent on the length
    of the list or O(n)
 * 
 */

public class DedupSortedList {
    
    public Node dedupSortedList(Node head) {
        if (head == null || head.next == null) {
            return head;
        }

        Node current = head;
        while (current.next != null) {
            
            // checks for matching values
            if (current.val == current.next.val)
                current.next = current.next.next;
            
            else
                current = current.next;

        }

        return head;
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
