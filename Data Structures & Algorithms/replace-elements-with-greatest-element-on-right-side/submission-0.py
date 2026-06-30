class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(0,len(arr)-1):
            maximum = -1
            for j in range(i+1,len(arr)):
                if(arr[j]>maximum):
                    maximum = arr[j]
                arr[i] = maximum
        arr[len(arr)-1] = -1
        return arr




        