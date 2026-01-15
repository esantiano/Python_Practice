# Time O(n+k) where we need to run through the number of elements in heights and k(range min to max)
# Space O(n) we use another list to compare
# counting sort practice: 
# sort the list first then compare
# use a hashmap and empty list
# for each element in the list count the number of times it appears
# pull the min and max values from the list
# then loop through the range of min and max values 
# every time we see the value in the hashmap add that value to the list
# do this for the number of frequencies it occurrs 
# compare the list against heights and count the number of misplaced elements

class Solution:
    def count(self,heights):
        sorted_heights = []
        seen = {}
        min_val, max_val = min(heights), max(heights)

        for num in heights:
            if num in seen:
                seen[num]+=1
            else:
                seen[num]=1

        for val in range(min_val,max_val+1):
                while seen.get(val,0)>0:
                    sorted_heights.append(val)
                    seen[val]-=1
        return sorted_heights
    
    def heightChecker(self, heights: list[int]) -> int:
        misplaced = 0
        sorted_heights = self.count(heights)
        for j in range(len(heights)):
            if sorted_heights[j] != heights[j]:
                misplaced+=1
        return misplaced
sol = Solution()
print(sol.heightChecker([1,1,4,2,1,3]))
print(sol.heightChecker([1,2,3,4,5]))