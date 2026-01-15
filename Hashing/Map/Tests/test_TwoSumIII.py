import pytest
from Hashing.Map.TwoSumIII import TwoSum


def test_basic_true():
    sol = TwoSum()
    sol.add(1)
    sol.add(2)
    sol.add(3)
    assert sol.find(4) == True
def test_basic_false():
    sol = TwoSum()
    sol.add(1)
    sol.add(2)
    sol.add(3)
    assert sol.find(6) == False
def test_edge_double_true():
    sol = TwoSum()
    sol.add(1)
    sol.add(3)
    sol.add(3)
    assert sol.find(6) == True
def test_edge_double_false():
    sol = TwoSum()
    sol.add(0)
    assert sol.find(0) == False
