class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        ans = high
        while (low <= high):
            mid = (low+high)//2
            if mid == 0: 
                low = 1
                continue
            if (self.eat(mid, piles, h) == -1):
                low = mid+1

            else:
                ans = mid
                high = mid-1
        return ans
    
    def eat(self, k: int, piles1: List[int], h: int) -> int:
        counter = 0
        for p in piles1:
            counter += math.ceil(p / k)
        if (counter > h):
            return -1

        else:
            return 0

        