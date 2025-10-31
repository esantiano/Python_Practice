# we will use linear search 
# check the length of the list to make sure its greater than 3 elements
# to check that the list is a mountain we need to find the crest 
#   we need to make sure that each of the elements before the crest match the constraint
#   we need to make sure that each of the elements after the crest match the constraint
#   if any of the elements fall out of the constraints then we do not have a mountain
# Time O(n) - we are scanning the array at least twice 
class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        if len(arr) < 3:
            return False
        
        # find the crest and its index
        crest = max(arr)
        index_of_crest = arr.index(crest)
        
        # edge case where we have a slope but still technically able to pass the scans below
        if index_of_crest == 0 or index_of_crest == len(arr)-1:
            return False
        
        #scan the first half of the list 1 -> index of crest
        for i in range(0,index_of_crest):
            if arr[i]>=arr[i+1]:
                return False
        
        # scan the second half of the list
        for j in range(index_of_crest+1, len(arr)):
            if arr[j-1] <= arr[j]:
                return False
        
        # we have found a mountain
        return True
    
    # another approach using a single pass technique is climbing up the first half and then down the second half
    # no need to find the max 
    def validMountainArray2(self, arr: list[int]) -> bool:
        n = len(arr)
        i = 0 

        while i+1 < n and arr[i] < arr[i+1]: # with while loops we can include multiple conditional statements, we check i+1<n because of the second condition arr[i] < or > arr[i+1]
            i+=1 
        
        # we still need to include the check from above

        if i == 0 or i == n-1:
            return False
        
        while i+1 < n and arr[i] > arr[i+1]: 
            i+=1

        return i == n-1
sol = Solution()
print(sol.validMountainArray2([2,1]))
print(sol.validMountainArray2([3,5,5,6,5]))
print(sol.validMountainArray2([0,3,2,1]))
print(sol.validMountainArray2([0,1,2,3,4,5]))
print(sol.validMountainArray2([5,4,3,2,1,0]))
print(sol.validMountainArray2([3,4,5,6,5,4,4]))