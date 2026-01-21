
# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

# Space: O(1) No extra space is used 
class Solution:
# Time: O(logN) where N is the initial size of the search space
#   O(logN) time is used for the binary search of the space
# Algorithm
#   Here we assume an initial search space
#   Use binary search to reduce search space to a size of 1
#   check final search space and return the result
    def search1(self, reader: 'ArrayReader', target: int) -> int:
        
            L = 0
            R = 10**4
            while L < R:
                M = L + (R-L)//2
                result = reader.get(M)
                if result == (2**31)-1 or result >= target:
                    R = M
                elif result < target:
                    L = M + 1
            if reader.get(L) == target:
                return L
            return -1
# Time: O(logT) where T is the index of the target
#   O(logT) time is used to expand the size of the search space
#   O(logT) time is used to search for target within the search space
# Algorithm:
#   Here we expand our search space until we have a range of values that target is likely to exist in
#   We perform binary search until our search space is reduced to zero or the index of target is found
    def search2(self, reader: 'ArrayReader', target: int) -> int:
        
            L = 0
            R = 1
            while reader.get(R) < target:
                R *= 2
            
            while L <= R:
                M = L + (R-L)//2
                result = reader.get(M)
                if result == target:
                    return M
                elif result < target:
                    L = M + 1
                else:
                    R = M - 1
            return -1

            