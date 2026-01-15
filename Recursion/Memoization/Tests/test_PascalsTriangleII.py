import pytest
from Recursion.Memoization.PascalsTriangleII import Solution

def test_optomized():
    assert Solution().getRowOptimized(4) == [1,4,6,4,1]

def test():
    assert Solution().getRow(4) == [1,4,6,4,1]