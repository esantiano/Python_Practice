# Time: O(NLogN) - first we heapify the start times O(N). Then we extract the start times O(logN). Extract end times and push end times onto the heap O(logN)
# Space: O(N) - we use two heaps for the start and end times. 
# Algorithm: 
#   First we sort intervals according to start times.
#   Then we iterate through the sorted start times
#   We allocate rooms based according to the end time heap
#   If a room is available we can remove the end time from the heap otherwise we assign a new room
#   We will need to add meeting end times to the end time heap
#   Finally we return the number of rooms we need
# Notes: 
#   Intervals can be sorted in place if we don't care about modifying the input array - no extra space required
#   If we do care then we can create a min heap for the start times - will require extra space for the heap.
#   The min heap used for the end times lets us determine the next available room since the min heap will keep track of the minimum value end time.
#   Another way this can be done is by returning the length of the min heap of end times since this corresponds to the number of rooms we will need to use.
from typing import List
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = [(s,e) for s,e in intervals]
        end = []
        heapq.heapify(start)
        rooms = 0
        while start:
            start_time,end_time = heapq.heappop(start)
            if not end or end[0] > start_time:
                rooms+=1
            else:
                heapq.heappop(end)
            heapq.heappush(end,end_time)
        return rooms