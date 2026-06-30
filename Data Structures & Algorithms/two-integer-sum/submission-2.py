class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_list=[]
        hashmap = {val:idx for val,idx in enumerate(nums)}
        print(hashmap)
        for i in hashmap:
            for j in hashmap:
                if hashmap[i]+hashmap[j] == target and i !=j:
                    sum_list.append(i) 
                    sum_list.append(j)
                    return sum_list
        return sum_list
        