import pytest
from Hashing.Map.LongestSubstringWithoutRepeatingCharacters import Solution

def test_basic():
    s="abcabcbb"
    assert Solution().lengthOfLongestSubstring() == 3

def test_edge_empty():
    s=""
    assert Solution().lengthOfLongestSubstring() == 0

def test_edge_single():
    s="a"
    assert Solution().lengthOfLongestSubstring() == 1

def test_edge_all_unique():
    s="abcdefg"
    assert Solution().lengthOfLongestSubstring() == 7

def test_edge_all_repeating():
    s="aaaaaaa"
    assert Solution().lengthOfLongestSubstring() == 1

def test_edge_end_repeating():
    s="abcdeff"
    assert Solution().lengthOfLongestSubstring() == 6

def test_edge_middle_repeating():
    s="dvdf"
    assert Solution().lengthOfLongestSubstring() == 3

def test_edge_same_length_unique():
    s="pwwkew"
    assert Solution().lengthOfLongestSubstring() == 3




