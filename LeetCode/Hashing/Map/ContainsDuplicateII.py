# Time O(n) - we will need to look at all elements in nums
# Space O(n) - at worst each element in nums will be stored in the hashmap
# Algorithm:
# use a hashmap to store the num:index relationship
# iterate through nums 
# if we see num in the hashmap we compare the differences between the index in hashmap and current index to k
# if there is a match then return true
# otherwise update the index in the hashmap in case there is another match and comparison later 
# if we come to the end with no solution return false
class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        indices = {}
        for idx,num in enumerate(nums):
            if num in indices and abs(indices[num]-idx)<=k:
                return True
            else:
                indices[num]=idx
        return False