# Time O(n+m) - iterate through stones and jewels
# Space O(n) - create a map for jewels
# create a map of the jewels first then go through each of the stones and check the jewels map to see if we have a jewel or not
import collections
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jmap = collections.defaultdict(int)
        for j in jewels:
            jmap[j]=0
        for s in stones:
            if s in jmap:
                jmap[s]+=1
        return sum(jmap.values())
            