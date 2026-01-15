# Time O(n) - we only visit each node once
# Space O(n) - we use n space for the stack 
# Algorithm:
# we will use a stack to keep track of the nodes to visit
# use an output list to store the visited node values
# use a pointer to keep track of the current node
# iterate on current node until it points to None or on the stack until it is empty
# iterate on the current node until the pointer points to None
# add the current node to the stack
# move the pointer to the left subtree 
# after itertation remove the node on top of the stack and assign it to the current pointer
# add the current pointers node value to output list
# then move the current pointer to the right node
# return the output list

from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class IterativeSolution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            output.append(curr.val)
            curr = curr.right
        return output

# Time: O(n) - where n is the number of nodes in the tree 
# Space O(n) - we perform a recursive call on every node within the tree, which uses n space on the call stack
# Algorithm: 
# use a helper function that takes the current node and output list
# first we perform a null check on the current node
# then we perform a recursive call on the left node and output list
# afterwards we can add the current node's value to the output list (we always need an action outside of the recursive calls to move us closer to the answer)
# finally we perform a recursive call on the right node and output list

# in the inorderTraversal call:
# we initialize an output list 
# call the helper function on the root node and output list 
# finally return the output list 

# Note: There is no explicit stack used here instead the call stack is used

class RecursiveSolution:
    def DFS(self, node, output):
        if node is None:
            return None
        
        self.DFS(node.left,output)
        output.append(node.val)
        self.DFS(node.right,output)
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        self.DFS(root,output)
        return output
