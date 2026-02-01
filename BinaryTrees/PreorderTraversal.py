# Time: O(N) time used to traverse root with N nodes, in each case.
# Space: O(N) each solution uses extra space at most N with either an explicit or implicit call stack.
# Notes: Preorder traversal happens in the order: root, left, right
from typing import List, Optional
from TreeNode import TreeNode
class Solution:
    # Algorithm:
    # In this solution we use an explicit call stack to iteratively traverse the tree.
    # Stacks are LiFo so we want to place the right node in the stack first then the left.
    # when we remove from the stack we take the left node first.
    def preorderTraversalIterative(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        nxt = []
        nxt.append(root)
        while nxt and nxt[-1]:
            cur = nxt.pop()
            result.append(cur.val)
            if cur.right is not None:
                nxt.append(cur.right)
            if cur.left is not None:
                nxt.append(cur.left)
        return result
    # Algorithm:
    # In this solution we use an implicit call stack to recursively traverse the tree.
    # We use a helper function to add node values to our resulting list and traverse the tree.
    # In this case we can call recursively call the helper on the nodes in order of the preorder traversal.
    # We need to use an non local list to store the result of the traversal.
    def preorderTraversalRecursive(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def addNode(node):
            if node is None:
                return None
            result.append(node.val)
            addNode(node.left)
            addNode(node.right)
        addNode(root)
        return result