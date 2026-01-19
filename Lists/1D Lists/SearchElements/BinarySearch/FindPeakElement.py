# Time: O(log2N)
#   We use binary search to reduce the search space for every iteration
# Space: O(1)
# Notes: 
#   We must use the fact that nums[i] != nums[i+1].
#   We only need to compare nums[i] to nums[i+1]. 
#   Reasoning behind this: 
#   assume peak is at beginning: all numbers appear in descending order, every number afterwards will be less than the starting number
#   assume peak is at the end:  all numbers appear in ascending order, we are on a rising slope, every number after the first will be greater than the last
#   assume peak is in the middle: every number before the peak will be less than as will every number after the peak
#   At every point we only need to check the number to the right because that neighbor will determine what kind of slope we are on, decreasing or increasing.
#   If we are on a decreasing slope then we know that the peak must be to the left of that number
#   If we are on an increasing slope then we know that the peak must be to the right of that number
#   We continue until we reduce the search space to 1 number which must be a peak.
from typing import List
class Solution:
# Algorithm:
#   Search space is entire nums list
#   We use binary search to narrow the index down to one value.
#   Here we must compare neighbors on both sides of mid to determine if we have found a peak.
    def findPeakElement1(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left<right:
            mid = left + (right-left)//2
            if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
                return mid
            elif nums[mid] < nums[mid+1]:
                left = mid + 1
            else:
                right = mid
        return left
# Algorithm:
#   In this algorithm we use the same search space in the previous algorithm
#   We use binary search to find a structural property (direction/slope)
#   We accomplish this by comparing the midpoint to its right hand neighbor to determine the direction to search
#   We continue until we have 2 elements to compare in the post process 
#   After we determine which two values are likely to be the peak value we compare the final values and return the peaks index
    def findPeakElement2(self, nums: List[int]) -> int:
        L, R = 0, len(nums)-1
        while L + 1 < R:
            M = L + (R-L)//2
            if nums[M] < nums[M+1]:
                L = M
            else:
                R = M
            
            
        if nums[L] > nums[R]:
            return L
        return R
    