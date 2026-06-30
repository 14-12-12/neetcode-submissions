class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        Rows, Cols = len(grid), len(grid[0])
        r,c = 0,0
        island =0
        visit = set()
        def dfs(self, grid:List[List[str]], r: int, c: int):
            if (min(r,c)<0 or r == Rows or c ==Cols or (r,c) in visit or grid[r][c] == "0"):
                return 0
            visit.add((r,c))
            dfs(self,grid,r+1,c)
            dfs(self,grid,r-1,c)
            dfs(self,grid,r,c+1)
            dfs(self,grid,r,c-1)
            return 1
        while(r!= Rows):
            while(c!= Cols):
                if ((r,c) not in visit and (r,c)!= "0"):
                    island += dfs(self,grid,r,c)
                c += 1
            c = 0
            r += 1
        return island

        

        