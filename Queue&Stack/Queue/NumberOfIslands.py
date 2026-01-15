
# Time complexity : O(M×N) where M is the number of rows and
# N is the number of columns.
# Space complexity : O(min(M,N)) because in worst case where the
# grid is filled with lands, the size of queue can grow up to min(M,N).

# Algorithm: 
# use a count to keep track of islands
# check each cell in the grid: this is accomplished with a linear scan, we will check each cell in the grid
# if the cell is an island: 
# increment the count 
# flip the value
# use a deque to keep track of the cells to check
# queue the current cell
# queue neighbors: use a for loop and a list of directions to check LRDU
# flip any neighbor that is an island so it doesn't increment the count, add that neighbor to the queue

import collections
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        m,n = len(grid),len(grid[0])
        
        for row in range(m):
            for col in range(n):
                if grid[row][col] == "1":
                    count +=1 
                    grid[row][col] = "0"
                    neighbors = collections.deque([(row,col)])
                    while neighbors:
                        cur_row,cur_col = neighbors.popleft()
                        directions = [(-1,0),(1,0),(0,-1),(0,1)]
                        for r,c in directions:
                            n_row = cur_row+r
                            n_col = cur_col+c
                            if 0<=n_row<m and 0<=n_col<n and grid[n_row][n_col]=="1":
                                neighbors.append((n_row,n_col))
                                grid[n_row][n_col] = "0"
        return count
            