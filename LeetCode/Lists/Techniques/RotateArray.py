# three different solutions using different techniques
# the main trick is knowing that for k/n = 1*x rotations where x is any number and n is the length of the list 
# the rotation will result in the original list
# we need to take the remainder of the k%n to know the true number of places we need to rotate the list
# see rotate2 for clearer explanation 
class Solution:
    def rotate1(self, nums: list[int], k: int) -> None:
        # Time O(n^2) this passes but is the worst time complexity
        for i in range(k):
            nums.insert(0,nums.pop(-1))
    
    def rotate2(self, nums: list[int], k: int) -> None:
       # brute force Time O(n*k) results in RTE runtime error
       # no additional space
       k %= len(nums) 
       # This operation is commonly used in problems involving array rotation (e.g., rotating an array to the right by k steps).
       # The reason is that rotating an array by its length (or any multiple of its length) results in the array returning to its original state. 
       # Therefore, if k is greater than or equal to len(nums), the effective number of rotations needed is k modulo len(nums).
       for i in range(k):
           prev = nums[-1]
           for j in range(len(nums)):
               nums[j],prev = prev,nums[j]

    def rotate3(self, nums: list[int], k: int) -> None:
        # Space O(n) uses an extra list 
        # Time O(n)
        n = len(nums)
        hold = ['']*n
        for i in range(n):
            hold[(i+k)%n] = nums[i]
        #reassign nums
        for j in range(n):
            nums[j] = hold[j]
        # could use nums[:] = hold
    
    def rotate4(self, nums: list[int], k: int) -> None:
        def reverse(self,nums,start,end):
            while start<end:
                nums[end],nums[start] = nums[start],nums[end]
                end-=1
                start+=1
        # Time O(n)
        # Space O(1)
        n = len(nums)
        k %= n

        # first reverse the entire list
        l,r = 0,n-1
        self.reverse(nums,l,r)
        # next reverse the first k elements of the list
        l,r = 0,k-1
        self.reverse(nums,l,r)
        
        # finally reverse the last n-k elements of the list
        l,r = k,n-1
        self.reverse(nums,l,r)