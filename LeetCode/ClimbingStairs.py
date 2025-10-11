class Solution:
    def climbStairs(self, n: int) -> int:
        _first, _second = 1, 1
        i = 1
        while i < n:
            temp = _first 
            _first = _first + _second
            _second = temp 
            i += 1
        return _first