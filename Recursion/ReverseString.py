class Solution:
    # we need a helper function that takes two indexes to swap 
    def helper(self, start, end, s):
        # start with the base case: we reach end of the list 
        if start >= end:
            return
        s[start],s[end] = s[end],s[start]
        self.helper(start+1,end-1,s)  
        
    def reverseString(self, s: list[str]) -> None:
        return self.helper(0,len(s)-1,s)