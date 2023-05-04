/*  Space complexity is O(1)
    there is no extra space required from variables. this makes it O(1)

    Time complexity is O(n)
    in order to test the BST property, you must visit every node in the tree and compare its
    parent and children. Therefore, the time complexity is O(n)

    I spent 8 minutes on this problem
 */

public class IsBST {

    public boolean isBST(Node root) {
        return isBSTHelper(root, null, null);
    }

    private boolean isBSTHelper(Node node, Integer min, Integer max) {
        if(node == null)
            return true;

        // checks property
        if ((min != null && node.val <= min) || (max != null && node.val >= max))
            return false;
        
        
        // call on left and right ensuring that nothing in left is larger than value
        // and that nothing is right is less than value
        return isBSTHelper(node.left, min, node.val) && isBSTHelper(node.right, node.val, max);
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
