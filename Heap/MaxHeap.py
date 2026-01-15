import heapq
maxHeap = []

heapq.heapify(maxHeap)

heapq.heappush(maxHeap, -1 * 1)
heapq.heappush(maxHeap, -1 * 3)
heapq.heappush(maxHeap, -1 * 2)

print("maxHeap: ", maxHeap)

peekNum = maxHeap[0]

print("peek number: ", -1 * peekNum)

popNum = heapq.heappop(maxHeap)

print("pop number: ", -1 * popNum)

print("peek number: ", -1 * maxHeap[0])

print("maxHeap: ", maxHeap)

size = len(maxHeap)

print("maxHeap size: ", size)