import pytest
from Hashing.Set.HappyNumber import Solution

def test_ishappy_true():
    n = 19
    assert Solution().isHappy(n) == True

def test_ishappy_false():
    n = 2
    assert Solution().isHappy(n) == False

def test_ishappy_edge():
    n = 1
    assert Solution().isHappy(n) == True

def test_ishappy_edge():
    n = 2438291041
    assert Solution().isHappy(n) == False


# -------------------Test isHappy2--------------------
def test_ishappy2_true():
    n = 19
    assert Solution().isHappy2(n) == True

def test_ishappy2_false():
    n = 2
    assert Solution().isHappy2(n) == False

def test_ishappy2_edge():
    n = 1
    assert Solution().isHappy2(n) == True

def test_ishappy2_edge():
    n = 2438291041
    assert Solution().isHappy2(n) == False
