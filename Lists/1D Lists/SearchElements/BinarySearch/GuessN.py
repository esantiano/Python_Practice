# Time: O(logN) we use binary search to cut the search space in half after every comparison
# Space: O(1) no extra space is used
# Algorithm: establish a search space, use binary search to guess the number and return the number when found.
# Notes: Algorithm 1 uses a a way to calculate the mid point that is prone to index overflow, algorithm 2 does not. 
#        Algorithm 2 guarantees loop termination
import math
class Solution:
    def __init__(self):
        self.y = math.random()
    def guess(self,x):
        if x == self.y:
            return 0
        elif x > self.y:
            return -1
        else:
            return 1
        
    def guessNumber1(self, n: int) -> int: 
        left = 1 
        right = n 
        while left <= right: 
            pick = (right+left)//2 
            result = self.guess(pick) 
            if result == 0: return pick 
            elif result == -1: right = pick-1 
            else: left = pick+1

    def guessNumber2(self, n: int) -> int:
        left = 1
        right = n
        
        while left < right:
            pick = (right-left)//2 + left
            result = self.guess(pick)
            if result == 0:
                return pick
            elif result == -1:
                right = pick-1
            else:
                left = pick+1
        return right