# Time O(n) - n = length of nums 
# Space O(1) or O(n) depending on whether or not we count the output 

# two pointer technique - we only need to run through nums list once 
# list is sorted in non decreasing order and want to return nums list squared in sorted order 
# sorting and squaring is trivial but to get the optimal time complexity we need to use two pointers
# take advantage of the non decreasing order 
# compare either squared values or absolute values from both sides
# we build the resulting list in reverse order (largest values first)
# return the resulting list in reverse order
# cases [0,1,2,3], [-3,-2,-1,0,1,2,3,4]

# using pythons built in sort or sorted functions results in Time:O(nlogn)
class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        l = 0
        r = len(nums)-1
        result = []
        while l<=r:
            left = nums[l]
            right = nums[r]
            if abs(left)>abs(right):
                result.append(left*left)
                l+=1
            else:
                result.append(right*right)
                r-=1
        return result[::-1]
sol = Solution()
print(sol.sortedSquares([-4,-1,0,3,10]))