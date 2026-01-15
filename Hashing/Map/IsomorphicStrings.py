# Time: O(n) - we will go through each string once, strings are also the same length
# Space: O(1) - the number of characters available is 26 lowercase letters, because of this the dictionaries do not grow with the size of the input
# Algorithm:
# use two hashmaps to save the mappings
# map the char in s as a key to the char in t as val and vice versa
# loop through both s and t
# first check the hashmaps for the chars in s and t
# if neither doesnt exist then map the kvps s:t and t:s
# if either exists and the current char t is not the same value as kvp s:t or current char s is no the same value as kvp t:s return false
# we can return true at the end
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        char_s_map = {}
        char_t_map = {}
        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]
            if (char_s not in char_s_map) and (char_t not in char_t_map):
                char_s_map[char_s] = char_t
                char_t_map[char_t] = char_s
            elif char_s_map.get(char_s) != char_t or char_t_map.get(char_t) != char_s: # we use .get() here instead of directly acessing a value because .get() will return a default value where as trying to directly access the value will return a key error
                return False
        return True