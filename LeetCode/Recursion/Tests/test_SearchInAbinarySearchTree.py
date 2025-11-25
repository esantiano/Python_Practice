import pytest 
from Recursion.SearchInABinarySearchTree import Solution, TreeNode

def build_example_bst():
    n1 = TreeNode(1)
    n3 = TreeNode(3)
    n2 = TreeNode(2, n1, n3)
    n7 = TreeNode(7)
    root = TreeNode(4, n2, n7)
    return root

def test_found():
    sol = Solution()
    root = build_example_bst()
    result = sol.searchBSTOptimized(root, 2)
    assert result.val == 2
    assert result.left.val == 1
    assert result.right.val == 3

    
def test_not_found():
    sol = Solution()
    root = build_example_bst()
    result = sol.searchBSTOptimized(root, 5)
    assert result == None

