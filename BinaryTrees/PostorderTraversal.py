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
    # This agorithm results in a reversed postorder list: N -> R -> L
    # in order to obtain the correct order we have to reverse the list once all nodes have been processed.
    # we place the root value in the result list first,
    # then place the root node in the stack of nodes to process, we do this to be able to process the nodes left subtree
    # then move right to the right subtree, 
    # once we finish processing the right subtree we can process the left subtree 
    # repeat above until we have processed all nodes in the tree 
    def postorderTraversalIterative2(self, root):
        result = []
        nxt = []
        cur = root

        while cur or nxt:
            if cur:
                result.append(cur.val) # -> N 
                nxt.append(cur) # nxt = [N{L,R}]
                cur = cur.right # N -> R
            else:
                cur = nxt.pop() # N 
                cur = cur.left # N -> R -> L
        result.reverse()
        return result