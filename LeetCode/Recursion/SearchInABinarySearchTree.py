# Best case:
# Time O(logN) - here we use master theorem to detemine the average time complexity. O(N) is the worst case
# Space: O(logN) - Space taken on the call stack, O(N) also being the worst case 


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Algorithm:
# base case check root is none
# assign vars to left and right nodes call search BST on left and right nodes
# check left and right for T/F, return T nodes
# compare the node value against val return the node if they match 
class Solution:
    def searchBST(self, root: [TreeNode], val: int) -> [TreeNode]:
        if not root:
            return None
         
        left = self.searchBST(root.left,val)
        right = self.searchBST(root.right,val)
        
        if left:
            return left
        if right:
            return right
        if root.val == val:
            return root
# The algorithm above uses O(N) since it checks all the the nodes in the BST 
# It can be simplified: we have two cases where we return the root 
# we can also reduce the checks and calls on the left and right nodes since BST's are structured
# so that values greater/less than the root value are organized on the right/left nodes
    def searchBSTOptimized(self, root: [TreeNode], val: int) -> [TreeNode]:
        if not root or root.val == val:
            return root
        if val < root.val:
            return self.searchBSTOptimized(root.left,val)
        else:
            return self.searchBSTOptimized(root.right,val)
        

