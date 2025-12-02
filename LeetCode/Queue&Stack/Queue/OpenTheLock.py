# Complexity n = 10 = 0-9, w = 4 = # wheels, d = len(deadends)
# Time: O(4(d+10^4)) ~ O(1) 
# Space: O(4(d+10^4)) ~ O(1) 
# Explanation: there are 10000 possible combinations 0000->9999, the set will store all the combinations and possibly process every combination

# Algorithm:
# use a deque to queue the possibilities to check 
# use a set to keep track of seen possibilities to skip
# use a step counter to keep track of required number of steps 
# check "0000" first to see if its in dead ends 
# use a while loop to drive 
#   get the size of the queue to determine the number of loops in for loop 
#   use a for loop to go through the 
#       popleft from the deque to get the first combo to check
#       check if equal to target 
#           if it is then return the total number of steps 
#       otherwise 
#           mark the current combo as seen 
#           generate neighbors, skip seen and dead ends
#   increment steps 
# return -1
import collections 
from typing import List
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        q = collections.deque(["0000"])
        seen = set(deadends)
        seen.add("0000")
        step = 0 
        if "0000" in deadends:
            return -1
        if "0000" == target:
            return step
        while q:
            size = len(q)
            for i in range(size):
                cur = q.popleft()
                if cur == target:
                    return step
                else: # generate neighbors
                    for j in range(4):
                        digit = cur[j]
                        updigit = str((int(digit)+1)%10) # the section from here to the end of the for loop can be replaced as seen below
                        downdigit = str((int(digit)-1+10)%10)
                        new_up_combo = cur[:j] + updigit + cur[j+1:]
                        new_down_combo = cur[:j] + downdigit + cur[j+1:]
                        if new_up_combo not in seen:
                            q.append(new_up_combo)
                            seen.add(new_up_combo)
                        if new_down_combo not in seen:
                            q.append(new_down_combo)
                            seen.add(new_down_combo)   
            step+=1
        return -1
    
    def openLock2(self, deadends: List[str], target: str) -> int:
        q = collections.deque(["0000"])
        seen = set(deadends)
        seen.add("0000")
        step = 0 
        if "0000" in deadends:
            return -1
        if "0000" == target:
            return step
        while q:
            size = len(q)
            for i in range(size):
                cur = q.popleft()
                if cur == target:
                    return step
                else: # generate neighbors
                    for j in range(4):
                        digit = cur[j]
                        turns = (1,-1)
                        for turn in turns:
                            new_digit = str((int(digit)+turn)%10)
                            new_combo = cur[:j] + new_digit + cur[j+1:]
                            if new_combo not in seen:
                                seen.add(new_combo)
                                q.append(new_combo)
            step+=1
        return -1