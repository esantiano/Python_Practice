
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
# Time O(N+M) where N is the number of nodes and M is the number of edges
# Space O(N) we need N space on the call stack and to store the clones in the map

# Algorithm: 
# if the node is none then return none
# create a clone node of the current node
# if the current node contains neighbors then we will process them using the DFS 
# we will need to use a map for the nodes we have processed, we will map the original node back to its clone and return it if it is encountered 
# return the cloned node
from typing import Optional
class Solution:
    def DFS(self, node, nodemap):
        if not node:
            return node
        if node in nodemap:
            return nodemap[node]
        clone = Node(node.val,[])
        nodemap[node] = clone
        if node.neighbors:
            clone.neighbors = [self.DFS(neighbor,nodemap) for neighbor in node.neighbors]
        return clone
    
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        nodemap = {}
        return self.DFS(node,nodemap)