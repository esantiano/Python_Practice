# Time: O(n) - top down memoization, each value of n is calculated once and stored 
# Space O(n) - used to store the number of solutions per given n 
# Algorithm: Same as Fibonacci Number except we change our base cases, n will never be 0
# cache to memorize solutions for the given n 
# check the cache and return a cache value 
# store the recursive call solution for given n in cache
# return the recursive solution for given n from cache 
class Solution:
    cache = {0:1,1:1,2:2}
    def climbStairs(self, n: int) -> int:
        if n in self.cache:
            return self.cache[n]
        self.cache[n] = self.climbStairs(n-1)+self.climbStairs(n-2)
        return self.cache[n]