# Time O(N) - N = number of items in nums since we will have to check each number
# Space O(1) = no extra space is used 
# two pointer technique 
#   create a pointer to keep track of the current index, we want to start it at 1 since we know that the starting index should always be unique 
#   create a second pointer to move through the list and find the unique numbers
#   we'll compare the element at the second pointer to the previous element
#   update the element at the current index  
#   increment the current index 
#   return the current index - no need to return anything else
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        current = 1
        for i in range(1,n):
            if nums[i-1] != nums[i]:
                nums[current] = nums[i] 
                current += 1
        return current