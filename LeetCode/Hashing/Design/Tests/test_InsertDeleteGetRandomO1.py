import pytest
from Hashing.Design.InsertDeleteGetRandomO1 import RandomizedSet

def test_basic():
    randomset = RandomizedSet()
    assert randomset.insert(1)==True
    assert randomset.remove(2)==False
    assert randomset.insert(2)==True 
    assert randomset.getRandom()==1 or randomset.getRandom()==2
    assert randomset.remove(1)==True 
    assert randomset.insert(2)==False
    assert randomset.getRandom()==2