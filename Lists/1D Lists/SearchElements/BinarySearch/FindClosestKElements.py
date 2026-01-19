
from typing import List
# Time: O(log(N-k)+k)
#   O(log(N-k)) time is required for binary search to find the left boundary 
#   O(k) time is required to build the list returned at the end
# Space: O(1)
#   No extra space is used to find the leftmost boundary, 
#   the returned list does not count towards the space used
# Algorithm:
#   In this algorithm we are using the binary search to find a window of size k that includes values closest to x. 
#   Calculate the mid point in the search space.
#   Compare the element at [mid] to the element at [mid + k] (right most boundary of the current window [mid: mid+k]) to determine the direction of the next search space.
#   Since we are not expecting more than k elements we conclude that only one of these elements [mid] or [mid + k] must be in the final list. (mid + k is just outside of the window)
#   We determine which side to include in the search based on how close each given element is to x as well as how close elements in that direction are to x. 
#   We repeat this until we have the left most boundary of the window. 
class Solution1:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        L, R = 0, len(arr)-k # If the window includes the last element then the left boundary of the window must be len(list)-k
        while L < R: # left and right pointers will meet L == R
            M = (R+L)//2
            if x-arr[M] > arr[M+k]-x: # in this comparison we do not use abs() because it would remove the sign ordering information of each element
                L = M + 1 # nothing to the direction left of the midpoint, including the midpoint will be included in the window
            else:
                R = M # mid point value is closer nothing in the direction of mid + k is close to x, here set the right boundary to mid (remember that the actual search space goes up to mid + k)

        return arr[L:L+k] # We can use either pointer from the binary search to set the left boundary and add k to the left boundary to get the right boundary of the window

# Time O(logN + k) 
#   O(logN) time required to find the closest element to x within array.
#   O(k) time required to expand the window of k values
# Space O(1) No extra space needed
# Algorithm: 
#   In this algorithm we use binary search to find the leftmost position of the element closest to x.
#   Once we find this index we use the two pointer window approach to expand the window of the eligible k elements.
#   If we see that the left pointer is out of bounds we expand to the right.
#   If we see that the right pointer is out of bounds expand left.
#   We compare the distances and expand outward toward the closer element
class Solution2:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        L, R = 0, len(arr)-1
        while L < R:
            M = L + (R-L)//2
            if arr[M] < x:
                L = M + 1
            else:
                R = M
        L = L - 1, L
        while R - L - 1 < k:
            if L < 0:
                R += 1
            elif R >= len(arr):
                L -= 1 
            elif abs(arr[L] -x) <= abs(arr[R]-x):
                L -= 1
            else:
                R += 1 
        return arr[L + 1: R]