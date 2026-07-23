class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def bfs(self, row:int,col:int,grid: List[List[int]]) -> int:
            ROWS, COLS = len(grid), len(grid[0])
            visit = set()
            queue = deque()
            minutes = 0
            queue.append((row,col))
            visit.add((row,col))
            while queue:
                for i in range(len(queue)):
                    r,c = queue.popleft()
                    if grid[r][c] == 2:
                        return minutes
                    neighbors = [[1,0],[-1,0],[0,1],[0,-1]]
                    for dr, dc in neighbors:
                        nr, nc = r+dr, c+dc
                        if nr < 0 or nc < 0 or nr == ROWS or nc == COLS or (nr,nc) in visit or grid[nr][nc]==0:
                            continue
                        queue.append((nr,nc))
                        visit.add((nr,nc))
                minutes += 1
            return -1
        values = [0]
        for x in range (len(grid)):
            for y in range (len(grid[0])):
                if grid[x][y] == 1:
                    minutes = bfs(self,x,y,grid)
                    if (minutes == -1):
                        return -1
                    else:
                        values.append(minutes)
        return max(values)



        