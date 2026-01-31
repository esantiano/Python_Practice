# Time: O(NlogM + NlogN)
#   O(NlogM) time is used to determine the count of pairs less than the midpoint and search the space M
#   O(NlogN) time is used to sort nums
# Space: O(1) no extra space is used
# Algorithm:
#   We use a binary search with sliding window technique to determine the kth smallest distance
#   To use binary search we must sort the list first
#   The search space is between 0 and the maximum distance within the list
#   Once we determine the midpoint we use the sliding window to count the number of pairs that are less than the midpoint
#   We then compare the count to K to help us select the next search space
#   If we have found a potential value M that whose count is greater than or equal to k we save the result
#   We repeat the above until the search space has been closed 
class Solution:
    def smallestDistancePair(self, nums, k):
        def get_count(dist):
            l = 0
            count = 0
            for r in range(len(nums)):
                while nums[r]-nums[l]>dist:
                    l+=1
                count+=r-l
            return count
        
        nums.sort()
        L, R = 0, nums[-1]-nums[0]
        result = 0
        while L <= R:
            M = (R+L)//2
            count = get_count(M)
            if count < k:
                L = M+1 
            else:
                R=M-1
                result = M
        return result
                