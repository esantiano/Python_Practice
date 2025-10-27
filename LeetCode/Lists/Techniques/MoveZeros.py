# Time O(N) - we need to iterate through nums at least once
# Space O(1) - can be done in place
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # two step approach using two pointers, not operation optimal 
        current = 0 
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[current] = nums[i]
                current +=1
        for j in range(current,len(nums)):
                nums[j] = 0

        # we realize that we are swappwing elements at current and i we 
        current = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[current],nums[i]=nums[i],nums[current]
                current += 1
        return nums