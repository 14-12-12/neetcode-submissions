class Solution:
    def calPoints(self, operations: List[str]) -> int:
        arr = []
        for i in range (0, len(operations)):
            try:
                num = int(operations[i])
                arr.append(num)
            except ValueError:
                if(operations[i]=="+"):
                    arr.append(int(arr[-1])+int(arr[-2]))
                elif(operations[i]=="D"):
                    arr.append(2*int(arr[-1]))
                elif(operations[i]=="C"):
                    arr.pop()
                else:
                    print("invalid")
        sum = 0
        for i in range(0, len(arr)):
            sum = sum+arr[i]
        return sum
