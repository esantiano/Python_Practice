# Time O(N) 
# Space O(1)
# Two pointer sliding window technique
# we keep track of the longest sequence of 1s and zeros
# when we encounter a zero we increment zeros count
# if we encounter another zero that means the sequence of 1s has ended
# we need to move the left pointer to decrement the number of consecutive 1s 
# we continually update the right pointer and take the max longest sequence 
class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        longest_seq = 0
        left,right = 0
        zeros_count = 0

        while right < len(nums):
            if nums[right] == 0:
                zeros_count+=1
            while zeros_count ==2:
                if nums[left] == 0:
                    zeros_count-=1
                left+=1
            longest_seq = max(longest_seq, right-left+1)
            right+=1

        return longest_seq
sol = Solution()
print(sol.findMaxConsecutiveOnes([1,0,1,1,0,1]))