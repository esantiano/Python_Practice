# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Time O(N) - only going through list once
# Space O(1) - in place removals 
# Edge cases: empty list, nodes to remove are at beginning and end of list, all elements in list are val, only element in list is val
# we need the sentintel node to keep track of the overall list
# we use two pointers to keep track of the previous and current ndoes
# in case the current nodes val is equal to the val we want to remove we have a reference to the previous node 
# if it isn't then we move the previous node along with the current node
# the current node will always move 
class Solution:
    def removeElements(self, head: [ListNode], val: int) -> [ListNode]:
        if head is None: 
            return None
        sentinel = ListNode(0)
        sentinel.next = head
        prev = cur = sentinel
        while cur: # cur will evenutally be None
            if cur.val == val:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next
        return sentinel.next
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
node4 = ListNode(6)
node5 = ListNode(4)
node6 = ListNode(5)
node7 = ListNode(6)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7

print_list_nodes(sol.removeElements(node1,6))

# start
#      p
# s -> 0 -> 1 -> 2 -> 3 -> 6 -> 4 -> 5 -> 6 -> None
#      c

#      p
# s -> 0 -> 1 -> 2 -> 3 -> 6 -> 4 -> 5 -> 6 -> None
#           c

#           p
# s -> 0 -> 1 -> 2 -> 3 -> 6 -> 4 -> 5 -> 6 -> None
#                c

#                p
# s -> 0 -> 1 -> 2 -> 3 -> 6 -> 4 -> 5 -> 6 -> None
#                     c

#                     p
# s -> 0 -> 1 -> 2 -> 3 -> 6 -> 4 -> 5 -> 6 -> None
#                          c   c.n

#                     p
# s -> 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None
#                          c

#                          p
# s -> 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None
#                               c

#                               p
# s -> 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None
#                                    c    c.n

# end 
#                               p
# s -> 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> None
#                                     c
