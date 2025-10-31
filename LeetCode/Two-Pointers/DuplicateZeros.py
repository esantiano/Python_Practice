    # Time O(n) - could be done in two passes 
    # count the number of zeros in the list 
    # insert 0's where possible 
    # space O(1) in place 
class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        zeros = arr.count(0)
        n = len(arr)
        j = n + zeros - 1 # we set j at the last index at the extended list 
        i = n - 1 # we start iteration at the end 
        while i>=0:
            if j<n: # once j is within the bounds of the current list we can start reassigning the indexes
                arr[j] = arr[i]
            if arr[i] == 0: # when we find a 0 at index i 
                j -= 1 # j is being used to manage the placement of non-zero elements, 
                       # and encountering a zero at arr[i] means that the position j 
                       # was previously assigned to a non-zero element that should now 
                       # be shifted to an earlier position or that j is being adjusted 
                       # to account for the zero encountered.
                if j<n: # This step, in conjunction with the previous j -= 1, 
                        # suggests that if a 0 is found at arr[i], 
                        # a 0 is also explicitly placed at the adjusted j position, 
                        # effectively moving the 0 towards the end of the array
                        # or filling a gap created by shifting non-zero elements.
                    arr[j] = 0 # if j is within the bounds then we can reassign the value at index j 
            j -= 1
            i -= 1
sol = Solution()
print(sol.duplicateZeros([1,0,2,3,0,4,5,0])) 