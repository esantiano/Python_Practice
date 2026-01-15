# Time O(n) - we only need to loop through the list once
# Space O(1) - we only use 3 extra variables
# Three pointer practice
# edge cases nums = [1] returns 1 since its the only element in nums
# nums = [1,100000] returns 100000 max element
# nums = [1,2,2] returns 2 max element
# use 3 variables to hold first 3 distinct maxes 
# loop through nums to find 3 dist els
# 3 els need to be first 3 max els, and distinct
# bump each max down to the next variable until we have 3 or until we reach end of list
# return them in bottom up order 
class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        first = second = third = float('-inf') # follow up instead of using float('-inf') we can use a pair of int and bool (-1,false) to keep track of when the variable was updated
        for num in nums:
            if num == first or num == second or num == third: # check for a distinct number, alt: check if first, second, and third have been updated first[1] and first[0] != num
                continue
            if num > first: # alt check if first[1] and num > first[0]
                third = second
                second = first
                first = num # alt set first[1] to true
            elif num >= second: # alt check for second
                    third = second
                    second = num # alt set second[1] to true
            elif num >= third: # alt check for third
                third = num # alt set third[1] to true
        
        if third == float('-inf'): # alt check for third[1]
            return first
        
        return third
        
        