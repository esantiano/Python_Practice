# Time: O(NlogK)
#   O(N) time is used to create the hashmap for the frequencey counts
#   O(logK) time is used to heapify the hashmap for the top K frequent values
# Space: O(N + K) 
#   we use a hashmap to store the counts for all values in nums
#   we use a heap to store the top K frequent values 
# Algorithm:
#   First we create a hashmap of the values in nums and their frequencies
#   Then we heapify the hashmap: we store an object of a values frequency and value within a min heap
#   Finally we can return a list of the values from the min heap
# Note:
#   getting the hashmap and heap can be done using count and nlargest functions from python
import heapq
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for num in nums:
            if num not in hashmap:
                hashmap[num]=1
            else:
                hashmap[num]+=1
        
        min_heap = []
        heapq.heapify(min_heap)

        for num,count in hashmap.items():
            if len(min_heap) < k:
                heapq.heappush(min_heap,(count,num))
            else:
                if min_heap[0][0] < count:
                    heapq.heapreplace(min_heap,(count,num))
        
        return [num for count,num in min_heap]