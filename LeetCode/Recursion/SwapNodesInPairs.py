#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Time O(N)-we need to make the swap for all nodes
# Space O(N)-the amount of space taken on the call stack since this is a recursive function with N nodes being swapped. 
#    First, we swap the first two nodes in the list, i.e. head and head.next;
#    Then, we call the function self as swap(head.next.next) to swap the rest of the list following the first two nodes.
#    Finally, we attach the returned head of the sub-list in step (2) with the two nodes swapped in step (1) to form a new linked list.

class Solution:
    def swapPairs(self, head: [ListNode]) -> [ListNode]:
        # If the list has no node or has only one node left. base case 
        if not head or not head.next:
            return head
        # create references to the two nodes we swap
        cur = head
        succ = head.next 
        
        # first assign cur.next and call the recusive function, we do this while we still have the reference to the other nodes 
        cur.next=self.swapPairs(succ.next)
        # then assign succ.next to cur
        succ.next = cur
        # return the new head
        return succ