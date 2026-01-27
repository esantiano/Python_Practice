# Time: O(mlogm + nlogn) - time required to sort the lists, perform a linear search on the shorter list and binary search on the longer list
# Space: O(m+n) - we require space for the sorted lists 
# Algorithm:
#   sort each list
#   iterate through the shorter list
#   use binary search on the longer list to search for matches 
from typing import List
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        sorted_nums1 = sorted(nums1)
        sorted_nums2 = sorted(nums2)
        
        m = len(sorted_nums1)
        n = len(sorted_nums2)
        
        if m < n:
            short = sorted_nums1
            long = sorted_nums2
        else:
            short = sorted_nums2
            long = sorted_nums1
        
        result = []
        for i in short:
            L, R = 0, len(long)-1
            while L <= R:
                M = L + (R-L)//2
                if long[M] == i and i not in result:
                    result.append(i)
                    break
                if long[M] < i:
                    L = M + 1
                else:
                    R = M - 1
        return result
            