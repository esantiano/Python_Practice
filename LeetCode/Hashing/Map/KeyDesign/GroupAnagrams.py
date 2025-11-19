# Time: O(NKLogK) - N is length of strs and K is the max length of a string in strs, outer loop O(N)m sorting is O(KLogK)
# Space: O(NK) - total number of characters stored in the map
# we use a hashmap with a anagram:list[strings] relationship
# the key we use is alphabetical order, we sort the chars in each string by alphabetical order
# once we have the correct key we will be able to map the string to its appropriate list in the hashmap
# iterate through the hashmap
# for each key store the mapped list in an output list
# the output list should be a list of lists in the format [[string]]
class Solution:
    def getKey(self,s):
            return "".join(sorted(s))
        
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        string_map = {}
        for s in strs:
            key = self.getKey(s)
            if key not in string_map:
                string_map[key]=[s]
            else:
                string_map[key].append(s)
        result = []       
        for str_list in string_map.values():
            result.append(str_list)
        return result
    # the above can be simplified 
    def groupAnagrams2(self, strs: list[str]) -> list[list[str]]:
        string_map = {}
        for s in strs:
            key = "".join(sorted(s))
            if key not in string_map:
                string_map[key]=[s]
            string_map[key].append(s)
        return [string_map.values()]