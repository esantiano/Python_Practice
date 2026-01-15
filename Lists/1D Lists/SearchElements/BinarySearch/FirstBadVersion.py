# Time: O(logN)
#   Given N we use binary search to find the first bad version by reducing the search space per iteration.
# Space: O(1)
#   We use no extra space 
# Algorithm:
#   The search space is defined to be 1 and N
#   We set the termination of the loop to be when the boundaries of the search space are equal
#   The mid point is calculated using an over flow defensive calculation
#   We use the given API to determine if the midpoint value is a bad version or is not
#   dependent on the API result we move the boundaries of the search space
#   if the API returns False we know that all versions before the midpoint version are False(good versions)
#   if the API returns True we know that all the versions after the midpoint version are True(bad versions)
#   Finally when the search space is reduced to a single version we can check that version and depending on the result return that version number
#   The space will always reduce to the first bad version.

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            mid = (right-left)//2 + left
            if isBadVersion(mid) == False:
                left = mid + 1
            else:
                right = mid 
        
        if isBadVersion(left) == True:
            return left