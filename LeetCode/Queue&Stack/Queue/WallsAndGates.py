# use a deque: standard used for BFS, collections.deque provides O(1) time complexity for both appending elements to the end (append()) and removing elements from the front (popleft()).
# queue rooms that are gates first 
# process the queue
# check the neigboring rooms for open rooms 
# we need to determine the directions to check: up, down, left, right 
# we also need to make sure the potential rooms are within bounds
# get a step value from the current room 
# if we have an open room then we assign the step distance which is the current step value + 1
# then we queue the open room and repeat the process 

# Time O(mn) - there are m*n rooms to check 
# Space same as time there will be at most m*n rooms in the queue
import collections
from typing import List

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        In the input matrix:
        0 means a Gate
        -1 means a Wall
        2147483647 (or float('inf')) means an empty room
        """
        if not rooms or not rooms[0]:
            return

        m, n = len(rooms), len(rooms[0])
        q = collections.deque()
        
        # 1. Queue all gates
        for r in range(m):
            for c in range(n):
                if rooms[r][c] == 0:
                    q.append((r, c))
        
        # Define directions: (up, down, left, right) its easier to do it this way than to check i-1,i+1,j-1,j+1 
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # 2. Process rooms
        while q:
            row, col = q.popleft()
            current_distance = rooms[row][col]  # The rooms that are queued initially are gates, current distance = 0 
            # 3. Queue neighbors
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                # 4. Check boundaries
                if 0 <= new_row < m and 0 <= new_col < n:
                    # If neighbor is an unvisited open room (inf), assign step value and queue
                    if rooms[new_row][new_col] == 2147483647:
                        rooms[new_row][new_col] = current_distance + 1
                        q.append((new_row, new_col)) # queue the room in order to check its neighbors 
        return rooms 
