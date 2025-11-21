import pytest
from Hashing.Map.KeyDesign.GroupAnagrams import Solution

def test_basic():
    strs=["eat","tea","tan","ate","nat","bat"]
    expected_output = [["bat"],["nat","tan"],["ate","eat","tea"]]
    actual_output = Solution().groupAnagrams2(strs)
    assert sorted([sorted(group) for group in actual_output]) == sorted([sorted(group) for group in expected_output])
def test_edge_single():
    strs=["a"]
    assert Solution().groupAnagrams2(strs)==[["a"]]
def test_edge_empty():
    strs=[""]
    assert Solution().groupAnagrams2(strs)==[[""]]