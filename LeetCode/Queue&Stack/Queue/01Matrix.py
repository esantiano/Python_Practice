# Time: O(mxn) - m - number of rows, n - number of columns, we iterate over each cell in the grid at most once. 
# Space O(mxn) - we use a copy of the original matrix and modify that, we also use that amount of space in the deque for each cell

# Algorithm:
# BFS approach, given a 01 matrix we want to find the shortest path from each 0. 
# We can do this easily by creating a queue of cells that are already 0 and spreading out from there. 
# We use a set to make sure that we don't modify any cells that are 0 or have been modified already
# Create a copy of the given matrix
# iterate through the rows and columns of the matrix, queing zero value cells and the current steps away from those cells ( 0 in this case ) and adding the cells to the set
# iterate through the queue
# remove the first value in the queue ( from the front ), this should be a row, col, and number of steps  -> shortest path, BFS
# check to make sure the neighbors of the cell are in bounds and not in the set
# upate the neighbor cell value equal to the inrecemented number of steps away from 0. 
# add neigboors of the cell and their incremented number of steps away from 0 to the queue
# add the neighbor cell to the set to ensure it isn't visited again

from collections import deque
from typing import List
class SolutionBFS:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        matrix = [row[:] for row in mat]
        
        m = len(matrix)
        n = len(matrix[0])
        
        q = deque()
        seen = set()

        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    q.append((row,col,0))
                    seen.add((row,col))
        
        neighbors = [(1,0),(-1,0),(0,-1),(0,1)]
        while q:
            r,c,step = q.popleft()
            for dr,dc in neighbors:
                nr = r+dr
                nc = c+dc
                if (nr,nc) not in seen and 0<=nr<m and 0<=nc<n:
                    matrix[nr][nc] = step +1
                    q.append((nr,nc,step+1))
                    seen.add((nr,nc))
        
        return matrix
                    