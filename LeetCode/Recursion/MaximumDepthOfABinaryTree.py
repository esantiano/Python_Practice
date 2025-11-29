# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# base case? the root is none so we return 0 
# recursive call on left and right nodes. We add 1 because the current node itself contributes to the depth of the tree.
# return the maximum between the left and right nodes
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        # adding one can occur here or at the return, both are accepted. 
        left = 1 + self.maxDepth(root.left)
        right = 1 + self.maxDepth(root.right)
        return max(left,right) # the return here is stylistic.
    # returning 1 + max(...) is more direct in saying "the depth is this"