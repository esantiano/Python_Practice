# Time: O(logN)
#   When searching for the target value we cut the search space in half after every value comparison
# Space: O(1) - no extra space is used 
# Algorithm:
#   First we define the search spaces using left and right boundary indexes.
#   We search over the search space as long as its not empty using the condition left <= right
#   We calculate the pivot point (middle index) that divides the list in half. 
#   This pivot point is used to remove the half of the list thats unlikely to contain the target value
#   Since we are dealing with a sorted list we can use three conditions to determine what steps to take.
#   pivot index value = target, < target, > target. we recalculate the pivot index based on the latter two conditions.
#   We adjust the search space depending on which of the latter conditions were met. 
#   If the pivot index value is > or < target we can adjust the left or right boundaries +- 1
#   since we know that the search space up to or before the pivot index will not contain the target value
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            middle = (right-left)//2 + left
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle-1
        return -1