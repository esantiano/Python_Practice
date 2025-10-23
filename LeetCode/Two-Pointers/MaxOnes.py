# Two pointer exercise using fast and slow pointers and max comparisons 
# we can use the indexes of the pointers to calculate the length of a window of consecutive ones, no need to increment result everytime we see a 1
# this is a sliding window technique 
class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        slow = 0
        fast = 0
        result = 0
        
        while fast < len(nums):
            if nums[fast] == 1:
                result = max(result, fast-slow+1)
            else:
                slow = fast+1 
            fast +=1
        return result
sol = Solution()
print(sol.findMaxConsecutiveOnes([1,0,1,1,0,1]))