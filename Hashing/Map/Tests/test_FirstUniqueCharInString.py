import pytest
from Hashing.Map.FirstUniqueCharInString import Solution

def test_f1_basic():
    s = "loveleetcode"
    assert Solution().firstUniqChar(s) == 2
def test_f1_edge_empty():
    s = ""
    assert Solution().firstUniqChar(s) == -1
def test_f1_edge_single():
    s = "a"
    assert Solution().firstUniqChar(s) == 0
def test_f1_edge_first():
    s = "abbbbbb"
    assert Solution().firstUniqChar(s) == 0
def test_f1_edge_last():
    s = "bbbbbbc"
    assert Solution().firstUniqChar(s) == 6
def test_f1_edge_duplicates():
    s = "aabb"
    assert Solution().firstUniqChar(s) == -1


def test_f2_basic():
    s = "loveleetcode"
    assert Solution().firstUniqChar2(s) == 2
def test_f2_edge_empty():
    s = ""
    assert Solution().firstUniqChar2(s) == -1
def test_f2_edge_single():
    s = "a"
    assert Solution().firstUniqChar2(s) == 0
def test_f2_edge_first():
    s = "abbbbbb"
    assert Solution().firstUniqChar2(s) == 0
def test_f2_edge_last():
    s = "bbbbbbc"
    assert Solution().firstUniqChar2(s) == 6
def test_f2_edge_duplicates():
    s = "aabb"
    assert Solution().firstUniqChar2(s) == -1

