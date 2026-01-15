# Practice swapping elements in place
# Time O(n) - we only go through the list once
# Space O(1) - this is done in place 
class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        # last element always be part of list unless there is only one element
        # start with seen = -1
        # loop through the list starting at n-1
        # use a temp to store the largest seen element
        # store seen at index of largest seen element
        # set seen = temp
        largest_seen = -1
        n = len(arr)
        
        for i in range(n-1,-1,-1): # can also just use len(arr) here
            temp = arr[i] 
            if temp > largest_seen: # we can also just do a direct comparison between arr[i] and largest_seen
                arr[i] = largest_seen # we can single line swap largest_seen, arr[i] = arr[i], largest_seen
                largest_seen = temp
            else:
                arr[i] = largest_seen
        return arr
sol = Solution()
print(sol.replaceElements([17,18,5,4,6,1]))
print(sol.replaceElements([17,18,5,6,1,1]))
print(sol.replaceElements([400]))
