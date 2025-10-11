# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 0
        r = n
        m = 0
        while l<r:
            m = l + int((r-l)/2) # we calculate mid this way because left + right could overflow mathematically left+right/2 == left + (right-left)/2

            # check which half of the list to cut
            if not isBadVersion(m):
                l = m + 1 #cut the left side out and exclude the previous version
            else:
                r = m # cut the right side out and include the previous version since we know that all versions after current m can be discarded but we don't know if current m is first bad version
        return l