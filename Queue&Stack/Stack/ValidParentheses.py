# Time O(n) - at worst we iterate through all chars in s
# Space: O(n) - we use a stack as well as a map
# Algorithm: 
# use a map to map close brackets to open brackets 
# use a stack to maintain order of open brackets 
# iterate though s 
# push open brackets onto the stack 
# when we encounter a closing bracket we need to check the stack first then use the map to compare the type of open bracket we should see on top of the stack
# return false if they dont match
# when we complete iterating through s we should check to see if anything is on the stack as the final check
class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {"{":"}", "(":")", "[":"]"}
        open_stack = []
        for b in s:
            if b in brackets.keys():
                open_stack.append(b)
            elif not open_stack or b != brackets[open_stack.pop()]:
                return False
        return not open_stack