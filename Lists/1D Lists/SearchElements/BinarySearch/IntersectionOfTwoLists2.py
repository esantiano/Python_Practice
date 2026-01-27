# Time: O(MlogM + MlogN)
#   Here M is the length of the shorter list while N is length of the longer
#   O(MlogM) and O(NlogN) tims is required to sort both lists 
#   O(M) time is used to iterate through the shorter list
#   O(logN) time is used for the binary search of the longer list
# Space: O(N+M) 
#   this space is required for the sorted lists 
# Notes: 
#   This variation invloves two unsorted lists that contain duplicate values
#   We are looking for values that occur in both lists. 
#   [1,2,2,1], [2,2] => [2,2] 
#   [9,4,4,9,9], [4,9,5] => [4,9] or [9,4]
# Algorithm:
#   first sort each list
#   determine the smaller list
#   iterate through smaller list
#   binary search through larger list until we find the leftmost matching element index
#   retain the leftmost index to prevent duplicates and shrink the search space 
#   return result list
from typing import List
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s_nums1 = sorted(nums1)
        s_nums2 = sorted(nums2)
        
        if len(s_nums2) < len(s_nums1):
            s_nums1, s_nums2 = s_nums2, s_nums1
            
        # here we assume s_nums1 is shorter
        result = []
        start_index = 0
        for i in s_nums1:
            L, R = start_index, len(s_nums2)-1
            found_idx = -1
            while L <= R:
                M = L + (R-L)//2
                if s_nums2[M] >= i: # keep searching for the left most index
                    if s_nums2[M] == i:
                        found_idx = M
                    R = M - 1
                else:
                    L = M + 1 
            if found_idx != -1:
                result.append(i)
                start_index = found_idx + 1
        return result