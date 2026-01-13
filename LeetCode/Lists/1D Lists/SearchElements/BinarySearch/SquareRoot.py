# Time: O(logN)
#   Binary search halves the search space (range of numbers) to determine the square root of a given number
# Space: O(1) this algorithm uses no additional space
class Solution:
    # Algorithm: Here we use the entire range of numbers from 0 to x, we use binary search to determine the correct root.
    def mySqrt1(self, x: int) -> int:
        left = 0
        right = x
        while left <= right:
            mid = (right+left)//2
            if mid*mid == x:
                return mid
            elif mid*mid < x:
                left = mid + 1
            else:
                right = mid-1
        return right
    
    # Algorithm: here mathematical optimizations are made to further reduce the search space. 
    #   We can mathematically determine that any input less than 2 can return the given input
    #   Any input greater than to 2 will require a search space from 2 to half of the input. 
    #   We know that we can use half the input as the upper bound because of the math proof:
    #   for x≥4: sqrt(x)≤x/2​

    def mySqrt2(self, x:int) -> int:
        if x < 2:
            return x
        left = 2, right = x//2
        while left <= right:
            mid = (right+left)//2
            num = mid*mid
            if num == x:
                return mid
            elif num < x:
                left = mid + 1
            else:
                right = mid - 1
        return right