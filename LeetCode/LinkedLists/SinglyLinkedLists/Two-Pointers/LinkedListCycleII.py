# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# Time O(n) + O(n) => O(n) - no nested loops but we will loop through the linked list twice
# Space O(1) - we dont use extra space 
# Two pointer practice, Floyds Tortoise and Hare algorithm:
# we create the slow and fast pointers 
# first loop
# if fast and slow meet break out of the first loop - there is a cycle
# if fast reaches the end then there is no cycle
# reset the fast pointer to the beginning of the list
# second loop fast and slow pointers move at same pace
# fast and slow will eventually meet at entrance of cycle
# return either pointer
class Solution:
    def detectCycle(self, head: [ListNode]) -> [ListNode]:
        slow = fast = head # initialize the pointers
        
        while fast and fast.next: # check for a cycle using the standard two pointer technique
            slow = slow.next
            fast = fast.next.next
            
            if fast == slow:
                break

        if not fast or not fast.next: # check if there is no cycle 
            return None
        
        fast = head # there is a cycle reset the fast pointer! 
        
        while fast != slow: # use this condition because we know that there is a cycle, we are waiting for the fast pointer to reach the entrance of the cycle 
            slow = slow.next
            fast = fast.next
        
        return fast
sol = Solution()
# Create nodes
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

# Link them linearly
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node1 # create the cycle

head = node1 # head of the list

print(sol.detectCycle(head).val)