# Time: O(n) - we are checking every element in nums
# Space O(n) - at worst case the map will hold all elements 
# Algorithm:
# use a map to store number and index kvp
# go through nums
# check the map to see if there is a kvp for target - current value
# if there is return the target-currentvalue value and the current index
# if there isn't then add the current value index pair ot the map
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i in range(len(nums)):
            cur = nums[i]
            if target-cur in seen:
                j = seen[target-cur] 
                return[i,j]
            else:
                seen[cur]=i