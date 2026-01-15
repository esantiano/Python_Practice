# this is a dynamic programming problem as each new row builds off the previous row
# we must start with an initial row [1] inside our result list since the constraint is 1 <= numRows <=30
class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        # start with [[1]]
        result = [[1]]
        for i in range(1,numRows): # since we start with [1] in result we only need to look at the range (1 (inclusive), numsRows (exclusive))
            prev = result[-1] # grab the previous row 
            new = [1] # we always start the new row with 1 
            for j in range(len(prev)-1): # exclude the last item in the previous row (1)
                new.append(prev[j] + prev[j+1]) # we add the current item in previos row to the next item in the previous row
            new.append(1) # we always end the new row with 1
            result.append(new) # add the new row to the result
        return result
sol = Solution()
result = sol.generate(8)
print(result)    
