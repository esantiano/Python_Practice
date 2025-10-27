# Time O(k^2) where k is = rowIndex
# Space O(k)
# Notes: This is a dynamic programming approach 
# Algorithm: we create a list with the alloted amount of space we need
# set the first column we need to modify in the first loop
# modify the set column and each column before it 
# we don't need to modify the first or last columns because they are equal to 1 
class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        # initialize row with all elements as 1 
        row = [1]*(rowIndex+1)
        # populate each row element
        for i in range(1,rowIndex+1):
            for j in range(i,0,-1):
                # current element is sum of current and previous element in above row
                row[j] += row[j-1]
        return row
    
# 0      1
# 1     1 1 
# 2    1 2 1   
# 3   1 3 3 1

# run through rowIndex = 3
# row = [1,1,1,1]
# i = 1, j = 1 row = [1,2,1,1]
# i = 2, j = 2 row = [1,2,3,1]
# i = 2, j = 1 row = [1,3,3,1]
# end loop return row