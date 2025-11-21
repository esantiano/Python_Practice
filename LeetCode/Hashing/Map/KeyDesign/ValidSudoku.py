# Time O(N^2) - we use two loops to iterate through values each row
# Space O(N^2) - worst case scenario is that the board is full
# keys: row, col, sub-box : set()
# we can skip cells with "."
# for every value we see we will check the corresponding row, column, and box
# if we see repeat numbers in any of the lists return false 

# For this 
# hashsets here are used to make sure the values seen in rows, columns, and sub boxes are unique. time complexity for checking sets is O(1)
# a hashmap is not strictly used here, instead we use lists to store sets time complexity list access is O(1)
# lists are used to keep track of the rows, columns and sub boxes
# rowkey: 0-8
# colkey: 0-8
# sub box key: 0-8

# the main issue here is determining which box a value gets sorted into, to determine this we can use the formula (r//3) * 3 + (c//3).
# why use * 3? think of the 9X9 grid as 3 horizontal bands, the first band starts at row 0, next band starts at row 3, and the last band starts at row 6. Determining the vertical bands for the columns can be done in a similar fashion. The multiplication by 3 is essential to translate the index of the vertical band back into the actual starting row coordinate in the larger 9x9 grid

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        N = 9
        rows = [set() for _ in range(N)]
        cols = [set() for _ in range(N)]
        boxes = [set() for _ in range(N)]
        
        for r in range(N): # go through each row
            for c in range(N): # go through each column
                val = board[r][c]
                if val == ".":
                    continue
                
                if val in rows[r]: # check the row
                    return False
                rows[r].add(val)

                if val in cols[c]: # check the column
                    return False
                cols[c].add(val)

                b = (r//3)*3+(c//3) # determine which subbox to check
                if val in boxes[b]: # check the sub box
                    return False
                boxes[b].add(val)

        return True
            
        