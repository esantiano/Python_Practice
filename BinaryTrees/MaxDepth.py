# Time O(N) where N is the number of nodes in the tree
#   Both iterative and recursive solutions require O(N) time to determine the depth of a tree.
#   Each solution requires every node in the tree to be processed.
# Space O(N) 
#   Both iterative and recursive solutions use N space on the call stack (explicit or implicit).
from typing import Optional
from TreeNode import TreeNode
class Solution:
# Algorithm:
# For iteration we manage the current node and its depth using sets.
# We process each node using a stack starting at the root node.
# We iterate through the tree unpacking the set on top of the stack.
# If we have a non null node we update the the depth.
# We also add children nodes onto the stack and update the depth for those nodes.
    def maxDepthIterative(self, root: Optional[TreeNode]) -> int:
        nxt = [(root,1)]
        depth = 0

        while nxt and nxt[-1]:
            cur,cur_depth = nxt.pop()
            if cur is not None:
                depth = max(depth, cur_depth)
                nxt.append((cur.left,cur_depth+1))
                nxt.append((cur.right,cur_depth+1))
        return depth
    
# Algorithm: 
# For recursive solutions I like using helper methods but its also possible to recursively call the method itself in this case.
# Each method below determines the depths of the left and right subtrees. 

# For the bottom up approach we calculate the depth in a postorder fashion, process L->R->N nodes and allowing the depth to bubble up from the base case.
    def maxDepthRecursiveBottomUp(self, root: Optional[TreeNode]) -> int:
        def getDepth(node):
            if node is None:
                return 0
            left_ans = getDepth(node.left)
            right_ans = getDepth(node.right)
            return max(left_ans, right_ans) + 1
        return getDepth(root)
# For the top down approach we calculate the depth by tracking its state in a preorder fashion, process N->R->L nodes while updating the depth.    
    def maxDepthRecursiveTopDown(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def getDepth(root,depth):
            if root is None:
                return 0
            self.ans = max(self.ans, depth)
            getDepth(root.left, depth+1)
            getDepth(root.right, depth+1)
        getDepth(root,1)
        return self.ans