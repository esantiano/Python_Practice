# region hashmap solution:
class Solution:
    def twoSum(self, nums, target, i, hashmap):
        for j in range(i+1,len(nums)):
            y = nums[j]
            z = target-y
            if z in hashmap:
                k = hashmap[z] 
                if j < k:
                    yield y,z
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = set()
        nums = sorted(nums)
        hashmap = {}
        for idx in range(len(nums)):
            hashmap[nums[idx]] = idx

        for i in range(len(nums)):
            x = nums[i]
            for y,z in self.twoSum(nums,-x,i,hashmap):
                output.add((x,y,z))
        return [list(val) for val in output] 
# endregion
# region two pointer solution:
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(nums, idx):
            low = idx+1
            high = len(nums)-1
            while low < high:
                sum = nums[idx] + nums[low] + nums[high]
                if  sum < 0:
                    low += 1
                elif sum > 0:
                    high -=1
                else: 
                    results.append([nums[idx], nums[low], nums[high]])
                    high -=1
                    low +=1
                    while low < high and nums[low] == nums[low-1]:
                        low+=1

        nums.sort()
        n = len(nums)
        results = []
        
        for idx in range(n):
            if idx == 0 or nums[idx-1] != nums[idx]:
                twoSum(nums, idx)
        return results
        

# endgregion