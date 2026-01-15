# Time O(2^k) - where k is the rowIndex. 
# based on recurrence theorem 
# where k is the number of calls we need to make 
# in order to reach the base cases in our getElement function

# Space O(k) - where k is the row index, we need O(k) space to store that row
# the worst case also O(k) also accounts for the space needed to make the recursive calls

# Algorithm: 
# we use a function to generate elements for the given row
# we use an output list to store the elements 
# in order to fill the output list we must make multiple calls to generate the elements 
# we do this per column in the given row. Each row containss row+1 columns

class Solution:
    def getElement(self, i, j):
        if i==0 or j == 0 or i == j: # we index from 0, j is the column index, i is the row index, this is our base case 
            return 1 # the top row and sides of each row are 1's
        return self.getElement(i-1,j-1)+self.getElement(i-1,j) # we call the function again until we reach the base cases
    
    def getRow(self, rowIndex: int) -> list[int]:
        output = [] # we use an output list to store each element
        for i in range(rowIndex+1):
            output.append(self.getElement(rowIndex,i)) # we start building the output from the leftside
        return output 

# the solution above takes too much time when trying to generate later rows 
# One work around is to use a cache, (map or dict) to memorize solutions for some of the recursive calls 
# Time O(k^2) - Reduced time complexity because we can check the dict for the memoized calculations
# Space O(k) - same amount of space needed to store the kth ro
    def getRowOptimized(self, rowIndex: int) -> list[int]:
        cache={} #decorator
        def getElement(self, i, j):
            if (i,j) in cache:
                return cache[(i,j)]
            if i==0 or j == 0 or i == j: # base case
                return 1 
            
            colVal = self.getElement(i-1,j-1)+self.getElement(i-1,j) # store the returned value in a variable
            cache[(i,j)]=colVal # memoize the returned value
            return colVal
        output = [] # we use an output list to store each element
        for i in range(rowIndex+1):
            output.append(self.getElement(rowIndex,i)) # we start building the output from the leftside
        return output