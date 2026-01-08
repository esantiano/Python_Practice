# Time O(X + KlogX) where X = min(N,K), N = size of matrix 
#   constructing the heap requires O(X) time
#   We perform KlogX iterations of removing and adding from/to the min heap
# Space O(X) - a heap is created 
# Notes:
#   We're given a sorted matrix, rows and columns are sorted in ascending order.
#   In order to find the kth smallest value in the matrix we can treat this like finding the kth smallest value from N sorted lists. 
#   (Use a pointer in each list to compare values, advance the pointer within the appropriate list ie the next value to appear in the sequence)
#   Using a heap we can store the values and indexes/pointers for the values in the matrix. 
#   The tuple that is stored in the heap is (value, row, column). Here the row and column are used to point to the value in the row.
# Algorithm  
#   We will build the heap using the minimum between N and K.
#   Our reasoning: We don't need to push all the values from the matrix into the heap.
#     if K < N: the kth value will likely reside in one of the earlier rows so there is no need to look initialize pointers to look at the values in later rows.
#     if K > N: the kth value will likely reside in one of the later rows, however we cannot push elements from more than N rows, we will need to initialize values in all of the rows to determine where the kth value resides.
#   Once the heap has been initialized with the starting values and pointers we can start looking for the kth element.
#       To do this we remove the value and pointer (row and column) from the heap
#       We check to see if there are additional values in the row and add them to the heap
#       We will repeat the above k times, decrementing k each time.
#   Once we have found the kth value we can return it.
from typing import List
import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        min_heap = []
        n = len(matrix)
        
        for i in range(min(n,k)): 
            heapq.heappush(min_heap,(matrix[i][0],i,0))

        while k:
            val, row, col = heapq.heappop(min_heap)

            if col < n-1:
                heapq.heappush(min_heap,(matrix[row][col+1], row, col+1))
            k-=1
        return val