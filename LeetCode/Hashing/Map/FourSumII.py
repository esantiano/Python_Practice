# Time: O(n^2) - two nested loop passes are used here, we use nested loops to get all sums from nums1+nums2 and nums3+nums4 
# Space: O(n^2) - where n the number of elements in each list. we store sums from nums1+nums2 in a map. at worst there will be n^2 unique solutions
# Algorithm: nums1[i] + nums2[j] + nums3[k] + nums4[l] = 0 we must find combinations to satisfy this condition so we set nums1[i] + nums2[j] = -(nums3[k] + nums4[l]). The first loop will find and count sums from the left side of the equation. The second loop will search through the map for the counts of the sum on the right side of the equation and add that number to the result. 
from typing import List
import collections
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        sum_counts = collections.defaultdict(int)
        result = 0
        for n1 in nums1:
            for n2 in nums2:
                s=n1+n2
                sum_counts[s]+=1
        for n3 in nums3:
            for n4 in nums4:
                s=-1*(n3+n4)
                if s in sum_counts:
                    result+=sum_counts[s]
        return result
        