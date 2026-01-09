# Time: O(NlogN)
#   O(NlogN) time is used to add elements from sticks to a min heap
#   O(logN) time is also used to remove and add to the heap (N-1) add and remove operations are performed because we only want one element in the heap
# Space: O(N)
#   We require O(N) space for the heap since it will hold all values from sticks
# Algorithm:
#   First we heapify sticks
#   Then while there are at least 2 elements in the heap
#   we will take the first two elements on top of the heap and add them together
#   we will increment the cost of adding the two elements 
#   we will then place the result back into the heap and repeat the process
# Notes:
#   Greedy approach, we always pick two of the smallest sticks until we are left with one stick.
#   The sticks that are picked first are repeatedly used in the cost calculation.
#   Therefore we will want to pick the smallest first and the largest last.
from typing import List
import heapq
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        min_heap = sticks
        heapq.heapify(min_heap)

        cost = 0
        while len(min_heap)>=2:
            a = heapq.heappop(min_heap)
            b = heapq.heappop(min_heap)
            c = a + b
            cost += c
            heapq.heappush(min_heap,c)

        return cost