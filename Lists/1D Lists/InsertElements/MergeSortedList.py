# Time O((m+n)^2) - the worst case is that all the elements in nums2 are smaller than the first element in nums1 which would require that all the elements be shifted
# O(m)+O(m+1)+O(m+2)+⋯+O(m+n−1)=O((m+n)2)
# Space O(1) - in place 
# practice inserting elements in place
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = 0, 0
        max_i = m # the current number of valid elements inside nums1
        while i < max_i and j < n:
            if nums2[j] < nums1[i]: # we've found an insertion 
                for k in range(len(nums1)-1,i,-1): # shift all elements in nums1 right 1 index
                    nums1[k] = nums1[k-1]
                nums1[i] = nums2[j] # insert the element from nums2 into nums1
                j+=1 # update the index for nums 2 
                max_i+=1 # update the maximum for the elements in nums1
            i+=1

        if j<n: # if there are remaining elements in nums2 then insert the remainder into nums1 starting from the index next to the last filled index in nums1
            nums1[i:] = nums2[j:]
sol = Solution()
print(sol.merge([1,2,3,0,0,0],3,[2,5,6],3))