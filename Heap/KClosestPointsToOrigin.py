# Time: O(NlogK) 
#   We must iterate through points which requires O(N) time
#   O(logK) time is required to add and remove from the heap of size K
# Space: O(K) 
#   Space required for heap
# Algorithm:
#   We will iterate through points
#   calculate the distance between coordinates and origin
#   Add to the max heap if there is space (-dist, [coordinates])
#   If there is no space on the heap 
#   then we must compare the current distance and the distance on the top of the heap
#   and possibly replace the top of the heap
#   We can then deconstruct the heap into a coordinate list and return the result
from typing import List
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def calc_dist(x,y):
            return x*x+y*y
        closest = []
        for x,y in points:
            dist = calc_dist(x,y)
            if len(closest) < k:
                heapq.heappush(closest,(-dist,[x,y]))
            else:
                if closest[0][0] < -dist:
                    heapq.heapreplace(closest,(-dist,[x,y]))
        
        return [point for _,point in closest]