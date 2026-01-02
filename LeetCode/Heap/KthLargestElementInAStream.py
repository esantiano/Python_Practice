# Time: O((M+N)logK) 
#   In this implementation we call add N times for the given intial list nums
#   Add is called M times 
#   To add any value to the heap of size K requires O(logK) time
# Space: O(K)
#   The space required to hold K values in the min heap
# Design:
#   For Add we want to check that the heap has the space to add additional values 
#   or if the top value on the heap (kth value) is smaller than the current value before adding
#   Additionally we want to remove any extra values from the heap if its size exceeds k.
#   The top value on the heap is the kth value.

from typing import List
import heapq
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = []
        
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.min_heap) < self.k or self.min_heap[0] < val:
            heapq.heappush(self.min_heap,val)
            if len(self.min_heap) > self.k:
                heapq.heappop(self.min_heap)
        return self.min_heap[0]