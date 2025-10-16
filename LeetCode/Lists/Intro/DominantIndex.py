# optimal solution
# we can find the max number in nums by using max(num)
# we can check using the all() function 
# return the index of the max number using nums.index()
# or return -1
class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        m = max(nums)
        if all(2*num <= m for num in nums if num != m):
            return nums.index(m)
        return -1
# sol = Solution()
# res = sol.dominantIndex([3,6,1,0])
# print(res)
