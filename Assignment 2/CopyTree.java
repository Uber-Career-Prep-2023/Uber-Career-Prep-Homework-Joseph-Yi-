/*  Space complexity is O(n)
    since we are creating a deep copy of the entire tree, there is a new
    node for each value in the tree. Thus there is a new n nodes created

    Time complexity is O(n)
    the only way you can create a copy of each node is to access each node and
    traverse through the entire tree. This makes the total time complexity O(n) 
    being dependent on the number of elements in the tree

    I spent 6 minutes on this problem
 */

public class CopyTree {
    
    public Node copyTree(Node root){
        if(root == null)
            return null;
        
        // creates the deep copy node
        Node newNode = new Node(root.val, null, null);
        
        // copy subtrees
        newNode.left = copyTree(root.left);
        newNode.right = copyTree(root.right);

        return newNode;
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
