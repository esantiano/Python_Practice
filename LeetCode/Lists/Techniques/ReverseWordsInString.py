# brute force
class Solution:
    def reverseWords(self, s: str) -> str:
        # base case s is one word -> we can just return s 
        
        # case spaces before first word and after last word in s -> we need to trim s first then reverse
        # case multiple spaces between words -> eliminate the extra spaces
        # create a copy of s
        
        copy = str(s)
        
        # split the copy into a list of words, this eliminates having to address extra spaces
        words = copy.split()
        
        # reverse the order of the words 
        l = 0 
        r = len(words)-1
        while l<r:
            
            # check that words[l] and words[r] are words and not spaces
            if words[l] != ' ' and words[r] != ' ':
                words[l], words[r] = words[r], words[l]
            l+=1
            r-=1
        
        # join words 
        return ' '.join(words)