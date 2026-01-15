class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        _hash = {0:0,1:0,2:0}
        for num in nums:
                _hash[num] += 1
        i = 0
        while i < (_hash[0]):
            nums[i] = 0
            i+= 1
        while i < (_hash[0] + _hash[1]):
            nums[i] = 1
            i+=1
        while i < (_hash[0] + _hash[1] + _hash[2]):
            nums[i] = 2
            i+=1 
        return nums