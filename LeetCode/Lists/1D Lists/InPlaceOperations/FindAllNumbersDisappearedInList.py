# Time O(n) - we do two loops through nums, once to mark the nums we've seen and the second to add the missing nums to the output
# Space O(1) - we dont consider the output list as extra space
# we know that the range of numbers in nums is from [1,n] 
# we can modify the values at those indexes and add the non modified indexes to the output list
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            index = abs(nums[i])-1 # we need to check the index this way in case there are any duplicates 
            if nums[index] > 0:
                nums[index] *= -1 # modify the number at the index that is stored within nums[i]-1 (zero based)
        for j in range(1,len(nums)+1):
            if nums[j-1] > 0: # look for the non modified elements and add the index - which are the missing numbers
                output.append(j)
        return output
sol = Solution()
print(sol.findDisappearedNumbers([4,3,2,7,8,2,3,1]))