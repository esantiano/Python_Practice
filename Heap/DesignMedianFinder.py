# Time: 
#   addNum O(KlogK) - we remove and add on to two heaps to determine where an element should be placed in the median finder
#   findMedian O(1) - We have constant access to elements that can be considered to be the median or used to calculate the median
# Space: O(K) 
#   we use two heaps to store elements added to the median finder
# Design: 
#   Using two heaps, a max heap and a min heap we can keep track of the bottom halves and top halves of the elements added to the median finder.
#   The max heap will store the lesser (first half) elements. The max heap will also store the most number of elements if we have an odd number of elements added to the median finder.
#   The min heap will store the greater (second half) elements.
#   This design will allow us to store the elements in ascending order e.g. [1,2,3,4,5] or [-5,-4,-3,-2,-1].
#   AddNum:
#       When we add elements we will first add to the max heap.
#       Then we'll attempt to balance the heaps by adding the top element of the max heap to the min heap.
#       If we are over balance (the min heap has more elements than the max) we'll add the top of the min heap to the max heap.
#       This will allow us to keep the added elements sorted while also allowing us constant access to the median element.
#   findMedian:
#       We determine the median by comparing the number of elements in both heaps.
#       If they are the same, then there are an even number of elements and we must calculate the median.
#       Calculating the median can be done by taking the top element from the min and max heap, adding them, and then dividing them by 2
#       If they are not the same then the median is at the top of the max heap and we can just return that.

import heapq
class MedianFinder:

    def __init__(self):
        self.minh = []
        self.maxh = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxh,-num)
        
        heapq.heappush(self.minh, -self.maxh[0])
        heapq.heappop(self.maxh)
        
        if len(self.minh) > len(self.maxh):
            heapq.heappush(self.maxh,-self.minh[0])
            heapq.heappop(self.minh)
            

    def findMedian(self) -> float:
        if len(self.minh) == len(self.maxh):
            return (self.minh[0] + (-self.maxh[0]))/2
        return -self.maxh[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()