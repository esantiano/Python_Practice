# Time: O(N + Nlogk) if k < N and O(1) if k == N where N is the number of elements in the list. We must count the frequencies of each element in the list and then sort the map 
# Space: O(N+K) we must store N elements in the map and a list of k elements
from typing import List
import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # we should include this check as well 
        if k == len(nums):
            return nums
        num_count = collections.Counter()
        for num in nums: # this can be replaced by num_count = collections.Counter(nums)
            num_count[num]+=1
        sorted_num_count=sorted(num_count, key=num_count.get, reverse=True)
        return list(sorted_num_count)[:k]