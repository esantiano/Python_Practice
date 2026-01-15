import pytest
from Hashing.Map.JewelsAndStones import Solution

def test_basic_some():
    jewels = "aA" 
    stones = "aAAbbbb"
    assert Solution().numJewelsInStones(jewels,stones)==3

def test_basic_none():
    jewels = "z" 
    stones = "ZZ"
    assert Solution().numJewelsInStones(jewels,stones)==0