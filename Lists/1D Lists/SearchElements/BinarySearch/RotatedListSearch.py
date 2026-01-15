# Time: O(logN) in all algorithms we use binary search to find the pivot index and then the target index, or just the target index
# Space: O(1) we do not use extra space to find the index of target
# Note: All approaches use binary search
from typing import List
class Solution:
    # This algorithm determines the pivoted index by comparing the middle value to the last value in nums and shifting 
    # the left and right pointers until they cross. if mid > end then the pivot index is on the right side of mid, else its on the left side
    # After determining the pivot index we can split the list into two halves and perform a standard binary search on both halves to find the target value index or not.
    def search1(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n-1

        while left <= right:
            mid = (left + right) // 2 + left
            if nums[mid] > nums[-1]:
                left = mid + 1
            else:
                right = mid - 1 
        
        def binarySearch(left_bound, right_bound, target):
            left, right = left_bound, right_bound
            while left <= right:
                mid = (left + right) // 2 + left
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1
        
        if (answer := binarySearch(0, left-1, target)) != -1:
            return answer
        return binarySearch(left, n-1, target)
    
    # This algorithm uses the same method as above to determine the pivot index. 
    # In this algorithm we are treating the list as a circular list.
    # Instead of performing a binary search on two parts of the split list 
    # we perform one binary search by first calculating the shift and
    # adjusting the left and right indexes to their effective distances from the pivot.
    # The mid point is calculated as normal however the value we compare uses an offset mid index relative to n. 
    # The rest of the binary search algorithm continues as usual.
    def search2(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n-1

        while left <= right:
            mid = (left + right) // 2 + left
            if nums[mid] > nums[-1]:
                left = mid + 1
            else:
                right = mid - 1

        def shiftedBinarySearch(pivot_index, target):
            shift = n - pivot_index
            left, right = (pivot_index + shift)%n, (pivot_index-1+shift)%n

            while left <= right:
                mid = (left + right) // 2 + left
                if nums[(mid-shift)%n] == target:
                    return (mid-shift)%n
                elif nums[(mid-shift)%n] > target:
                    right = mid -1
                else:
                    left = mid + 1
            return -1
        return shiftedBinarySearch(left, target)
    
    # In this algorithm we perfrom a single binary search. 
    # The binary search uses standard search space and middle point calculation. 
    # However we determine which half of the list to search based on comparison of the first value in the list and the mid point value.
    # We recognize that at the pivot index only one half of the list is sorted.
    # If the middle value is greater than or equal to the first value then we can conclude that the left hald of the list is sorted.
    # We can determine if the target value resides in the left half of the list by comparing it to the first and middle values otherwise we can check the right half of the list.
    # If the middle value is less than the first value then we can conclude the right hald is sorted.
    # We can determine if the target value resides in the right half of the list through similar comparison of middle, target and right, otherwise we can check the left half of the list. 

    def search3(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (right-left)//2 + left
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[left]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid -1
        return -1