# optimized solution for pivotIndex
# we can create a variable to hold the sum of nums
# we will also create a variable leftsum to hold the sum of numbers to the left of the current index
# we can treat the rightsum as the total minus current index num minus left sum
# formula for rightsum: s - nums[i] - leftsum
# formula for leftsum : leftsum += nums[i-1]
# we'll compare leftsum to rightsum and if an index is found return that index
# otherwise we'll return -1
class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        leftSum = 0
        total = sum(nums)

        for i in range(len(nums)):
            # if we set leftSum at the start of the loop then we need
            # to make sure that nums[-1] is not included in the starting sum since
            # for i = 0 i-1 = -1 
            # if i-1 < 0: 
            #     leftSum = 0 
            # else:
            #     leftSum += nums[i-1] 
            rightSum = total - nums[i] - leftSum
            # print(i, leftSum, rightSum)
            if leftSum == rightSum:
                return i
            # if we add the current number at nums[i] to leftSum at the end after the comparison then we dont have
            # to include a check for nums[-1] since it accounts for adding the current number after the comparison
            leftSum += nums[i]
        return -1
sol = Solution()
res = sol.pivotIndex([1,7,3,6,5,6])
print(res)