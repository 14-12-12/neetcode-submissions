class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for i in range(0, len(nums)):
            heapq.heappush(heap, -nums[i])
        temp = k
        while (temp !=0):
            kth= -heapq.heappop(heap)
            temp = temp -1
        return kth


    
    
            


                    



        