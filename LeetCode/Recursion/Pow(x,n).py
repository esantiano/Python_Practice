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
# Time O(logn) - each recursive call reduces n by hald 
# Space O(logn) - the recursive stack also uses the same amount of space 

# Algorithm: 
# The basic idea here is to use the fact that xn can be expressed as:
#    (x2)n/2 if n is even
#    x∗(x2)(n−1)/2 if n is odd (we separate out one x, then n−1 will become even)

    def myPowOptimized(self, x: float, n: int) -> float:
        def helper(x,n):
            if n==0:
                return 1
            if n < 0:
                return 1/helper(x,-1*n)
            
            if n%2==1 :
                return x*helper(x*x,(n-1)//2)
            else:
                return helper(x*x,n//2)        
        return helper(x,n)