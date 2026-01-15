# Time O(n) - one pass
# Space O(1) - in place
# Technique: two pointers, slow pointer to write, fast pointer to read 
# Another way to think of this is we are deleting elements in place
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        unique_position = 0
        for idx in range(len(nums)):
            if idx == 0 or (nums[idx] != nums[idx-1]):
                nums[unique_position] = nums[idx]
                unique_position+=1
        return unique_position
sol = Solution()
print(sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))