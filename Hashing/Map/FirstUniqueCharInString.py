# Time O(n) - loop through s once to build the map and once through map to get the resulting index
# Space O(1) - only 26 characters to fill map
# Unconventional Algorithm: 
#   map stores two concepts [index, unique flag], 
#   the list is mutable and its semantics are ambiguous, 
#   it would be more conventional to store a class with these datatypes
# use a map to create a char:index relationship
# use a second map to create a char:[index, is_unique] relationship
# iterate through s
# if we encounter a char for the first time place it, its index, and is_unique flag in the map
# otherwise update the is_unique flag of the char in the map
# initialize a result to store the index 
# iterate through the map checking the is_unique flag and updating the value of the resulting index to the minimum index 
# return the result
class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_index_map = {}
        
        for i,c in enumerate(s):
            if c not in char_index_map:
                char_index_map[c] = [i,True]
            else:
                char_index_map[c][1] = False
                
        result = -1
        for index,is_unique in char_index_map.values():
            if is_unique:
                if result == -1 or index < result:
                    result = index

        return result
    
# Conventional algorithm: 
# use a map to store the char:count relationship in s
# enumerate s and return the index of the first char with a count of 1 
# return -1 if no unique char exists 
    def firstUniqChar2(self, s: str) -> int:
        count = {}
        for c in s:
            if c in count:
                count[c]+=1
            else:
                count[c]=1
        for index,c in enumerate(s):
            if count[c]==1:
                return index
        return -1