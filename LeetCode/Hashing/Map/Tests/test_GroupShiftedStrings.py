import pytest
from Hashing.Map.KeyDesign.GroupShiftedStrings import Solution

def test_basic():
    strs=["abc","bcd","acef","xyz","az","ba","a","z"]
    expected_output = [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]
    actual_output = Solution().groupStrings(strs)
    assert sorted([sorted(group) for group in actual_output]) == sorted([sorted(group) for group in expected_output])