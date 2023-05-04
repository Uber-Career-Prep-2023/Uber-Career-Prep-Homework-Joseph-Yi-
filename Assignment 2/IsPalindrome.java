/*  Space complexity is O(1)
    the only space requriecd is for simply dummy pointer nodes

    Time complextiy is O(n)
    the function must traverse through the entire list to ensure
    that is is a palindrome, thus resulting in O(n)

    this problem took me 9 minutes
 * 
 */

public class IsPalindrome {

    public boolean isPalindrome(Node head){

        Node front = head;

        Node end = head;
        while (end != null && end.next != null) {
            end = end.next;
        }
        
        while (front != end && end.next != front) {
            
            // compares
            if (front.val != end.val)
                return false;
        
            // moves pointers towards the center
            front = front.next;
            end = end.prev;
        }
        return true;
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
