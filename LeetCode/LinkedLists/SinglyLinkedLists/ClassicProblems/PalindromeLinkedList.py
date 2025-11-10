# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# base case: [1] true 
# case: [1,3,3,1,3,3,1] true odd numbered lists could be true, even numbered lists could be true
# case: [1,2] false
# Time O(N) - multiple passes but once through for every loop
# Space O(1) - in place reversal and comparison
class Solution:
    def isPalindrome(self, head: [ListNode]) -> bool:
        # count the number of nodes, we need to know if its odd or even
        # get a pointer to middle of list 
        # reverse the first half of the list
        # compare the two halves of the list using pointers at the beg and middle
        
        if not head.next:
            return True
        
        mid = head
        count = 0
        while mid:
            mid = mid.next
            count+=1
        
        i = 0 
        mid = head 
        while i < count//2:
            mid = mid.next
            i+=1
        
        prev = None
        cur = head
        while cur != mid:
            nextTemp = cur.next  # keep the reference to the node next to current
            cur.next = prev # reverse the nodes 
            
            prev = cur # move prev, should always be the node at the beginning of the ll
            cur = nextTemp # move current 
        
        if count%2 != 0: # skip the middle node if the list is odd
            mid = mid.next
            
        cur = prev
        while mid:
            if cur.val != mid.val:
                return False
            cur = cur.next
            mid = mid.next
        return True
sol = Solution()
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(3)
node5 = ListNode(3)
node6 = ListNode(2)
node7 = ListNode(1)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7

print(sol.isPalindrome(node1))