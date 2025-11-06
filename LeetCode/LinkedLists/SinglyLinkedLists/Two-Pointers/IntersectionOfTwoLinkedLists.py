# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# Time O(m+n) m - length of list a, n - length of list b
# Space O(1) - no extra space used 
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> [ListNode]:
        # count the nodes in each list 
        # take the difference between the counts 
        # move the longer list pointer that difference along its list
        # reset the shorter list pointer 
        # move both pointers at the same rate until we find the intersection
        # return the intersecting node
        # return null 
        
        count_a = 0
        count_b = 0 
        
        cur_a = headA
        cur_b = headB
        
        while cur_a != None:
            cur_a = cur_a.next
            count_a +=1
        while cur_b != None:
            cur_b = cur_b.next
            count_b +=1
        
        diff = 0
        if count_a > count_b:
            diff = count_a-count_b
            cur_a = headA 
            count_a = 0
            while count_a<diff:
                cur_a=cur_a.next
                count_a+=1
            cur_b = headB
        elif count_b>count_a: 
            diff = count_b-count_a
            cur_b = headB 
            count_b = 0
            while count_b<diff:
                cur_b=cur_b.next
                count_b+=1
            cur_a = headA
        else:
            cur_a = headA
            cur_b = headB
        
        while cur_a != cur_b:
            cur_a = cur_a.next
            cur_b=cur_b.next
        
        if cur_a == cur_b:
            return cur_a
        return None
# same time and space complexity
# without keeping count, we can reset the pointers for the shorter list until the pointers match places in the list. 
# the loop will run once and the shorter list nodes will be seen more than once but it will give the longer list pointer 
# time to catch up. 
# what if the lists don't intersect? 
# At some point both pointers hit the end of their respective lists at the same time and they will both point to None.
    def getIntersectionNode2(self, headA: ListNode, headB: ListNode) -> [ListNode]:
        cur_a = headA
        cur_b = headB

        while cur_a != cur_b: 
            cur_a = headA if cur_a is None else cur_a.next
            cur_b = headB if cur_b is None else cur_b.next
        return cur_a

# --- Intersecting List 1 (L1_Int) nodes ---
L1_Int_head = ListNode(1)
current_l1 = L1_Int_head
for i in range(2, 6):
    current_l1.next = ListNode(i)
    current_l1 = current_l1.next

# --- Create the intersection point and subsequent shared nodes ---
intersection_node = ListNode(50)
current_l1.next = intersection_node # L1 links to the intersection
current_shared = intersection_node
for i in range(51, 55):
    current_shared.next = ListNode(i)
    current_shared = current_shared.next

# --- Intersecting List 2 (L2_Int) nodes ---
L2_Int_head = ListNode(10)
current_l2 = L2_Int_head
current_l2.next = ListNode(20)
current_l2 = current_l2.next
current_l2.next = intersection_node # L2 links to the shared intersection point

print("--- INTERSECTING LISTS ---")
# Verification for intersecting lists
print("L1_Int path:")
current = L1_Int_head
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")

print("\nL2_Int path:")
current = L2_Int_head
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")
print("-" * 30)


# =======================================================
# SECTION 2: TWO NON-INTERSECTING LINKED LISTS
# =======================================================

# --- Non-Intersecting List 1 (L1_Non) nodes ---
L1_Non_head = ListNode(1000)
current_l1_non = L1_Non_head
for i in range(1001, 1005):
    current_l1_non.next = ListNode(i)
    current_l1_non = current_l1_non.next

# --- Non-Intersecting List 2 (L2_Non) nodes ---
L2_Non_head = ListNode(2000)
current_l2_non = L2_Non_head
for i in range(2001, 2007):
    current_l2_non.next = ListNode(i)
    current_l2_non = current_l2_non.next
# Note: No node from L1_Non ever points to any node in L2_Non, and vice versa.

print("--- NON-INTERSECTING LISTS ---")
# Verification for non-intersecting lists
print("L1_Non path:")
current = L1_Non_head
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")

print("\nL2_Non path:")
current = L2_Non_head
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")
print("-" * 30)

sol = Solution()
print(sol.getIntersectionNode(L1_Int_head,L2_Int_head).val)
print(sol.getIntersectionNode(L1_Non_head,L2_Non_head))
print(sol.getIntersectionNode2(L1_Int_head,L2_Int_head).val)
print(sol.getIntersectionNode2(L1_Non_head,L2_Non_head))


