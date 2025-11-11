
# Definition for a Node.
class Node:
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
# Time O(n) - we will go though the list once
# Space O(n) - we use a stack and at worst the stack will be the size of the list itself 
# Algorithm - we use a stack to place the nodes, stack is filo, first the next nodes are added and then the child nodes
# the child nodes are handled first 
# we must also sever the first real nodes connection to the reference node 
class Solution:
    def flatten(self, head: [Node]) -> [Node]:
        # edge case check , no head return None
        # use output node to store values from list 
        # use cur pointer to travel through each level
        # use a stack to go through the nodes and check them 
        # run a loop while there are nodes in the stack
        # remove the node on top of the stack
        # add node from top to output 
        # if there is a next node then add it to stack 
        # if current node has child add it to stack and set current node child to none
        # repeat 
        # return output
        if not head:
            return None
        
        output = Node(0,None,head,None)
        out = output
        stack = [head]
        
        while stack:
            cur = stack.pop()
            out.next = cur
            cur.prev = out
            
            # check for next node
            if cur.next:
                stack.append(cur.next)
            # check for children 
            if cur.child:
                stack.append(cur.child)
                cur.child = None
            # move the pointer for the output list
            out = cur
        output.next.prev = None # sever the output node, first real node does not point back to output 
        return output.next
def print_list_nodes(head: Node):

    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

n1 = Node(1); n2 = Node(2); n3 = Node(3); n4 = Node(4); n5 = Node(5); n6 = Node(6)
n1.next=n2; n2.prev=n1
n2.next=n3; n3.prev=n2
n3.next=n4; n4.prev=n3
n4.next=n5; n5.prev=n4
n5.next=n6; n6.prev=n5

# level 1 (child of 3)
n7 = Node(7); n8 = Node(8); n9 = Node(9); n10 = Node(10)
n7.next=n8; n8.prev=n7
n8.next=n9; n9.prev=n8
n9.next=n10; n10.prev=n9
n3.child = n7

# level 2 (child of 8)
n11 = Node(11); n12 = Node(12)
n11.next=n12; n12.prev=n11
n8.child = n11

sol = Solution()
print_list_nodes(sol.flatten(n1))