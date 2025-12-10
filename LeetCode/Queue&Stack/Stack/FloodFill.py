# Time: O(mxn) - at worst we'll need to go through every cell in the grid m-rows n-cols
# Space: 0(mxn) - we may need mxn space on the stack and set for each cell
# Algorithm: 
# we'll use a stack to keep track of the cells to process 
# we'll use a set to keep track of the cells we've already seen
# from the given cell we'll store the color 
# we'll add the position (sr,sc) to the stack to process, we'll also add the position to the set
# iterate on the stack
# first remove the first element within the stack
# then check the value of the cell to see if it matches the color we've stored
# if it does then we'll change it to the given color 
# then we will add its neighbors (top, bottom, left, right)
# we will only add neighbors to the stack if they are within the bounds of the grid
from typing import List
class SolutionIterative:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        q = []
        seen = set()
        
        seen.add((sr,sc))
        q.append((sr,sc))
        
        old_val = image[sr][sc]
        neighbors = [(-1,0),(1,0),(0,-1),(0,1)]
        while q:
            r,c = q.pop()
            if image[r][c] == old_val:
                image[r][c] = color
                for r_d, c_d in neighbors:
                    n_r = r + r_d
                    n_c = c + c_d
                    if 0 <= n_r < len(image) and 0 <= n_c < len(image[0]) and (n_r,n_c) not in seen:
                        q.append((n_r,n_c))
                        seen.add((n_r,n_c))
        return image

# same space and time complexity for the same reasons just on an implicit call stack
# Algorith: 
# we'll use a global set, variable, and list of neighbors 
# we'll use a helper function to change the old values for the given sr, sc
# the base case is the given row and col are out of bounds or are within the set, we'll just return 
# if the cell value at the given row and col is equal to the old cell value then replace and recurse on its neighbors 

class SolutionRecursive:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        seen = set()
        old_val = image[sr][sc]
        neighbors = [(1,0),(-1,0),(0,-1),(0,1)]
        
        def DFS(r,c,image,seen,color):
            nonlocal old_val
            nonlocal neighbors
            if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]):
                return
            
            if image[r][c] == old_val:
                image[r][c] = color
                for dr,dc in neighbors:
                    if (r+dr,c+dc) not in seen:
                        seen.add((r+dr,c+dc))
                        DFS(r+dr,c+dc,image,seen,color)
        DFS(sr,sc,image,seen,color)
        return image