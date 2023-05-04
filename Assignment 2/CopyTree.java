/*  
 * 
 */

public class CopyTree {
    
    public Node copyTree(Node root){
        if(root == null)
            return null;
        
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
