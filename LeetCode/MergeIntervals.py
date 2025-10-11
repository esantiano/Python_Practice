# intervals may not be sorted, sort intervals first
# take stock of the start and end of the first items least and greatest seen so far 
# if the start in the next item of intervals[i] is less than greatest seen so far then merge
# if we merge then take note of the new greatest and least seen so far of the new interval created
# if the start of the next item of intervals is greater than the greatest seen so far then we can move on and change the greatest seen so far and 
# current = [1,3], least = 1, greatest = 3 ,next = 2,6 
# 3 > 2  merge == [1,6] 
# current = [1,6], least = 1 greatest = 6 next = 8,10
# current = [8,10], least = 1, greatest = 10, next = 15,18
# current = []
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        result = []
        for interval in intervals:
            if not result or result[-1][1] < interval[0]:
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1],interval[1])
        return result
        