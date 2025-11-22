import pytest
from Hashing.Map.TopKFrequentElements import Solution

def test_basic():
    nums=[1,1,1,2,2,3]
    k=2
    assert Solution().topKFrequent(nums,k)==[1,2]

def test_edge_single():
    nums=[1]
    k=1
    assert Solution().topKFrequent(nums,k)==[1]