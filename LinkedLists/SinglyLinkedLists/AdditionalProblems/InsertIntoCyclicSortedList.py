
# Definition for a Node.
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

# Time O(n) - go through each node once 
# Space 0(1) - no additional space is used 
# edge cases: no nodes, single node, all nodes have same value, insertVal is at beginning or end of list-> insert into start but how do we check?
# question: how do we know if a list has a single node? 
# ans check if the node points to itself using is
class Solution:
    def insert(self, head: [ListNode], insertVal: int) -> 'ListNode':
        new = ListNode(insertVal)
        if head is None: # case: head is null
            new.next = new
            return new 
        
        prev, cur = head, head.next
        toInsert = False
        
        while True:
            if prev.val <= new.val <= cur.val:# case insertion point is prev.val<=insertVal<=cur.val
                toInsert = True 
            elif prev.val > cur.val:# case val to insert is greater or less than max/min values in list
                if prev.val <= new.val or new.val <= cur.val:
                    toInsert = True 
            
            if toInsert: # insert the insertVal between prev and cur or end/beginning
                prev.next = new
                new.next = cur
                return head
                
            prev = cur
            cur = cur.next 
            if prev == head: # we've seen all nodes in the list and they're either all the same value or one single node
                break

        # case: single node in head or all nodes in list have same value 
        prev.next = new
        new.next = cur
        return head
    
def print_list_nodes(head: ListNode):

    current = head
    while True:
        print(current.val, end=" -> ")
        current = current.next
        if current == head:
            break
    print("(back to head)")

sol = Solution()
# Create nodes
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(6)

# Link them linearly
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node1  # close the loop

head = node1 # head of the list

print_list_nodes(sol.insert(head,5))