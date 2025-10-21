class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        
        res = []
        
        level = 0 #start at the outer most layer of the spiral
        # my original code - each while loop does not account for checking the len of result 
        # while len(res) < rows*cols:
        #     c_row = c_col = level
        #     while c_col <= cols - level - 1: # top row move right
        #         res.append(matrix[c_row][c_col])
        #         c_col += 1
            
        #     if c_col > cols - level - 1: # reset the c_col pointer 
        #         c_col -= 1
                
        #     while c_row < rows - level - 1: # right-most col move down
        #         c_row += 1
        #         res.append(matrix[c_row][c_col])
                
            
        #     if c_row == rows - level - 1: # we are at the outermost bottom layer     # fails once it gets to this point 
        #         c_col -= 1
        #         while c_col >= level: # move left
        #             res.append(matrix[c_row][c_col])
        #             c_col -= 1
        #         # we have hit outermost layer on the left side 
        #         c_col += 1 # reset the c_col pointer to in bounds 
        #         c_row -= 1
                
        #         while c_row > level: # left-most col move up
        #             res.append(matrix[c_row][c_col])
        #             c_row -= 1
                    
        #     level += 1 # move into the next layer of the spiral
            
        while len(res) < rows * cols:
            c_row = c_col = level

            # ✅ Top row — move right
            while c_col < cols - level and len(res) < rows * cols:
                res.append(matrix[c_row][c_col])
                c_col += 1
            c_col -= 1  # step back to last valid column

            # ✅ Right-most column — move down
            while c_row + 1 < rows - level and len(res) < rows * cols:
                c_row += 1
                res.append(matrix[c_row][c_col])

            # ✅ Bottom row — move left (only if we’re not on same row)
            while c_col - 1 >= level and len(res) < rows * cols and rows - level - 1 != level:
                c_col -= 1
                res.append(matrix[c_row][c_col])

            # ✅ Left-most column — move up (only if we’re not on same col)
            while c_row - 1 > level and len(res) < rows * cols and cols - level - 1 != level:
                c_row -= 1
                res.append(matrix[c_row][c_col])

            level += 1  # move into the next layer of the spiral
        return res
sol = Solution()
res = sol.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(res)
res = sol.spiralOrder([[1,2,3],[4,5,6],[7,8,9]])
print(res)

# in this iteration of spiralOrder we set the boundaries using top, bottom, left and right thing of a square/rectangle that shrinks as we move along the spiral
class Solution2:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        rows = len(matrix)
        cols = len(matrix[0])

        top = left = 0 
        bottom = rows - 1 
        right = cols - 1 

        res = []

        while len(res) < rows * cols:
            # topmost row 
            for col in range(left, right +1):
                res.append(matrix[top][col])
            # rightmost column
            for row in range(top + 1, bottom +1):
                res.append(matrix[row][right])
            
            # check to make sure that we still have row elements to grab and reverse direction
            if top != bottom:
                # bottommost row
                for col in range(right-1, left-1, -1):
                    res.append(matrix[bottom][col])
            # check to make sure we have column elements to grab and reverse direction
            if left != right: 
                # leftmost column
                for row in range (bottom-1, top, -1):
                    res.append(matrix[row][left])
            
            # increment and decrement the layers:
            top += 1
            left += 1 
            bottom -= 1
            right -=1 
        return res

sol2 = Solution2()
res = sol2.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(res)
res = sol2.spiralOrder([[1,2,3],[4,5,6],[7,8,9]])
print(res)