class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        maxStreak = 0
        for i in range(0,len(nums)):
            if (nums[i]==1):
                counter = counter +1
            else:
                counter = 0
            if (counter > maxStreak):
                maxStreak = counter
        return maxStreak