class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0,0,0]
        for i in range(0, len(nums)):
            for j in range (0,len(counts)):
                if (nums[i]== j):
                    counts[j]= counts[j]+1
        
        print(counts)
        n = 0
        for i in range (0, len(counts)):
            for j in range (0,counts[i]):
                nums[n] = i
                n = n +1
        