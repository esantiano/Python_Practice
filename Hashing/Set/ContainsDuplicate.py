# Time O(n) - at worst we go through the entire nums list
# Space O(n) - we use extra space for the set 
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False