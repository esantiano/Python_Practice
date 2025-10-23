# standard two pointer list reversal
class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0 
        r = len(s)-1
        
        while l<r:
            s[l],s[r] = s[r],s[l]
            l+=1
            r-=1
        print(s)
sol = Solution()
print(sol.reverseString(["h","e","l","l","o"]))