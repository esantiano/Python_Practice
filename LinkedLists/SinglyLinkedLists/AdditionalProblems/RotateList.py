# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# we only need to rotate the list k%n  times 
# get the number of nodes - n
# since the list is already partially in order we just need to determine the new head and tail
# move a pointer within the orginal list n-k%n-1 times to place us at the new tail node of the output list
# the new head will be the next node after the new tail
# break the link in the circular list and return the new head

# edge case: k == n or k ==1: return the original list
# edge case: n == 0: return None
class Solution:
    def rotateRight(self, head: [ListNode], k: int) -> [ListNode]:
        if not head: # no nodes
            return None
        elif not head.next: # single node
            return head
        
        # get number of nodes n
        cur = head
        n = 1
        while cur.next:
            cur = cur.next
            n+=1
        cur.next = head # creates a circular linked list
        
        if k == n: # no rotations, break the circular reference and return head
            cur.next = None 
            return head
        
        # reset cur
        new_tail = head

        for _ in range(n-(k%n)-1): # travel to new tail
            new_tail = new_tail.next
        
        new_head = new_tail.next # since we are at the tail we can assign the new head 
        new_tail.next = None # break the circular reference from the tail
        
        return new_head

def print_list_nodes(head: ListNode):

    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

node0 = ListNode(0)
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node0.next = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = None

sol = Solution()
print_list_nodes(sol.rotateRight(node0,2))