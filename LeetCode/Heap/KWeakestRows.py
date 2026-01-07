# Time: O(MlogNK)
#   O(M) time is required to iterate through each row in the matrix
#   for each row we use binary search to detemine the rows strength O(logN) 
#   and O(logK) time to place a tuple of the strength and row index in a max heap of size K
# Space: O(K)
#   We use a heap of size K to store the top K weakest rows
# Algorithm:
#   We iterate through each row and use binary search to determine the strength of each row.
#   Once we determine the strength we create a tuple of the strength and row index to insert into a max heap
#   the max heap will only allow the top K tuples from the result of the enumeration of mat and binary search for each row.
#   Once the entire matrix has been iterated and the top K tuples determined we unpack the max heap.
#   We will return the reversed and normalized result of the unpacked max heap.
from typing import List
import heapq
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        n = len(mat[0])
        def bin_search(row):
            low = 0
            high = n
            while low < high:
                mid = low + (high - low) // 2
                if row[mid] == 1:
                    low = mid + 1
                else:
                    high = mid
            return low
        
        max_heap = []
        for i,row in enumerate(mat):
            strength = bin_search(row)
            entry = (-strength,-i)
            if len(max_heap) < k or entry > max_heap[0]: # the comparison happening between entry and max_heap[0] is based on lexicographical ordering. We compare both elements inside entry and use the last element in entry as a tie breaker.
                heapq.heappush(max_heap,entry)
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        indexes = []
        while max_heap:
            strength,i = heapq.heappop(max_heap)
            indexes.append(-i)
        
        indexes = indexes[::-1]
        return indexes
            
            
        