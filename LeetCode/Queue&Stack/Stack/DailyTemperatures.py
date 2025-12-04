
# Notes: The brute force method is straightforward two for loops is easy, look at a temperature and then compare all the future temperatures until we find a warmer one. 
# Building off the brute force solution: we can "delay" finding the answer for the first x days, and upon finding a warmer temperature, we can move backward to find the answer for all x days at the same time. This process of storing elements and then walking back through them matches the behavior of a stack.

# Time: O(N) Looks like N^2 but consider the fact that each element only gets pushed and popped onto the stack once. We iterate in the outer loop once and in the while loop we backfill the output. 
# Space: O(N) We use a stack to hold all the elements which will at worst be all the elements.

# Algorithm: In this approach we use a stack to hold the "days" of the cooler temperatures until we find a warmer temperature, once we find a warmer temperature we index differences between the days wihin the output list.
from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        output = [0]*n
        s = []
        for curDay,curTemp in enumerate(temperatures):
            while s and curTemp > temperatures[s[-1]]:
                prevDay = s.pop()
                output[prevDay] = curDay-prevDay
            s.append(curDay)  
        return output
            