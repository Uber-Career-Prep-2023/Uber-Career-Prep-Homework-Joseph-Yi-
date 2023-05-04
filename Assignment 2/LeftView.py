#   Space complexity is O(n)
#   there is a queue and you may possibly need to queue every single node in the tree

#   Time complexity is O(n)
#   you must check every node during the level order traversal

#   this problem took me 18 min

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def left_view(root):
    if not root:
        return []

    result = []
    queue = [root]

    # perform level order traversal
    while queue:
        levels = len(queue)

        for i in range(levels):

            node = queue.pop(0)

            # checks that it is the left most node
            if i == 0:
                result.append(node.val)

            # adds left and right ot the queue
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return result
