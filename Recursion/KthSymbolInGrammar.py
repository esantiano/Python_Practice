# Time O(n) - we reduce the number of recursive calls until n becomes 1, which will overall result in n
# Space O(n) - the number of calls on the call stack will be n as well, until it is reduced to 1 

# Explanation 
# We can treat this problem like a binary tree data structure
# for each level besides the first level we need to determine which side the node could be on 
# this will reduce the number of recursive calls we need to make since we cut the number of possibilities in half with each call 
# Each node value will either be 1 or 0 
# for each level n, there are 2^n-1 nodes 
# the recurrence relation is based on n, since the further up we go the less choices we have 
# based on k we choose the left side or right side of the tree 


# Algorithm: 
# base case is n=1 since the first level is just 0 or the root nodes value 
# determine which subtree k is inside 
# determine what the next root value is 

# how do we modify k to determine which side we are on after choosing? 
# if the given k is greater than half the number of nodes on the given level then we can eliminate the left half of the nodes 
# if k isnt then we leave it alone 

# how do we determine the next root value? 
# if k is greater than half the number of nodes then choose the right
# since for a given node the pattern is currentNodeValue->0->0,1 currentNodeValue->1->1,0 the current root node helps us figure out the next nodes possible value 


class Solution:
    def dFS(self,n,k,rootVal):
        if n == 1:
            return rootVal
        
        totalNumNodes = 2**(n-1) # 
        halfNumNodes = totalNumNodes/2
        
        if k > halfNumNodes:
            k = k - halfNumNodes # k only needs to be updated if its in the right half of the subtree since the left half will be discarded 
            nextRootVal = 1 if rootVal == 0 else 0 # here we update the nextRootValue since we can determine which it could be based on k and the current root val 
            return self.dFS(n-1,k,nextRootVal) 
        else: # k is in the left half of the tree 
            nextRootVal = 0 if rootVal == 0 else 1
            return self.dFS(n-1,k,nextRootVal)
        
    def kthGrammar(self, n: int, k: int) -> int:
        return self.dFS(n,k,0)