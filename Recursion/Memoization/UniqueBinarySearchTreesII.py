# Note, the time and space complexity of this problem is difficult to derive. 

# The complexity is:
# Time = O(n · Cₙ) Cₙ = (1/(n+1)) * (2n choose n)   (the nth Catalan number)
# Space: O(n · Cₙ)
# 1. Height of recursion: O(n)
# This is because at most we recursively split the interval [1..n] down until start > end.
# 2. Space for all constructed trees
# You build Cₙ trees, each with n nodes, so:
# Output space = O(n · Cₙ)
# (You need to store all generated trees in memory.)

# Algorithm:
# Here we use a helper function to generate all the possible binary search trees for a given range of numbers 
# we use a map to remember trees for a given range of numbers to avoid repeated calculations
# we iterate through the range of numbers and create the all possibilities for left and right subtrees for a given root 
# we create the possible subtree for the given range and then add it to a list
# add the list to the map for the given range 
# finally we return the resulting list of subtrees 

# note on when the iteration and recursion stops: Eventually one of these happens:
# start == end → single-node tree (1 valid root)
# start > end → empty tree ([None] returned)

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> list[Optional[TreeNode]]:
        memo = {}
        def allPossibleBST(start,end,memo):
            res = []
            if start > end:
                res.append(None)
                return res
            
            if (start,end) in memo:
                return memo[(start,end)]

            for i in range(start,end+1):
                leftSubtrees = allPossibleBST(start,i-1,memo)
                rightSubtrees = allPossibleBST(i+1,end,memo)
                
                for left in leftSubtrees:
                    for right in rightSubtrees:
                        root = TreeNode(i,left,right)
                        res.append(root)
                memo[(start,end)] = res
            return res
        return allPossibleBST(1,n,memo)