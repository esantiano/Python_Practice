from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        _seen = {}
        _oddChars = 0
        for char in s: 
            if char in _seen:
                _seen[char] += 1
            else: 
                _seen[char] = 1
            
            if _seen[char] %2 == 1:
                _oddChars += 1 
            else: 
                _oddChars -= 1
        
        if _oddChars > 0:
            return len(s) - _oddChars + 1
        else: 
            return len(s)