# Time: O(N) each algorithm uses O(N) time to process each node in the tree
# Space: O(N) each algorithm uses either an implicit or explicit call stack
# Notes: Postorder processing: Left -> Right -> Root
from typing import Optional, List
from TreeNode import TreeNode
class Solution:
    # Algorithm:
    # In this approach we use a helper function to recursively process nodes.
    # We can follow postorder processing highlighted in the notes. 
    def postorderTraversalRecursive(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def addNode(node):
            if not node:
                return None
            addNode(node.left)
            addNode(node.right)
            result.append(node.val)
        addNode(root)
        return result
    # Algorithm:
    # For this iterative algorithm we can use a modified preorder iterative algorithm.
    # This will return a reversed postorder result.
    # We will have to reverse the result in order to obtain the true postorder node list.
    def postorderTraversalIterative(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        nxt = [root]
        while nxt and nxt[-1]:
            cur = nxt.pop()
            result.append(cur.val)
            if cur.left is not None:
                nxt.append(cur.left)
            if cur.right is not None:
                nxt.append(cur.right)
        result.reverse()
        return result
    # Algorithm:
    # Another modified version of preorder iterative algorithm.
    # If we have a valid node
    # we place the root value in the result list first,
    # then place the root node in the stack of nodes to process,
    # then move right to the right subtree. 
    # otherwise we remove the top node on the stack and move to the left subtree 
    # the resulting list is in reversed postorder.
    def postorderTraversalIterative2(self, root):
        result = []
        nxt = []
        cur = root

        while cur or nxt:
            if cur:
                result.append(cur.val)
                nxt.append(cur) # even though we have already added the node value to the result we place it in the stack to be able to revisit it and process its left subtree
                cur = cur.right # we continue on to the right subtree first 
            else: # here we have run into None so we go back to the root node and process the left subtree 
                cur = nxt.pop() 
                cur = cur.left
        result.reverse()
        return result