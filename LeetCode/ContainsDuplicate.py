# we can use a hashtable _seen to store all the numbers we've seen in num 
# we can sort nums to cut down on time
# we will loop through nums 
# if its the first time we've seen a number then add it to _seen
# if its not the first time we've seen a number then return True
# if we loop through the entire list then return False
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # _seen = {}
        # # nums.sort()
        # for val in nums:
        #     if val not in _seen:
        #         _seen[val] = 1
        #     else: 
        #         return True
        # return False
        nums.sort()
        idx = 1
        while idx < len(nums):
            if nums[idx] == nums[idx-1]:
                return True
            idx += 1
        return False