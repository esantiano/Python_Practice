# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Time O(n) - we only go through the list once 
# Space O(1) - no extra space is used 
# Solution: we use two pointers, one for odd nodes and one for evens
# we also use a pointer to keep a reference to the even node chain since the algorithm causes a chain break
class Solution:
    def oddEvenList(self, head:[ListNode]) -> [ListNode]:
        if not head:
            return None
        
        odd = head # set odd at first node
        even = head.next # set even at second node
        evenHead = even # create reference to even
        while even and even.next: # we need to go until we reach None
            odd.next = even.next  # reassignment, this will skip over the even node and cause a chain break
            odd = odd.next # move odd pointer 
            even.next = odd.next # reassignment - this causes a chain break as well
            even = even.next # move the even pointer - its inside a new chain
        odd.next = evenHead # since two chains were created odd and even we need to reattach them 
        return head
def print_list_nodes(head: ListNode):
    """Helper function to print all values in a linked list."""
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")
sol = Solution()
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


print_list_nodes(sol.oddEvenList(node1))

# Run through 
# odd = 1
# even = 2
# even_head = 2

# List: 1 → 2 → 3 → 4 → 5
# Pointers:
# odd → 1
# even → 2

# Iteration 1
# Step 1: Link odd node (1) to next odd (3)
# odd.next = even.next   → 1 → 3

# Step 2: Move odd pointer forward
# odd = odd.next         → odd → 3

# Step 3: Link even node (2) to next even (4)
# even.next = odd.next   → 2 → 4

# Step 4: Move even pointer forward
# even = even.next       → even → 4

# State after iteration 1:
# Odd list: 1 → 3
# Even list: 2 → 4
# Remaining nodes: 5
# odd → 3, even → 4

# iteration 2
# Step 1: Link odd node (3) to next odd (5)
# odd.next = even.next   → 3 → 5

# Step 2: Move odd pointer forward
# odd = odd.next         → odd → 5

# Step 3: Link even node (4) to next even (None)
# even.next = odd.next   → 4 → None

# Step 4: Move even pointer forward
# even = even.next       → even → None

# State after iteration 2:
# Odd list: 1 → 3 → 5
# Even list: 2 → 4
# odd → 5, even → None

# Final 
# After loop ends (even == None), connect last odd node (5) to even_head (2)
# odd.next = even_head

# Final list:
# 1 → 3 → 5 → 2 → 4 → None
