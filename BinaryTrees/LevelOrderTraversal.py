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
    # In the recursive method we must use a helper function to add lists of different levels to the result.
    # Starting at the root node at level 0.
    # The helper function takes in the current node and the level which the node is located. 
    # We initialize the list that the node value will be placed in by comparing the size of the current list to the level (now we have an indexed list we can place the node values into)
    # place the node value into its correctly indexed list and then check for subtrees 
    # to handle the subtrees we recursively call the function on the left and right subtrees as well as increment the level they are located. 
    def levelOrderRecursive(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if root is None:
            return result
        def addList(node, level):
            if level == len(result):
                result.append([])
            
            result[level].append(node.val)
            if node.left:
                addList(node.left,level+1)
            if node.right:
                addList(node.right,level+1)
        addList(root,0)
        return result