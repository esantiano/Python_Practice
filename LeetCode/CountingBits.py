
class Solution: # space O(n) time O(n)
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n+1)
        offset = 1 # keep track of the most recent power of 2
        for x in range(1,n+1):
            if offset * 2 == x:
                offset = x # update offset when we hit the next power of 2
            ans[x] = 1 + ans[x - offset] # formula: number of 1s in x = 1 + number of 1's in (x - offset)
        return ans