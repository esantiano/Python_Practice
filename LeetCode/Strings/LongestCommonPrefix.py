# This solution applies horizontal scanning 
# there is a solution vertical scanning where we build the common prefix by comparing each of the characters in all strings in the list 
# time complexity O(S) S = sum of all characters in each string 
class Solution:
    def longestCommonPrefixHorizontal(self, strs: list[str]) -> str:
        # we can set common prefix to the first word in strs
        common_prefix = strs[0]
        # then we can start comparing the next words in strs to common prefix 
        # we will take a word and compare the characters in common prefix to the characters in the word
        # if the word is longer than common prefix then we can break out of the comparison
        # if they don't match then we can stop comparing the characters in common prefix and the word and udpate common prefix to just the characters that match
        # if the common prefix is longer than the word then we can update common prefix to match the length of the word
        # after we compare all the words to common prefix we can return the common prefix 
        # if we find that common prefix gets updated to an empty string then we can just return an empty string
        
        for i in range(1,len(strs)):
            if common_prefix == "":
                break
            word = strs[i]
            for j in range(len(word)):
                if j >= len(common_prefix):
                    break
                if common_prefix[j] != word[j]:
                    common_prefix = common_prefix[:j] # we want to exclude the non-matching character
            if len(common_prefix) > len(word):
                common_prefix = word
        return common_prefix
    
    def longestCommonPrefixVertical(self, strs: list[str]) -> str:
        common_pref = ''
        for i in range(len(strs[0])):
            char = strs[0][i]
            for j in range (1, len(strs)):
                if i == len(strs[j]) or strs[j][i] != char:
                    return common_pref    
            common_pref += char

        return common_pref
sol = Solution()
input1 = ["glow", "glowing", "glue"]
input2 = ["dog", "do", "d"]

print(sol.longestCommonPrefixHorizontal(input1))
print(sol.longestCommonPrefixVertical(input1))
print(sol.longestCommonPrefixHorizontal(input2))
print(sol.longestCommonPrefixVertical(input2))
