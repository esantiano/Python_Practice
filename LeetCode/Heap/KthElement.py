import heapq

class kthSmallestAlg1:
    def getKthSmallest(self,input,k):
        minHeap = input
        heapq.heapify(minHeap)

        for i in range(k-1):
            heapq.heappop(minHeap)
        
        return minHeap[0]
    
class kthLargestAlg1:
    def getKthLargest(self,input,k):
        maxHeap = [-el for el in input]
        heapq.heapify(maxHeap)

        for i in range(k-1):
            heapq.heappop(maxHeap)
        
        return -1*maxHeap[0]

ex1 = kthSmallestAlg1()
print(ex1.getKthSmallest([7, 10, 4, 3, 20, 15],3))

ex2 = kthLargestAlg1()
print(ex2.getKthLargest([7, 10, 4, 3, 20, 15],2))



class kthSmallestAlg2:
    def getkthSmallest(self,input,k):
        max_heap = []
        heapq.heapify(max_heap)

        for el in input:
            if len(max_heap) == k:
                if max_heap[0] < -el:
                    heapq.heappop(max_heap)
                    heapq.heappush(max_heap,-el)
            else:
                heapq.heappush(max_heap,-el)
        
        return -max_heap[0]

class kthLargestAlg2:
    def getkthLargest(self,input,k):
        min_heap = []
        heapq.heapify(min_heap)

        for el in input:
            if len(min_heap) == k:
                if min_heap[0] < el:
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap,el)
            else:
                heapq.heappush(min_heap,el)
        
        return min_heap[0]
    
ex3 = kthSmallestAlg2()
print(ex3.getkthSmallest([7, 10, 4, 3, 20, 15],3))

ex4 = kthLargestAlg2()
print(ex4.getkthLargest([7, 10, 4, 3, 20, 15],2))
