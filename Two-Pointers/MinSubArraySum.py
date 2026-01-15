# Two pointer technique sliding window
# the window size updates once we find the min number of elements required to meet or exceed target value
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        minLen = len(nums)+1
        l = 0 
        window_sum = 0
        for r in range(len(nums)):
            window_sum += nums[r]
            while window_sum >= target:
                minLen = min(minLen,r-l+1)
                window_sum -= nums[l]
                l +=1
        if minLen > len(nums):
            return 0
        return minLen
sol = Solution()
print(sol.minSubArrayLen(11,[1,2,3,4,5]))