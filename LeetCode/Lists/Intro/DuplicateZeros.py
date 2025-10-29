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
    # Time O(n) - could be done in two passes 
    # count the number of zeros in the list 
    # insert 0's where possible 
    # space O(1) in place 
    def duplicateZeros2(self, arr: list[int]) -> None:
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
# [1,0,2,3,0,4,5,0]
# zeros = 3 
# n = 8 
# j = 8 + 3 - 1 = 10
#     i = 7 
#         arr[7] == 0 
#         j = 9 
#     j = 8 
#     i = 6 
#         arr[6] == 5
#     j = 7 
#     i = 5
#         7 < 8
#         arr[7] = arr[5] => [1,0,2,3,0,4,5,5]
#     j = 6
#     i = 4
#         6 < 8 
#         arr[6] = arr[4] => [1,0,2,3,0,4,0,4]
#         arr[4] = 0 
#         j = 5 
#             5 < 8 
#             arr[5] => [1,0,2,3,0,0,0,4]
#     j = 4
#     i = 3
#         4 < 8 
#             arr[4] = arr[3] => [1,0,2,3,3,0,0,4]
#         arr[3] = 3 
#     j = 3
#     i = 2
#         3 < 8 
#             arr[3] = arr[2] => [1,0,2,2,3,0,0,4]
#         arr[2] = 2
#     j = 2
#     i = 1
#         2 < 8 
#         arr[2] = arr[1] => [1,0,0,2,3,0,0,4]
#         arr[1] = 0 
#             j = 1
#             1 < 8:
#                 arr[1] = 0 => [1,0,0,2,3,0,0,4]
#     j = 0 
#     i = 0 
#         arr[0] = arr[0] => [1,0,0,2,3,0,0,4]
#     arr[0] = 1
#     j = -1
#     i = -1