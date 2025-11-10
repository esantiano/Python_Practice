# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Time O(n) - at worst we go through each list once
# Space O(1) - We only use space for the output
class Solution:
    def mergeTwoLists(self, list1: [ListNode], list2: [ListNode]) -> [ListNode]:
        # create a reference node to return later
        # create a pointer for both lists 
        # compare the values of the pointers nodes
        # attach the smaller value node to the output node
        # move the pointer for that list 
        # if we run out of nodes for one list attach the rest of the other list to the output node
        output = ListNode()
        
        cur = output
        
        p1 = list1
        p2 = list2
        
        while p1 and p2:
            if p1.val <= p2.val:
                cur.next = p1
                cur = cur.next
                p1 = p1.next
            else:
                cur.next = p2
                cur = cur.next
                p2 = p2.next
        
        if p1:
            cur.next = p1
        elif p2:
            cur.next = p2
        
        return output.next
def print_list_nodes(head: ListNode):

    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")
# Example Linked List 1: list1 = [1, 2, 4]
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

# Example Linked List 2: list2 = [1, 3, 4]
list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

sol = Solution()
print_list_nodes(sol.mergeTwoLists(list1,list2))
