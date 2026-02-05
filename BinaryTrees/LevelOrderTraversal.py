# Time: O(N) we require O(N) time to process all nodes in the tree 
# Space: O(N) we use either an explicit queue or an implicit stack to process all nodes in the tree
from typing import Optional, List
from collections import deque
from TreeNode import TreeNode

class Solution:
    # Algorithm:
    # Here we use a queue to process all nodes within a level.
    # Starting at the root we gather the size of the queue as well as initialize a new list to store all values at the current level.
    # We take the ndoe from the beginning of the queue and add them to the new list, then check for left or right subtrees and add them to the queue.
    # the added subtrees are not counted for processing at the current level. 
    # once we have cleared the queue for the current level we add the new list (now full of all values at the current level) to the result
    # repeat until we have emptied the queue (and processed all the nodes in the tree)
    def levelOrderIterative(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        q.append(root)
        result = []
        while q and q[-1]:
            cur_list = []
            cur_q = len(q)
            for i in range(cur_q):
                cur = q.popleft()
                cur_list.append(cur.val)
                if cur.left is not None:
                    q.append(cur.left)
                if cur.right is not None:
                    q.append(cur.right)
        result.append(cur_list)
        return result
    # Algorithm:
    # For the recursive solution we use a helper function to create the level list for the current level.
    # The function will use the current node and the level the node is located at.
    # Start with a base case null check.
    # A new list is created for the current level if the size of the resulting list
    # matches the current level. The result will look like lists within a list.
    # We then add the node to its indexed list within the result. 
    # Finally we check for left and right subtrees and recursively call the function on 
    # those nodes as well as the level those nodes are located. The level moves down one or increments.
    # We start the recursion at the root node at level 0.
    def levelOrderRecursive(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        def addList(node, level):
            if root is None:
                return
            if level == len(result):
                result.append([])
            result[level].append(node.val)
            if node.left:
                addList(node.left,level+1)
            if node.right:
                addList(node.right,level+1)
        addList(root,0)
        return result