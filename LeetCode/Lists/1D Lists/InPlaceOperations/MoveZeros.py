# Practice swapping elements in place
# Time O(n) - we only go through the list once
# Space O(1) - this is done in place 
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        current_unique_position = 0 
        for idx in range(len(nums)):
            if nums[idx] != 0:
                nums[idx],nums[current_unique_position] = nums[current_unique_position],nums[idx]
                current_unique_position += 1
        return nums
sol = Solution()
print(sol.moveZeroes([0,1,0,3,12]))