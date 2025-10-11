class Solution:
    def romanToInt(self, s: str) -> int:
        _rNum = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        total = _rNum.get(s[-1])
        for i in reversed(range(len(s)-1)):
            if _rNum[s[i]] < _rNum[s[i+1]]:
                total -= _rNum[s[i]]
            else:
                total += _rNum[s[i]]
        return total