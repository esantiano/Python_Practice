# Time: O(logN) time required for the binary search
# Space: O(1) no extra time is required
# Algorithm: 
#   Standard binary search algorithm but with a tweak.
#   The search uses the right boundary as an anchor to determine the minimum element.
#   We also account for repeated values within the list however we conservatively recduce the search space
#   since we aren't sure about where the minimum value is located since the list could be rotated.
from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        L , R = 0, len(nums)-1
        while L < R:
            M = L + (R-L)//2
            if nums[M] < nums[R]:
                R = M
            elif nums[M] == nums[R]:
                R -= 1
            else:
                L = M + 1
        return nums[L]