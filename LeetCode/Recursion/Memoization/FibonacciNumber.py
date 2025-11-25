# use a map to memorize the solution for a given n, make sure the base cases are already in there 
# use the generator function to generate the output 
# check the map first for a solution 
# make a recursive call to generate the solution for a given n
# store the solution in the map for the given n
# return the solution
# return the output of the call to the generator function
class Solution:
    def fib(self, n: int) -> int:
        cache = {0:0,1:1}
        def generateOutput(n):
            if n in cache:
                return cache[n]
            
            nSol = generateOutput(n-1) + generateOutput(n-2)
            cache[n]=nSol
            return nSol
        
        return generateOutput(n)
# the above can be done without the generator function, we can recusively call fib on n instead
    cache = {0:0,1:1}
    def fibOptimized(self,n):
        if n in self.cache:
            return self.cache[n]
        
        self.cache[n] = self.fibOptimized(n-1) + self.fibOptimized(n-2)
        return self.cache[n]
    