import pytest
from Hashing.Map.TwoSum import Solution

def test_twosum_basic():
    n = [2,7,11,15]
    target = 9
    assert Solution().twoSum(n,target) == [0,1] or Solution().twoSum(n,target) == [1,0]

def test_twosum_edge_duplicate():
    n = [3,3]
    target = 6
    assert Solution().twoSum(n,target) == [0,1] or Solution().twoSum(n,target) == [1,0]

def test_twosum_edge_zero():
    n = [-5,5]
    target = 0
    assert Solution().twoSum(n,target) == [0,1] or Solution().twoSum(n,target) == [1,0]

def test_twosum_edge_zero_zeros():
    n = [0,0]
    target = 0
    assert Solution().twoSum(n,target) == [0,1] or Solution().twoSum(n,target) == [1,0]