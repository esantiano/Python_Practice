# Time: O(NlogS) 
#   O(N) time required to determine the number of lists for a given max
#   O(logS) time required to perform binary search on the search space S max, sum
# Space: O(1) no extra space is required 
# Algorithm:
#   our search space is max(nums) and sum(nums)
#   we calculate the midpoint of our search space 
#   from the midpoint we determine the number of lists that can be made
#   we do this by keeping a sum of the elements we have seen through iterating through nums
#   if the sum of elements is greater than the midpoint then we reset the sum to the last element #   we have seen and increment the count of lists made 
#   if the number of lists is less than or equal to K we can consider M a maximum value and move #   the right boundary of the search space
#   if it is greater then we move the left boundary of the search space 
#   we repeat this process until the search space is closed
from typing import List
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def isPossible(p_max):
            cur_sum = 0
            count = 1 # we start with the current list 
            for num in nums:
                cur_sum += num
                if cur_sum > p_max:
                    cur_sum = num
                    count += 1 
            return count <= k
        L, R = max(nums), sum(nums)
        
        while L <= R:
            M = (R+L)//2
            if isPossible(M):
                R = M - 1
            else:
                L = M + 1
        return L