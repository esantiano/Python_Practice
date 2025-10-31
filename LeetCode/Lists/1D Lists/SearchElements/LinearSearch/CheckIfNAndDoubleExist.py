# Linear search Practice
# create a hashtable to store indexes and elements
# loop through the list
# check the hashtable to see if we have seen elements that match the criteria
#   return true if criteria are met
# store elements in the hashtable
#   use element as key and indices as value
# return false if we reach the end of list and no criteria are met
# Time O(n) - linear search once through the list
# Space O(n) - hash table or set to store the elements 
class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        hash_table = {} # we can use a set here 
        
        for i in range(len(arr)):
            if (arr[i]*2 in hash_table):
                return True
            elif arr[i]%2 == 0 and (arr[i]/2 in hash_table): # we can combine this check with the top 
                return True
            else:
                hash_table[arr[i]] = i # add to the set 
        return False
sol = Solution()
print(sol.checkIfExist([10,2,5,3]))
print(sol.checkIfExist([3,1,7,11]))