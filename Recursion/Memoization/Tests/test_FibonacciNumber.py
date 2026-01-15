import pytest
from Recursion.Memoization.FibonacciNumber import Solution

def test_optomized():
    assert Solution().fibOptimized(4) == 3

def test():
    assert Solution().fib(4) == 3