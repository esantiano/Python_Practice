import pytest
from Hashing.Map.IntersectionOfTwoLists import Solution

def test_basic_match():
    nums1=[1,2,2,1]
    nums2=[2,2]
    assert Solution().intersect(nums1,nums2)==[2,2]
def test_basic_no_match():
    nums1=[1,3,4]
    nums2=[2,5]
    assert Solution().intersect(nums1,nums2)==[]
def test_edge_single_match():
    nums1=[1]
    nums2=[1]
    assert Solution().intersect(nums1,nums2)==[1]
def test_edge_single_no_match():
    nums1=[1]
    nums2=[2]
    assert Solution().intersect(nums1,nums2)==[]
