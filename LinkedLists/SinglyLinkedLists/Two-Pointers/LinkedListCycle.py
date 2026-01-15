# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Time O(n) - we will be traveling the linked list at least once
# Space O(1) - no space is used 
class Solution:
    def hasCycle(self, head: [ListNode]) -> bool:
        
        # initiate slow and fast pointers
        slow = fast = head
        i = 0 
        while fast and fast.next: # we continue on the condition that fast is not None and fast.next is not None 
            slow = slow.next # move the pointers first 
            fast = fast.next.next
            i +=1 
            if slow == fast: # then check to see if they are pointing at the same node 
                print(slow.val, fast.val,i)
                return True
        return False

sol = Solution()
# Create nodes
node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(4)
node5 = ListNode(5)

# Link them linearly
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2
node5.next = node3 # create the cycle

head = node1 # head of the list

print(sol.hasCycle(head))