class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)/2
        def recurse(lo, hi):
            if hi == lo:
                return nums[lo] 
            mid = (hi -lo)//2 + lo
            left = recurse(lo,mid)
            right = recurse(mid+1,hi)
            if left == right:
                return left
            left_count = sum(1 for i in range(lo,hi +1) if nums[i] == left)
            right_count = sum(1 for i in range(lo, hi + 1) if nums[i] == right)
            return left if left_count > right_count else right  
        return recurse(0,len(nums)-1)