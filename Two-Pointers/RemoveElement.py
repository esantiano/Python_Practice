# Two pointer technique for removing elements using a fast and slow pointer
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        for num in nums:
            if num != val:
                nums[k] = num
                k+=1
        return k
sol = Solution()
print(sol.removeElement([3,2,2,3],3))