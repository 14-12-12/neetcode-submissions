class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        lists = []
        nums.sort()
        def sum1(index: int, path: List[int], target: int):
            if (target == 0):
                lists.append(list(path))
                return
            for i in range(index, len(nums)):
                n = nums[i]
                if (target >= n):
                    path.append(n)
                    sum1(i, path, target - n)
                    path.pop()
                else:
                    break
        sum1(0, [], target)
        return lists