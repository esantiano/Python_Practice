# Time O(m+n) 
# Space O(1)
# strategy iterating backwards: 
# since each list is already sorted in non decreasing order 
# and nums1 has allocated extra space for all elements in num2 
# we can fill in nums1 starting from the end 
# 3 pointer technique with two pointers used to compare the values in nums1 and nums2 
# and a third pointer to write the values at the end of nums1 

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m-1 
        j = n-1
        
        for w in range(n+m-1,-1,-1): # m = number of values in nums1 and n = number of values in nums2 so total length should be n+m
            if j < 0: # this check is if nums2 is empty or we've come to the end of nums2 
                break
            if i >= 0 and nums1[i]>nums2[j]: # check to see if we are still in bounces with nums1 and comparison check 
                nums1[w] = nums1[i]
                i-=1
            else: # implied comparison check or seeing that there are still values in nums2 
                nums1[w] = nums2[j]
                j-=1
sol = Solution()
print(sol.merge([1,2,3,0,0,0],3,[2,5,6],3))