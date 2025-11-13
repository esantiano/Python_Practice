class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = x
        self.next = next
        self.random = random
# Time O(N) - each node is visited once in 3 different loops
# SpaceO(1) - no extra space is used, we don't count the output as using extra space
# Algorithm: first we create copies of the original nodes, we also connect the copies into the original list
# next we create the random connections for the copied nodes 
# finally we disconnect the copy from the original list 
class Solution:
    def copyRandomList(self, head: [Node]) -> [Node]:
        if not head:# edge case: head is none
            return None
        
        # create a pointer to reference the copy 
        cO = head

        while cO:  # loop once to create copy of node and interweave the original and copy nodes 
            # create copy of original node + link copy
            prime = Node(cO.val, None, None)
            prime.next = cO.next
            # interweave original and copy
            cO.next = prime
            # move pointer to next in original list
            cO = cO.next.next 

        #reset the pointer
        cO = head
        
        while cO: # loop again to assign copies random pointers 
            prime = cO.next
            if cO.random is None:
                prime.random = None
            else:
                # assign copies random pointer
                prime.random = cO.random.next
            # move pointer to next in original list
            cO = cO.next.next 

        # reset cO and create a reference for copy
        cO, copy = head, head.next
        # pointer for copy
        cP = copy
        while cO: # loop last time to unweave copy and pointers 
            # separate copy and original
            cO.next = cO.next.next
            cP.next = cP.next.next if cP.next else None
            # move the pointers
            cP, cO = cP.next, cO.next
            
        return copy
    
def print_random_list(head: Node):
    """
    Print the linked list in the format:
    index: val=X, next=Y, random=Z
    """

    # Step 1: gather nodes in sequential order
    nodes = []
    cur = head
    while cur:
        nodes.append(cur)
        cur = cur.next

    # Step 2: map: node -> index
    index_map = {node: idx for idx, node in enumerate(nodes)}

    # Step 3: output node details
    for idx, node in enumerate(nodes):
        next_idx = index_map[node.next] if node.next else None
        rand_idx = index_map[node.random] if node.random else None
        print(f"Index {idx}: val={node.val}, next={next_idx}, random={rand_idx}")


node0 = Node(7)
node1 = Node(13)
node2 = Node(11)
node3 = Node(10)
node4 = Node(1)

# Step 2: link the .next pointers: 0 -> 1 -> 2 -> 3 -> 4
node0.next = node1
node1.next = node2
node2.next = node3
node3.next = node4

node0.random = None
node1.random = node0
node2.random = node4
node3.random = node2
node4.random = node0

sol = Solution()
copied = sol.copyRandomList(node0)

print("Original List:")
print_random_list(node0)

print("\nCopied List:")
print_random_list(copied)