# Time: O(logN) binary search time required
# Space: O(1) no extra space used
# Algorithm: We can use binary search to determine whether or not s perfect square for num exists.
#   We set the boundarys between 0 and num (we do this to account for nums < 4)
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        L, R = 0, num
        while L < R:
            M = L + (R-L)//2
            sq = M*M
            if sq == num:
                return True
            elif sq > num:
                R = M
            else:
                L = M+1
        return L*L == num
        
        