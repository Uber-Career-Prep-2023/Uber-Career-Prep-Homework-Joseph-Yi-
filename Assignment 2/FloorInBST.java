/*  Space complexity is O(1)
    the only additional space needed was the use of a variable to store what to return

    Time Complexity is O(h) 
    The time is dependent on the heigh of the tree. As it traverses, it only
    traverses one path. If the tree is well ballanced, the time complexity will be
    O(log n) but if the tree is degenerate, the time complexity will be closer to O(n)

    this took me 11 minutes
 * 
 */

public class FloorInBST {
    
    public Node floorInBST(Node root, int target) {
        Node toReturn = null;
        while (root != null) {
            if (root.val == target)
                return root;
            
            // traverse left
            else if (root.val > target)
                root = root.left;
            // traverse righrt
            else {
                toReturn = root;
                root = root.right;
            }
        }
        return toReturn;
    }
    

    private class Node {

		private int val;
		private Node left;
		private Node right;

		public Node(int val, Node left, Node right){
			this.val = val;
			this.left = left;
			this.right = right;
		}
	}
}
