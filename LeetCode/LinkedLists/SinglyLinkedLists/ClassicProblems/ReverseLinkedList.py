# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Time O(n) - we only loop through the list once
# Space O(1) - this is done in place 
# Edge case: empty list 
# we need to use the head pointer which is given to us as a variable 
# we use two additional pointers: first pointer curHead keeps a reference to the current head node
# second pointer p keeps a reference to the next upcoming node is created within the loop
# we need to keep a reference to the next node after p, we will have the head pointer point to this node
# after we have established our references and their order we can begin swapping 
# p's next node will be swapped with the curHead node 
# then we can move curHead to p which is the new head node 
class Solution:
    def reverseList(self, head: [ListNode]) -> [ListNode]:
        if head is None:
            return None
        curHead = head
        while head.next != None:
            p = head.next
            head.next = p.next
            p.next = curHead
            curHead = p
        while curHead != None:
            print(curHead.val, end=" -> ")
            curHead = curHead.next
        return curHead
# --- Example Usage ---
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

sol = Solution()
sol.reverseList(node1)