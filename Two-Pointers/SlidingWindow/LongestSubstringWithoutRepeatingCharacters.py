# Time O(n) - two passes, each char is seen twice at most
# Space O(min(m,n)) we need space for the map, where n is size of string and m is size of the charset/alphabet
# two pointer approach: left and right pointers used to determine max length
# use length var to record string length
# use map to keep count of seen chars
# iterate through chars in s using right pointer
# if we come across a repeat char then move the left pointer within s and update map until the repeat char count is decremented
# get the max length between the current max and right-left+1 
# move the right pointer
# return the max length
import collections
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seenChars = collections.Counter()
        maxLen = 0
        left = right = 0
        while right<len(s):
            rchar = s[right]
            seenChars[rchar]+=1
            while seenChars[rchar]>1:
                lchar=s[left]
                seenChars[lchar]-=1
                left+=1
            maxLen=max(maxLen,right-left+1)
            right+=1
        return maxLen
    
# this can be done in a single pass
    def lengthOfLongestSubstring2(self, s: str) -> int:
        charsToNextIndex = collections.dict()
        maxLen = 0
        j = 0
        for i in range(len(s)):
            char = s[i]
            charsToNextIndex[char]=i+1 # we do this so that if we see a duplicate then we move the left pointer to the index after the duplicate char
            if char in charsToNextIndex:
                j=max(charsToNextIndex[char],j) # we take the max to prevent the left pointer from moving backwards since the char index in charsToNextIndex could be outdated
            maxLen=max(maxLen,i-j+1)
            right+=1
        return maxLen