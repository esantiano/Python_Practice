# Practice swapping in place, understand what conditions required to swap
# Time O(n) - one pass
# Space O(1) - in place
class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        current_even_position = 0
        for i in range(len(nums)):
            if nums[i]%2 == 0:
                nums[current_even_position], nums[i] = nums[i], nums[current_even_position]
                current_even_position +=1
        return nums
sol = Solution()
print(sol.sortArrayByParity([3,1,2,4]))