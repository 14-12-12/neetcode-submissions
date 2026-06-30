class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def subset1(self, nums_list: List[List[int]], length: int) -> List[List[int]]:
            res = [[]]
            for n in nums:
                res += [curr + [n] for curr in res]
            return res
        list_1 = []
        length = len(nums)
        list_1 = subset1(self, list_1, length)
        return list_1