public class BinarSearchTree {

	private Node root;

	// returns the minimum value in the BST
   	public int min() {
   		return findMin(root);
   	}

   	private int findMin(Node node) {
		if(node == null)
			return null;

		//goes all the way left
		if(node.left == null)
			return node.val;

		return findMin(node.left);
	}

	// returns the maximum value in the BST
	public int max() {
		return findMax(root);
	}

	private int findMax(Node node) {
		if(node == null) {
			return null;
		}
		//goes all the way right
		if(node.right == null)
			return node.val;
		return findMax(node.right);
	}



	// returns a boolean indicating whether val is present in the BST
	public boolean contains(int val) {
		return contains(root, val);
	}

	private boolean contains(Node node, int val) {
		if(node == null)
			return false;
		if(node.val == val)
			return true;

		if(val < node.val)
			return contains(node.left, val);
		else
			return contains(node.right, val);
	}

	// For simplicity, do not allow duplicates. If val is already present, insert is a no-op
	// creates a new Node with data val in the appropriate location
	public void insert(int val) {
		root = insert(val, root);
	}

	public Node insert(Node node, int val) {

		if(node == null)
			return new Node(val, null, null);

		if(val < node.val)
			node.left = insert(val, node.left);
		else if(val > node.val)
			node.right = insert(val, node.right);

		return node;
	}


	// deletes the Node with data val, if it exists
	public int delete(int val) {
		
	}

	private Node delete(Node node, int val) {

	}

	private 

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