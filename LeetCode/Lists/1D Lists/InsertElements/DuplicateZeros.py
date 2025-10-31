class Solution:
    # Time O(n^2) possibly since we would need to shift the elements ahead of any 0's found 
    # Space O(1) since its all done in place 
    # the main takeaways here are shifting the elements in place 
    def duplicateZeros(self, arr: list[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        # loop through the list until we find 0
        # then shift elements first then insert 0 into new open position
        # we also need to shift the pointer so we dont read the inserted 0
        i = 0 
        n = len(arr)-1
        while i < n:
            if arr[i] == 0:
                for j in range(n-1,i-1,-1):
                    arr[j+1] = arr[j]
                i+=1
            i+=1
sol = Solution()
print(sol.duplicateZeros([1,0,2,3,0,4,5,0])) 
