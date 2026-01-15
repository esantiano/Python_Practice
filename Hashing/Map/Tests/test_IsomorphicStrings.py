import pytest
from Hashing.Map.IsomorphicStrings import Solution

def test_basic_false():
    s="foo"
    t="bar"
    assert Solution().isIsomorphic(s,t) == False

def test_basic_true():
    s="egg"
    t="add"
    assert Solution().isIsomorphic(s,t) == True

def test_advanced_false():
    s="badc"
    t="baba"
    assert Solution().isIsomorphic(s,t) == False

def test_advanced_true():
    s="paper"
    t="title"
    assert Solution().isIsomorphic(s,t) == True