# binary search - use two pointers at the start and end of intervals, determine the midpoint, adjust the midpoint depending on the result newInterval[0] > midpoint => start = midpoint + 1 newInterval[0] < midpoint => end = midpoint -1 
# check for overlap: 
# if either newInterval[0] or newInterval[1] are equal to starti or endi or within an interval then there is overlap, we can take starti and use either newInterval[1] as endi or continue looking fo other overlapping intervals 
# compare intervals[midpoint][1] with newInterval[0] and intervals[midpoint+1][0] and newInterval[1]

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals: 
            return newInterval
        _beg = 0 
        _end = len(intervals)-1
        target = newInterval[0]
        while _beg <= _end:
            _mid = (_beg + _end)//2
            if intervals[_mid][0] < target:
                _beg = _mid + 1
            else:
                _end = _mid - 1  
        intervals.insert(_beg,newInterval)
        res = []
        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        return res