class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        land = set()
        maximum_land = 0
        def dfs(self, grid: List[List[int]], r:int, c:int):
            if (min(r,c)<0 or r == rows or c == cols or grid[r][c]==0 or (r,c)in visit):
                return
            visit.add((r,c))
            land.add((r,c))
            dfs(self,grid,r+1,c)
            dfs(self,grid,r-1,c)
            dfs(self,grid,r,c+1)
            dfs(self,grid,r,c-1)
        
        for i in range (0, rows):
            for j in range(0, cols):
                if ((i,j) not in visit and grid[i][j]==1):
                    dfs(self,grid,i,j)
                    maximum_land = max(maximum_land,len(land))
                    temp = set()
                    land = temp
        return maximum_land




        