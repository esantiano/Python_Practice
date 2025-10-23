# two sum using in place and two pointers
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l = 0 
        r = len(numbers)-1
        
        while l<r:
            sum = numbers[l] + numbers[r]
            if sum == target:
                break
            elif sum > target:
                r -=1 
            else:
                l+=1 
        return[l+1,r+1] 
sol = Solution()
print(sol.twoSum([2,7,11,15], 9))