import pytest
from Hashing.Map.FourSumII import Solution 

def test():
    nums1=[1,2]
    nums2=[-2,-1]
    nums3=[-1,2]
    nums4=[0,2]
    assert Solution().fourSumCount(nums1,nums2,nums3,nums4)==2