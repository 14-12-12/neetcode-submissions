import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for i in range (0, len(stones)):
            heapq.heappush(heap, -stones[i])
        i = 0
        while (len(heap)> 1):
            largest = -heapq.heappop(heap)
            largest2 = -heapq.heappop(heap)
            difference = largest - largest2 
            if (difference != 0):
                heapq.heappush(heap, -difference)
        if (len(heap) == 1):
            return -heapq.heappop(heap)
        else:
            return 0

        