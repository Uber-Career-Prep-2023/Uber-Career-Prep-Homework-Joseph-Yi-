public class BinarySearchTree {

	private Node root;

	// returns the minimum value in the BST
   	public int min() {
   		return findMin(root);
   	}

   	private int findMin(Node node) {
		if(node == null)
			return -1;

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
			return -1;
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

	private Node insert(int val, Node node) {

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
		this.root = delete(this.root, val);
		return val;
	}

	private Node delete(Node node, int val) {
		if(node == null)
			return null;
		if (val < node.val)
            node.left = delete(node.left, val);
        else if (val > node.val)
            node.right = delete(node.right, val);
        else {
			
			// no children
			if(node.left == null && node.right == null)
				node = null;
		
			// only 1 child
			else if(node.left == null)
				node = node.right;
			else if(node.right == null)
				node = node.left;

			// node has 2 children
			else {

				// inorder successor
				Node replace = findMinNode(node.right);

				// replace value
				node.val = replace.val;

				// recurse again to delete
				node.right = delete(node.right, replace.val);
			}
		}

		return node;
	}

	private Node findMinNode(Node node) {

		while(node.left != null)
			node = node.left;
		return node;
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