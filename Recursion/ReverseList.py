# Time O(n) - we go through each node 
# Space O(n) - the call stack uses space and goes n levels deep
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: [ListNode]) -> [ListNode]:
        # base case where head and head.next are None, we return the head
        if head is None or head.next is None:
            return head
        # we do the recursive call at the beginning
        # we travel all the way to the last node before beginning the reassignments
        # the reassignments bubble up from the last node 
        p = self.reverseList(head.next)
        head.next.next = head  # reverse the nodes by assigning the successor nodes next to the previous node
        head.next = None # set the head nodes next to none 
        # return the result of the recursive call 
        return p
