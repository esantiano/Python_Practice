# Binary Search Practice
# sort the list first 
# calculate the target value as 2*arr[i]
# use a custom function to validate the current value
#   use let, middle, right pointer 
#   use while loop to drive 
#   compare the middle pointer to target value
#   move left pointer to mid + 1 if middle pointer element < target
#   move right pointer to mid - 1 if middle pointer element > target 
#   return middle pointer if target is found
#   return -1 if the target is not found
# Time O(nlogn) - sorting is O(nlogn) time, binary search takes O(logn) time, but note that binary search is called in the for loop O(n) 
# Space O(n) - python uses space for sort() 
class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        n = len(arr)
        arr.sort()
        
        for i in range(n):
            target = arr[i]*2
            j = self.bin_search(target,arr)
            if j != -1 and i != j:
                return True
        return False
    
    def bin_search(self,target,arr):
        left = 0
        right = len(arr)-1
        while left<=right:
            mid = left + (right - left) // 2 
            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                right = mid-1
            else:
                left = mid+1
            # print (left, right, arr[mid])
        return -1
sol = Solution()
print(sol.checkIfExist([10,2,5,3]))
print(sol.checkIfExist([3,1,7,11]))