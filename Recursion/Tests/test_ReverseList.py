import pytest
from Recursion.ReverseList import Solution, ListNode

def build_linked_list(values: list[int]) -> ListNode | None:
    if not values:
        return None
    head = ListNode(values[0])
    cur = head
    for v in values[1:]:
        cur.next = ListNode(v)
        cur = cur.next
    return head

def linked_list_to_list(head: ListNode | None) -> list[int]:
    result = []
    cur = head
    while cur:
        result.append(cur.val)
        cur = cur.next
    return result

def test_reverse_empty_list():
    sol = Solution()
    head = build_linked_list([])
    reversed_head = sol.reverseList(head)
    assert linked_list_to_list(reversed_head) == []

def test_reverse_single_node():
    sol = Solution()
    head = build_linked_list([1])
    reversed_head = sol.reverseList(head)
    assert linked_list_to_list(reversed_head) == [1]

def test_reverse_two_nodes():
    sol = Solution()
    head = build_linked_list([1, 2])
    reversed_head = sol.reverseList(head)
    assert linked_list_to_list(reversed_head) == [2, 1]

def test_reverse_multiple_nodes():
    sol = Solution()
    head = build_linked_list([1, 2, 3, 4, 5])
    reversed_head = sol.reverseList(head)
    assert linked_list_to_list(reversed_head) == [5, 4, 3, 2, 1]
