# Time O(N*K) - number of strings and number of chars in the longest string 
# Space O(N*K) - hashmap stores the same number of strings and chars
# This algorithm is mainly about key design, there are two different keys we can use for this problem. The rest of the algorithm, sorting the strings into their buckets and returning the resulting buckets is standard  
# key design: we want collisions in this case so we can group the strings together
# Algorithm for key design: for the key we will shift each string to start with 'a' and shift the rest of the string correspondingly join the characters together and use the resulting string as the key
# shifting a letter: chr((ord(letter)-shift)%26 + ord('a')) this returns a character 
# what is shift? shift is the starting character in the string to group
# why do we take %26? we want to wrap around between a-z
# why do we add ord('a')? this brings us back to 'a'

# use a map to store key:list relationship
# loop through strings

# add key to map
# add each string to corresponding key list
import collections
from typing import List
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        def shift_char(letter, shift):
            return chr((ord(letter)-ord(shift))%26+ord('a'))
        def get_hash_key(string):
            shift = string[0]
            return ''.join(shift_char(c,shift) for c in string)

        groupings = collections.defaultdict(list)
        for string in strings:
            key=get_hash_key(string)
            groupings[key].append(string)
        return list(groupings.values())