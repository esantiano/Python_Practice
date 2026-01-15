# Time O(m+n) - we iterate through each list 
# Space O(min(m,n)) - m and n are lengths of the two lists, we store counts of elements in the shorter list 
# Algorithm:
# use a map to store the counts of each element in the shorter list
# iterate through longer list 
# for each element in long list and map reduce the count in map and add element to output list
# return the output list
class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # there is a simpler way to do this, we can just swap the pointers for nums1 and nums2 and assume that nums1 is shorter, see below
        m = len(nums1)
        n = len(nums2)
        count = {}
        short = long = None
        if m <= n:
            short = nums1
            long = nums2
        else:
            short = nums2
            long = nums1

        for num in short:
            if num in count:
                count[num]+=1
            else:
                count[num]=1
        result = []
        for num in long:
            if num in count and count[num]>0:
                result.append(num)
                count[num]-=1
                if count[num] == 0:
                    del count[num]
        return result
    
    def intersect2(self, nums1: list[int], nums2: list[int]) -> list[int]:
        if len(nums1) > len(nums2):
            return self.intersect2(nums2,nums1)
        count = {}
        
        # assume that nums1 is the shorter list
        for num in nums1:
            if num in count:
                count[num]+=1
            else:
                count[num]=1
        result = []
        for num in nums2:
            if num in count and count[num]>0:
                result.append(num)
                count[num]-=1
                if count[num] == 0:
                    del count[num]
        return result
        