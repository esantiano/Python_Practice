# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        _maxDiameter = 0 
        def DFS(root):
            nonlocal _maxDiameter 
            if not root:
                return 0 
            left = DFS(root.left)
            right = DFS(root.right)
            _maxDiameter = max(_maxDiameter,left+right)
            return 1 + max(left, right)
        DFS(root)
        return _maxDiameter