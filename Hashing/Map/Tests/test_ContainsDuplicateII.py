import pytest
from Hashing.Map.ContainsDuplicateII import Solution

def test_basic_true():
    nums = [1,2,3,1]
    k = 3
    assert Solution().containsNearbyDuplicate(nums,k) == True

def test_basic_false():
    nums = [1,2,3,1,2,3]
    k = 2
    assert Solution().containsNearbyDuplicate(nums,k) == False

def test_edge_single_element_false():
    nums = [1]
    k = 1
    assert Solution().containsNearbyDuplicate(nums,k) == False

def test_edge_unique_elements_false():
    nums = [1,2,3,4,5]
    k = 4
    assert Solution().containsNearbyDuplicate(nums,k) == False

def test_edge_identical_elements_true():
    nums = [1,1,1,1,1,1]
    k = 3
    assert Solution().containsNearbyDuplicate(nums,k) == True

def test_edge_k_is_zero_false():
    nums = [1,0,1,1]
    k = 0
    assert Solution().containsNearbyDuplicate(nums,k) == False

def test_edge_k_is_greater_than_nums_false():
    nums = [1,2,3,4,5,6]
    k = 10
    assert Solution().containsNearbyDuplicate(nums,k) == False

def test_edge_k_is_greater_than_nums_true():
    nums = [1,2,3,4,5,1]
    k = 10
    assert Solution().containsNearbyDuplicate(nums,k) == True
