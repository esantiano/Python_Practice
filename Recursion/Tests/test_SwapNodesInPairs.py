import pytest
from Recursion.SwapNodesInPairs import ListNode, Solution

def list_to_linkedlist(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linkedlist_to_list(head):
    arr = []
    current = head
    while current:
        arr.append(current.val)
        current = current.next
    return arr

@pytest.fixture
def sol():
    return Solution()

def test_empty_list(sol):
    head = list_to_linkedlist([])
    result_head = sol.swapPairs(head)
    result_list = linkedlist_to_list(result_head)
    assert result_list == []

def test_single_node(sol):
    head = list_to_linkedlist([1])
    result_head = sol.swapPairs(head)
    result_list = linkedlist_to_list(result_head)
    assert result_list == [1]

def test_two_nodes(sol):
    head = list_to_linkedlist([1, 2])
    result_head = sol.swapPairs(head)
    result_list = linkedlist_to_list(result_head)
    assert result_list == [2, 1]

def test_even_length_list(sol):
    head = list_to_linkedlist([1, 2, 3, 4])
    result_head = sol.swapPairs(head)
    result_list = linkedlist_to_list(result_head)
    assert result_list == [2, 1, 4, 3]

def test_odd_length_list(sol):
    head = list_to_linkedlist([1, 2, 3, 4, 5])
    result_head = sol.swapPairs(head)
    result_list = linkedlist_to_list(result_head)
    assert result_list == [2, 1, 4, 3, 5]

@pytest.mark.parametrize("input_list, expected_list", [
    ([1, 2, 3, 4, 5, 6], [2, 1, 4, 3, 6, 5]),
    ([10, 20, 30], [20, 10, 30]),
    ([5, 1], [1, 5]),
])
def test_parametrized_scenarios(sol, input_list, expected_list):
    head = list_to_linkedlist(input_list)
    result_head = sol.swapPairs(head)
    result_list = linkedlist_to_list(result_head)
    assert result_list == expected_list
