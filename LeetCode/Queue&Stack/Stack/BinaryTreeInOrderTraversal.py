# Time O(n) - we only visit each node once
# Space O(n) - we use n space for the stack 
# Algorithm:
# we'll also use a list to keep track of the values 
# use a stack to determine the order of the nodes to add to lilst
# we'll assign a pointer to the root node 
# iterate through the current node and stack  -> first loop begin iterating through the tree
# iterate through the current node -> second loop we move left until we can't move left
# add the pointers node to the stack and move the pointer left
# once we finish adding all the left subtrees to the stack then we start removing from the stack
# move the pointer to the top node on the stack
# add the current pointers value to the list
# move the pointer right
# return the lis

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
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