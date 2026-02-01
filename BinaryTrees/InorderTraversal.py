# Time: O(N) we use this time to travel to each node in the tree
# Space: O(N) we use space for an explicit or implicit stack
# Notes: Inorder traversal: left node -> root node -> right node
from typing import List, Optional
from TreeNode import TreeNode
class Solution:
    # Algorithm: 
    #   In this version we iterate through the tree.
    #   We use an explicit stack to determine which nodes to process.
    #   For inorder traversal: starting at the root node and iteratively place subtrees on top of the stack.
    #   We continue placing all left subtrees into the stack 
    #   Once all left subtrees are on the stack we can start processing nodes from the stack.
    #   For each subtree we process we place the value of the node in the result and then traverse to the right subtree and repeat placing subtrees on the stack.
    #   We repeat the above process until all nodes in the tree have been processed.
    def inorderTraversalIterative(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        cur = root
        nxt = []
        while cur or nxt:
            while cur:
                nxt.append(cur)
                cur = cur.left
            cur = nxt.pop()
            result.append(cur.val)
            cur = cur.right
        return result
    # Algorithm: 
    #   For this version we recursively process nodes on the tree.
    #   We use a helper function to add nodes into a list as well as traverse subtrees.
    #   We start the function with a none check.
    #   Then we recursively call the function on the left subtree.
    #   Next add the value and finally recursively call the function on the right subtree.
    def inorderTraversalRecursive(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def addNode(node):
            if not node:
                return None
            addNode(node.left)
            result.append(node.val)
            addNode(node.right)
        addNode(root)
        return result