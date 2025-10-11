# another kadanes algorithm implementatin
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        _current, _max = nums[0], nums[0]
        for num in nums[1:]:
            _current = max(num, _current+num)
            _max = max(_max,_current)
        return _max