/*  Space complexity is O(1)
    there is only space required for a constant number of dummy
    pointer variables

    Time complexity is O(n)
    this algorithm is based off of Floyd's cycle finding algorithm. An algorithm that 
    I do not completely understand the proof for but I know it and I know it works. I do know
    that the function itterates through the list until it detects a cylce through a fast and slow pointer.
    Then through some magic, the start of the loop is found when the slow and fast pointers meet again 
    after one of the pointers has been set to the start of the list


    this took my 25 minutes
 * 
 */

public class DisconnectCycle {


    public static void disconnectCycle(Node head) {
        Node slow = head;
        Node fast = head;
    
        // Find the meeting point of the two pointers
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) {
                break;
            }
        }
    
        // check for cycle
        if (fast == null || fast.next == null)
            return;
        
    
        // somehow this works
        slow = head;
        while (slow != fast) {
            slow = slow.next;
            fast = fast.next;
        }

        // goes all the way though cycle again to cut connection
        Node prev = null;
        while (fast != null && fast != slow) {
            prev = fast;
            fast = fast.next;
        }
        prev.next = null;
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
