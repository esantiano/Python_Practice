# we process elements and change direction until we leave the bounds of the matrix
# when we do leave the bounds we need to reset them and change direction
# - - - - -
# - 1 2 3 -
# - 4 5 6 - 
# - 7 8 9 - 
# - - - - -
class Solution:
    def diagonalTraverse(self, mat: list[list[int]]):
        rows = len(mat)
        cols = len(mat[0])

        res = []

        cur_row = cur_col = 0

        going_up = True

        while len(res) != rows * cols:
            if going_up:
                while cur_row >= 0 and cur_col < cols: # condition that drives this loop is before first row and before last column
                    res.append(mat[cur_row][cur_col])
                    cur_row -= 1
                    cur_col += 1
                if cur_col == cols: # this is an edge case check where we hit the boundary of the columns, this is for the case when we hit the longest up diagonal and afterwards, the column will be one outside of the boundary and the row will be one outside of the boundary
                    cur_col -= 1 # we reset the column back to the last column within the boundary
                    cur_row += 2 # we move the row down two rows 
                else: # this case is where we haven't yet hit the longest up diagonal but the row is out of bounds 
                    cur_row += 1 # reset the row from -1 to 0
                going_up = False # change the direction to down
            else:
                while cur_row < rows and cur_col >= 0: # condition that drives this loop is before last row and before first column
                    res.append(mat[cur_row][cur_col])
                    cur_row += 1
                    cur_col -= 1
                if cur_row == rows: # going down we handle the case where the column is out of bounds first
                    cur_col += 2 # we reset the col back to within the column boundary
                    cur_row -= 1 # we also reset the row back to within the boundary
                else: # this case handles before we hit the longest up diagonal, the pointer for the col will go out of bounds before the row pointer
                    cur_col += 1
                going_up = True
        return res
