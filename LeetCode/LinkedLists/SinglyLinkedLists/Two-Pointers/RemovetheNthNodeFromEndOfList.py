# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# A dummy node is used here to offset moving the pointers and to maintain a pointer at the head of the list, this stategy accounts for lists that are only one node long
class Solution:
    def removeNthFromEnd(self, head: [ListNode], n: int) -> [ListNode]:
        # we need a dummy node to point to the head of the list 
        dummy = ListNode(0)
        dummy.next = head
        # we point two pointers at dummy, this is done in case there is only one node in the list 
        cur = delay = dummy 
        # we'll move cur n nodes
        for i in range(n+1): #inclusive n
            cur = cur.next
        # Now we move our cur and delay pointer until cur is None
        while cur!=None:
            cur = cur.next
            delay = delay.next 
        # we can assign delays next node to the node after the next node
        delay.next = delay.next.next 
        return dummy.next # since the dummy node is pointing to the head of the list 
        
def print_list_nodes(head: ListNode):
    """Helper function to print all values in a linked list."""
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

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

resulting_head_1 = sol.removeNthFromEnd(node1, 2)
print_list_nodes(resulting_head_1)
# Expected output: 3 -> 2 -> 0 -> 5 -> None

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

resulting_head_2 = sol.removeNthFromEnd(node1, 1)
print_list_nodes(resulting_head_2)
# Expected output: 3 -> 2 -> 0 -> None