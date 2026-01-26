# base case check if n is 0 return 1
# return a recursive call on x and decremented n 



class Solution:
# The first approach here is naive,nothing is optimized and so is solved in linear time 
# There is also stack overflow ocurring here as well
    def myPow(self, x: float, n: int) -> float:
        def helper(x,n):
            if n==0:
                return 1
            if n < 0:
                return 1/helper(x,n+1)
            elif n > 0:
                return x*helper(x,n-1)        
        return helper(x,n)
# The optimized approach uses math to reduce the time and space complexity 
# Time O(logn) - each recursive call reduces n by half 
# Space O(logn) - the recursive stack also uses the same amount of space 

# Algorithm: 
# The basic idea here is to use the fact that xn can be expressed as:
#    (x2)n/2 if n is even
#    x∗(x2)(n−1)/2 if n is odd (we separate out one x, then n−1 will become even)

    def myPowRecursive(self, x: float, n: int) -> float:
        def helper(x,n):
            if n==0:
                return 1
            if n < 0:
                return 1/helper(x,-1*n)
            
            if n%2==1:
                return x*helper(x*x,(n-1)//2)
            else:
                return helper(x*x,n//2)        
        return helper(x,n)
# Algorithm:
#   The algorithm here uses the same conditions as the recursive above
#   we store and return the result within a variable.
#   if n is negative we flip the sign and set the base value to its reciprocal
#   then we iterate on n until it reaches 0 
#   we take advantage of some optimizations to reduce the number of iterations necessary
#   squaring the base and halving n with each iteration
#   if n is odd we use the result to keep track of an extra multiplication step with the base and reduce n by 1 
    def myPowIterative(self, x: float, n: int) -> float:
        def helper(x,n):
            if n == 0:
                return 1
            if n < 0:
                n*=-1
                x=1/x
            result = 1
            while n != 0:
                if n%2 == 1:
                    result*=x
                    n-=1
                x*=x
                n//=2
            return result
        return helper(x,n)