# Another two pointer approach
# the first pointer in the first loop goes through each word in text 
# the second pointer loops through each character in the word in reverse and adds it to the result
# Time O(N) - We iterate through each character in the s (N)
# Space: O(N) - N being size of the string, we must create space for the result 
class Solution:
    def reverseWords(self, s: str) -> str:
        # python doesnt allow string modification
        # split the s into a list based on spaces to preserve original white space
        text = s.split()
        
        # create a result string to store our result
        result = ''
        
        #iterate through each item in the list
        for i in range(len(text)):
            # Note: lines 17 and 19-21 can be replaced with result += text[i][::-1]
            # create a pointer at the end of chars
            j = len(text[i])-1
            # iterate through chars backwards 
            while j >= 0:
                result += text[i][j]
                j-=1
            
            # add spaces to result at the end of each item except the last one
            # Note: we can also just remove the chech and then return result.strip()
            # doing so would eliminate the use of index (i) and we can iterate through each element
            if i != len(text)-1:
                result += ' '
        
        # remove the space at the end of the resulting string
        return result