# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0 
        _cur = head 
        while _cur: 
            _cur = _cur.next 
            count += 1 
        _cur = head 
        
        if count%2 == 0: 
            for i in range(int(count/2)):
                _cur = _cur.next
            return _cur
        
        for i in range(count//2): 
            _cur = _cur.next
        return _cur