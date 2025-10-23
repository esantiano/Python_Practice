# Time complexity: O(nm). For every window_start, we may have to iterate at most m times. There are n−m+1 such window_start's. Thus, it is O((n−m+1)⋅m), which is O(nm).
# Sliding window - naive approach
# traverse each possible substring of length m (length of the needle) in the haystack and check if it is equal to the needle
# each substring will start at a different index 
# we can represent the starting position of each substring as n (length of haystack) - m + 1
# the ending position of each substring can be represented as 
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)

        for start in range(n-m+1): # we only need to iterate till starting index of the last substring of length m or (n-m), the +1 is added because the input for range is exclusive 
            for i in range(m): # iterate over the length of the needle, this is the length of the window
                if needle[i] != haystack[start+i]: # we start checking the haystack at start 
                    # if at any point in the loop the characters don't match then we break out of the inner comparison loop
                    break
                if i == m-1: # if we reach the last index of the needle then we have found the first ocurrence of the substring
                    return start
        # we haven't found an ocurrence

        # another way we can write this 
        # if haystack[start:start+m] == needle: we can just compare the haystack substring rather than each character
        #   return start
        return -1

sol = Solution()
result = sol.strStr("stringinafunction", "inafun")
print(result)