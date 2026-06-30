import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i in range (0, len(points)):
            distance = math.sqrt((points[i][0] - 0)**2 + (points[i][1] - 0)**2)
            # Push a tuple of (distance, point) into the heap
            heapq.heappush(heap, (distance, points[i]))
        k_closest= []
        temp = k
        while (temp > 0):
            # Pop the tuple and take the point (index 1)
            value = heapq.heappop(heap)[1]
            k_closest.append(value)
            temp = temp - 1
        return k_closest


        



                


        