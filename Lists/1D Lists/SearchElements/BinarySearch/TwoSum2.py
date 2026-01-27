# Time: O(NlogN) 
#   O(N) time required to iterate through numbers
#   O(logN) time required to search for a complement
# Space: O(1)
#   No extra space used 
# Notes:
#   numbers is already sorted 
#   two pointer is more efficient
# Algorithm:
#   iterate through numbers linearly
#   calculate target - i
#   the left boundary of the search space can be set to i + 1 
#   since we are finding the complement of the element at i
#   binary search for target - i
#   reduce the search space to 1 element 
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = []
        for i in range(len(numbers)):
            comp = target - numbers[i]
            L, R = i+1, len(numbers)-1
            while L <= R:
                M = L + (R-L)//2
                if numbers[M] == comp and M != i:
                    result.append(i+1)
                    result.append(M+1)
                    return result
                if numbers[M] < comp:
                    L = M + 1
                else:
                    R = M - 1
