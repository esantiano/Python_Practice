import pytest
import sys
from Hashing.Set.SingleNumber import Solution

def test_single_number_basic():
    nums = [2, 2, 1]
    assert Solution().singleNumber(nums) == 1

def test_single_number_larger():
    nums = [4, 1, 2, 1, 2]
    assert Solution().singleNumber(nums) == 4

def test_single_number_negative_values():
    nums = [-1, -1, -2]
    assert Solution().singleNumber(nums) == -2

def test_single_number_single_element():
    nums = [7]
    assert Solution().singleNumber(nums) == 7

def test_single_number_mixed_values():
    nums = [0, 1, 0, 1, 99]
    assert Solution().singleNumber(nums) == 99