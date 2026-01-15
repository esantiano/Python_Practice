# Time: O(NlogN)
#   We use O(logN) time to heapify a list of negative elements in stones,
#   remove elements from the heap, and add elements onto the heap
#   O(N) time is required to iterate through the list
# Space: O(N)
#   We use O(N) space for the heap
# Algorithm:
#   We heapify the stones list using a max heap
#   we iterate throught the heap until we have either 1 or 0 elements inside the heap
#   during iteration we remove the first two elements in the heap and compare them
#   if they are not equal we place the difference between the elements inside the heap
#   after iteration, we return the remaining element in the heap or 0
from typing import List
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stone_heap = [-stone for stone in stones]
        
        heapq.heapify(stone_heap)
        
        while len(stone_heap)>1:
            y = -heapq.heappop(stone_heap)
            x = -heapq.heappop(stone_heap)
            if x != y:
                result = y-x
                heapq.heappush(stone_heap,-result)
        
        return 0 if not stone_heap else -stone_heap[0]