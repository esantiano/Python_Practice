# Time: O(NlogN) 
#   O(N) time required to sum the count
#   O(logN) time required for the binary search
# Space: O(1) - no extra space is used (technically)
# Algorithm: 
#   here our search space is 1 -> n
#   at a given value within 1 -> n values that occur before the duplicate will have as many values from the list that are <= to that value as itself 
#   values past the duplicate value will have a number of values from the list that are > itself 
#   we can use this reasoning to find the duplicate value and determine which half of the search space we need to search
#   if the count of a value is <= value itself we search the right space
#   if the count of a value is > value itself we search the left space 
#   we reduce the search space to one element 
#   determine the mid point to check within 1 -> n
#   determine the count of numbers from the list <= midpoint
#   compare the count to the midpoint 
#   record the minimum value that have counts higher than itself
from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        L, R = 1, len(nums)-1
        cur_min = float("inf")
        while L <= R:
            M = (R+L)//2
            
            # the current method of determining count uses a temporary list technically violating the extra space constraint
            # we can replace the method to determine the count by using sum(x <= M for x in nums) the comparison x <= M returns T(1) or F(0) 
            count = len([x for x in nums if x <= M]) 
            if count <= M:
                L = M + 1
            else:
                R = M - 1
                cur_min = min(cur_min,M)
        return cur_min