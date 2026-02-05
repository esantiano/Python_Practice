# Time: O(N) we potentially check each node in the tree for all solutions.
# Space: O(N) at worst we use this amount of space to process each node in the tree.
from typing import Optional
from TreeNode import TreeNode
class Solution:
# Algorithm: 
# For this algorithm we build a list of both subtrees and compare the lists. 
# We define a recursive function to build each subtree and call the function on the left and right subtrees.
# We use nonlocal lists to store values from the nodes in each subtree. 
    def isSymmetricOwn(self, root: Optional[TreeNode]) -> bool:
        left_subtree = []
        right_subtree = []
        def buildSubTree(node,subtree,left):
            if node is None:
                subtree.append(None)
                return None
            subtree.append(node.val)
            if left:
                buildSubTree(node.right,subtree,left)
                buildSubTree(node.left,subtree,left)
            else:
                buildSubTree(node.left,subtree,left)
                buildSubTree(node.right,subtree,left)

        buildSubTree(root.left,left_subtree,True)
        buildSubTree(root.right,right_subtree,False)

        return left_subtree==right_subtree
# Algorithm: 
# This approach uses a recursive function to compare nodes from each subtree.
# Rather than go through all the nodes we exit the function as soon as we find non matching nodes.
    def isSymmetricRecursive(self, root: Optional[TreeNode]) -> bool:
        def checkSymmetry(node1, node2):
            # establish base cases 
            # None, not matching
            if node1 is None and node2 is None:
                return True
            if node1 is None or node2 is None or node1.val != node2.val:
                return False
            
            # compare the node values and recurse on left and right nodes.
            return (
            node1.val == node2.val 
            and checkSymmetry(node1.left,node2.right)
            and checkSymmetry(node1.right,node2.left)
            )
        return checkSymmetry(root.right,root.left)
# Algorithm: 
# This solution iteratively compares each node.
# Using a stack we start by comparing the left and right subtrees.
# We remove and add sets of nodes to the stack to compare and continue until we hit a false condition or we have compared all nodes in each subtree.
    def isSymmetricIterative(self, root: Optional[TreeNode]) -> bool:
        nxt = [(root.left, root.right)] # using a set is easier to understand which nodes we are comparing
        while nxt:
            n1, n2 = nxt.pop() 
            if not n1 and not n2: # this check is introduced because we are not checking for nodes of null value, so they may be placed on the processing stack.
                continue
            if not n1 or not n2 or n1.val != n2.val:
                return False
            nxt.append((n2.right,n1.left))
            nxt.append((n2.left,n1.right))
        return True