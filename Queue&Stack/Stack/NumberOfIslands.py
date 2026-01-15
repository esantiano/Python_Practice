# Time: O(m*n) the time it takes to iterate through each cell
# Space: O(m*n) the amount of space used on the callstack
# Algorithm: 
# we iterate through the grid in a linear manner
# when we encounter a 1 we trigger the DFS first to set all its neighbors to 0 and then increment the number of islands
# the DFS should just set the visited nodes and its neighbors to 0, the stack used here is the call stack
# the DFS stops if we are out of index or if we encounter a 0
# then return the count of islands
from typing import List
class Solution:
    def DFS(self,row,col,grid):
        r = len(grid)
        c = len(grid[0])
        if row < 0 or col < 0 or row >= r or col >= c or grid[row][col] != "1":
            return
        grid[row][col] = "0"
        self.DFS(row-1,col,grid)
        self.DFS(row+1,col,grid)
        self.DFS(row,col-1,grid)
        self.DFS(row,col+1,grid)

    def numIslands(self, grid: List[List[str]]) -> int:
        islands=0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    self.DFS(row,col,grid)
                    islands +=1
        return islands