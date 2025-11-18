# Time O(n) - we will see each element once
# Space: O(n) - worst case is the hashset will contain all elements 
# Note: This is just practicing using a hash set, the actual problem requires O(1) space constraint
# Algorithm using a hashset:
# use a hashset to keep track of variables we have seen
# loop through the list
# add nums to seen 
# remove duplicates from seen
# return the remaining num in the set
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                seen.remove(num)
            else:
                seen.add(num)
        return seen.pop()