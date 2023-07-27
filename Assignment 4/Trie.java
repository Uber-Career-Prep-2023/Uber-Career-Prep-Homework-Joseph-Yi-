import java.util.*;


public class Trie {

    private TrieNode root;

    public Trie() {
        root = new TrieNode();
    }

    public void insert(String word) {

        TrieNode curr = root;
        for (char ch : word.toCharArray()) {
            int index = ch - 'a';
            
            if (curr.children.get(index) == null)
                curr.children.set(index, new TrieNode());

            curr = curr.children.get(index);
        }
        curr.validWord = true;
    }

    public boolean isValidWord(String word) {

        TrieNode node = findNode(word);
        return node != null && node.validWord;
    }

    public void remove(String word) {

        TrieNode node = findNode(word);
        if (node != null)
            node.validWord = false;
    }

    private TrieNode findNode(String word) {
        
        TrieNode curr = root;

        for (char ch : word.toCharArray()) {
            int index = ch - 'a';
            if (curr.children.get(index) == null)
                return null;
            
            curr = curr.children.get(index);
        }
        return curr;
    }

    private boolean hasChildren(TrieNode node) {
        
        for (TrieNode child : node.children) {
            if (child != null)
                return true;
        }
        return false;
    }

    private void deleteNode(TrieNode node) {
        if (node == null)
            return;

        for (int i = 0; i < 26; i++) {
            if (node.children.get(i) != null) {
                deleteNode(node.children.get(i));
                node.children.set(i, null);
            }
        }
    }


    class TrieNode {

        List<TrieNode> children;
        boolean validWord;

        TrieNode() {
            children = new ArrayList<>(26);
            for (int i = 0; i < 26; i++)
                children.add(null);
            
            validWord = false;
        }
    }

}