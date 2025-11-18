import pytest

from Hashing.Set.IntersectionOfTwoLists import Solution, Solution2

def test_solution_basic():
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    assert Solution().intersection(nums1,nums2) == [2]
def test_solution_basic2():
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    assert Solution().intersection(nums1,nums2) == [4,9] or [9,4]
def test_solution_edge_empty1():
    nums1 = []
    nums2 = [1,2,3]
    assert Solution().intersection(nums1,nums2) == []
def test_solution_edge_empty2():
    nums1 = []
    nums2 = []
    assert Solution().intersection(nums1,nums2) == []
def test_solution_edge_multiple():
    nums1 = [1,1,1]
    nums2 = [1,1,1]
    assert Solution().intersection(nums1,nums2) == [1]
def test_solution_edge_single():
    nums1 = [5]
    nums2 = [5]
    assert Solution().intersection(nums1,nums2) == [5]
def test_solution_edge_boundary():
    nums1 = [1000, 1]
    nums2 = [1, 1000]
    assert Solution().intersection(nums1,nums2) == [1, 1000] or [1000,1]

def test_solution2_basic():
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    assert Solution2().intersection(nums1,nums2) == [2]
def test_solution2_basic2():
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    assert Solution2().intersection(nums1,nums2) == [4,9] or [9,4]
def test_solution2_edge_empty1():
    nums1 = []
    nums2 = [1,2,3]
    assert Solution2().intersection(nums1,nums2) == []
def test_solution2_edge_empty2():
    nums1 = []
    nums2 = []
    assert Solution2().intersection(nums1,nums2) == []
def test_solution2_edge_multiple():
    nums1 = [1,1,1]
    nums2 = [1,1,1]
    assert Solution2().intersection(nums1,nums2) == [1]
def test_solution2_edge_single():
    nums1 = [5]
    nums2 = [5]
    assert Solution2().intersection(nums1,nums2) == [5]
def test_solution2_edge_boundary():
    nums1 = [1000, 1]
    nums2 = [1, 1000]
    assert Solution2().intersection(nums1,nums2) == [1, 1000] or [1000,1]