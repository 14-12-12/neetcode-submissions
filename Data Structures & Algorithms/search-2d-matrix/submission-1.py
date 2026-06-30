class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L,R = 0,len(matrix)*len(matrix[0])-1
        number_of_columns = len(matrix[0])
        number_of_rows = len(matrix)
        while(L<=R):
            mid = (L+R)//2
            row = mid // number_of_columns
            col = mid % number_of_columns

            if (matrix[row][col]>target):
                R = mid -1 
            elif (matrix[row][col]<target):
                L = mid+1
            else:
                return True
        return False