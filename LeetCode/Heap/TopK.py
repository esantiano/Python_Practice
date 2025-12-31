import heapq

class ExampleTopKLargest:
    
    def getKLargest(self,input,k):
        minHeap = []
        heapq.heapify(minHeap)

        def addElementCheckHeap(heapLen,addEl):
            heapq.heappush(minHeap,addEl)

            if len(minHeap) > heapLen:
                heapq.heappop(minHeap)
        
        for el in input:
            addElementCheckHeap(k,el)

        return minHeap

class ExampleTopKSmallest:
    
    def getKSmallest(self,input,k):
        maxHeap = []
        heapq.heapify(maxHeap)

        def addElementCheckHeap(heapLen,addEl):
            heapq.heappush(maxHeap,addEl)

            if len(maxHeap) > heapLen:
                heapq.heappop(maxHeap)
        
        for el in input:
            addElementCheckHeap(k,(-1*el))

        return [-1*el for el in maxHeap]

ex1 = ExampleTopKLargest()
print(ex1.getKLargest([2,1,3,4,0],2))

ex2 = ExampleTopKSmallest()
print(ex2.getKSmallest([2,1,3,4,0],2))