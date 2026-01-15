# Definition for singly-linked list.
# Time: O(m+n) - worst case is we recurse through every node in each list
# Space: O(m+n) - the amount of space we take on the recursion stack and through the output list

# Algorithm: 
# we use a dummy node pointing to the output list and a pointer to assign the nodes to the output list
# first we check our base cases: both lists have reached the end or one list or the other reaches its end, 
# then we compare the values of the nodes, assign the next node, move the output list pointer and assign the pointer to the recursive function call
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        output = ListNode(0)
        out = output
        def merge(list1,list2,out):
            print(f'list1:{list1},list2:{list2}')
            if not list1 and not list2:
                return None
            if not list1:
                out.next = list2
                return list2
            if not list2:
                out.next = list1
                return list1 
            
            if list1.val <= list2.val:
                out.next = list1
                out = out.next
                out = merge(list1.next,list2,out)
            else:
                out.next = list2
                out = out.next
                out = merge(list1,list2.next,out)
                
        merge(list1,list2,out)
        return output.next
# The algorithm above can be simplified, we don't have to use a dummy node or extra space for the output
# we perform our base case checks first and return the non null list
# then we compare the values of the current nodes, recursively assign the next value for that head to the next merge result and return the set head
    def mergeTwoListsOptimized(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1 
        
        if list1.val <= list2.val:
            list1.next = self.mergeTwoListsOptimized(list1.next,list2)
            return list1
        else:
            list2.next = self.mergeTwoListsOptimized(list1,list2.next)
            return list2
# example :
# l1->1->2->3    l2->1->3->4
# recursive call: (1,1) -> (1,3) -> (2,3) -> (3,3) -> (3,4) -> (None,4) 
# result:           1 -> 1 -> 2 -> 3 -> 3 -> 4 -> None       