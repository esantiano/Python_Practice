# Time O(m+n) m and n are the number of elements in nums1 and nums2
# Space O(m+n) worst case is all elements in nums1 and nums2 are unique
# Algorithm: 
# we'll check the elements in nums1 and nums2 and place them in a set
# if there are elements in both we will remove the element from seen and place it in an output list
class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        output = []
        seen = set()
        for num in nums1:
            seen.add(num)
        for num in nums2:
            if num in seen and num not in output:
                output.append(num)
        return output
    
# Time O(m+n) m and n are the number of elements in nums1 and nums2
# Space O(m+n) worst case is all elements in nums1 and nums2 are unique
# Algorithm: place each list within its own set
# use a helper method to return the list of elements within both sets
# the helper method iterates over elements in the smaller set and checks the larger set for the element
class Solution2:
    def return_intersection_list(self, set1, set2):
        return [num for num in set1 if num in set2]
    
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        set1 = set(nums1)
        set2 = set(nums2)

        if len(set1) < len(set2):
            return self.return_intersection_list(set2,set1)
        else:
            return self.return_intersection_list(set1,set2)