# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        _cur = head
        _prev = None
        
        while _cur:
            _next = _cur.next
            _cur.next = _prev 
            _prev = _cur
            _cur = _next 
            
        return _prev
    
    class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (not head) or (not head.next): # null check
            return head
        
        current = self.reverseList(head.next) # recursive call 
        head.next.next = head # point the next node references next node to the current node
        head.next = None # assign the starting nodes next reference to None
        return current