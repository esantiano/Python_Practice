# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Time: O(max(m,n)) - since both lists can be different lengths
# Space: 0(1) - we dont count the output as space used 
class Solution:
    def addTwoNumbers(self, l1: [ListNode], l2: [ListNode]) -> [ListNode]:
        # two pointers to go through each list 
        # use a variable carry to carry over numbers 
        # put the %10 of sum of nodes into output 
        # carry stores the sum//10 
        # store the result in an output list 
        p1 = l1
        p2 = l2 
        carry = 0
        output = ListNode(0)
        cur = output
        while p1 and p2: # the loops and if statements can be condensed into a single loop if we use conditional expressions to hold the values 
            node_sum = p1.val + p2.val + carry
            carry = node_sum//10
            p = node_sum%10
            cur.next = ListNode(p)
            cur = cur.next 
            p1 = p1.next
            p2 = p2.next
        
        if p1:
            while p1:
                node_sum = p1.val + carry
                carry = node_sum//10
                p = node_sum%10
                cur.next = ListNode(p)
                cur = cur.next
                p1 = p1.next
        elif l2:
            while p2:
                node_sum = p2.val + carry
                carry = node_sum//10
                p = node_sum%10
                cur.next = ListNode(p)
                cur = cur.next
                p2 = p2.next
        if carry:
            cur.next = ListNode(carry)
            cur = cur.next 
            carry = 0
        return output.next
            
    def addTwoNumbers2(self, l1: [ListNode], l2: [ListNode]) -> [ListNode]:
        dummyHead = ListNode(0)
        curr = dummyHead
        carry = 0
        while l1 != None or l2 != None or carry != 0:
            l1Val = l1.val if l1 else 0 # conditional expressions 
            l2Val = l2.val if l2 else 0
            columnSum = l1Val + l2Val + carry
            carry = columnSum // 10
            newNode = ListNode(columnSum % 10)
            curr.next = newNode
            curr = newNode
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummyHead.next
def print_list_nodes(head: ListNode):

    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

# Example Linked List 2: list2 = [1, 3, 4]
list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

sol = Solution()
print_list_nodes(sol.addTwoNumbers(list1,list2))
print_list_nodes(sol.addTwoNumbers2(list1,list2))