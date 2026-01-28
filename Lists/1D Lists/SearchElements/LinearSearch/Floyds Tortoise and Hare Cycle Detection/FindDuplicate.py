# Time: O(N) we traverse the list twice 
# Space: O(1) no extra space used 
# Algorithm: 
#   we use floyds cycle detection algorithm to determine the duplicated number,
#   the values in nums are used as indexes for the next value 
#   two pointers are used, slow and fast
#   in the first traversal we allow the fast to lap the slow until the meet
#   we then reset the slow pointer to the beginning of the list
#   in the second traversal we move both pointers at the slow pace and allow both pointers to meet this will determine the duplicate value
from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tortoise = hare = nums[0]
        while True:
            tortoise = nums[tortoise] # to move slowly we use the value at the current index
            hare = nums[nums[hare]] # to move fast twice as fast as slow we use the value of the next index
            if tortoise == hare:
                break
        
        tortoise = nums[0]
        while tortoise != hare:
            tortoise=nums[tortoise]
            hare = nums[hare]

        return hare