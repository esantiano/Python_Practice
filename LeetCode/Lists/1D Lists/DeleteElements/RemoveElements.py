# Time O(n^2) - worst time complexity since we need to loop through elements ahead of val to overwrite val at its index
# Space O(1) - no extra space 
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        length = len(nums)
        # we must use an index to shift the elements in nums
        i = 0 
        while i < length: # the while loop will give us more control over the loop for situations like [num,val,val,num] 
            if nums[i] == val: # shift all the elements ahead of index to left to "delete" val
                for j in range(i,length-1): 
                    nums[j] = nums[j+1] # shift all elements left
                length-=1 # reduce the length, this will change our loop condition
            else:
                i+=1 # only move the index if the current element isnt equal to val
        return length
    
sol = Solution()
print(sol.removeElement([3,2,2,3],3)) # case where val is not in consecutive indexes
print(sol.removeElement([0,1,2,2,3,0,4,2],2)) # case where val is in consecutive indexes *
