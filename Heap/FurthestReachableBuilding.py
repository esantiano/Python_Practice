from typing import List
import heapq
class Solution:
# Time:O(NlogN) or O(NlogL)
#   consider that we are given L ladders 
#   To iterate through heights O(N) 
#   To add or remove from the heap O(logL) possibly performed N times 
# Space: O(N) or O(L) 
#   Space required for the heap 
# Algorithm:
#   create a min heap for ladders
#   iterate through heights
#   get the height difference between the next and current buildings
#   if the difference is less than or equal to zero we can continue to the next iteration
#   add the difference to the ladders heap
#   check the heap to make sure we haven't used more ladders than we have available and continue on to the next iteration
#   if we have used more ladders than available then we can instead use bricks and free a ladder from the heap
#   check to see that we haven't used more bricks than available
#   if we have then we have gotten to the furthest building we can
#   if we have iterated through all the heights then we can say we reached all buildings
    def furthestBuildingMinHeap(self, heights: List[int], bricks: int, ladders: int) -> int:
        ladders_allocated = []
        
        for i in range(len(heights)-1):
            diff = heights[i+1] - heights[i]
            if diff <= 0:
                continue

            heapq.heappush(ladders_allocated, diff)
            if len(ladders_allocated) <= ladders:
                continue
            
            bricks -= heapq.heappop(ladders_allocated)
            if bricks < 0:
                return i

        return len(heights)-1
# Time: O(NlogN)
#   O(N) required to iterate through heights
#   O(logN) required to add or remove from bricks heap
# Space: O(N)
#   Space required for the heap
# Algorithm: 
#   create a max heap for the bricks to allocate
#   track the bricks we have used
#   iterate through heights
#   calc the difference between next and current building
#   if less than or equal to zero we continue to the next iteration
#   if we can't continue:
#   add the negative difference to the bricks heap
#   add the difference to the bricks used 
#   check to make sure we haven't used more bricks than allocated and continue to the next iteration
#   if we can't continue
#   remove the top element from the bricks heap
#   subtract the top element from bricks used
#   decrement the number of ladders available 
#   check to see if we have used all ladders and return the current index if we have
#   return the last index of heights if iterated the entire list
    def furthestBuildingMaxHeap(self, heights: List[int], bricks: int, ladders: int) -> int:
        bricks_allocated = []
        bricks_used = 0

        for i in range(len(heights)-1):
            diff = heights[i+1]-heights[i]
            if diff <= 0:
                continue
            
            heapq.heappush(bricks_allocated,-diff)
            bricks_used+=diff
            if bricks_used <= bricks:
                continue
            
            bricks_gained = -heapq.heappop(bricks_allocated)
            bricks_used -= bricks_gained
            ladders -=1
            
            if ladders < 0:
                return i
        
        return len(heights)-1