class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        x = len(grid)
        y = len(grid[0])
        g = grid
        ret = 0
        for i in range(0, x):
            for j in range(0, y):
                if g[i][j] == 0:
                    continue
                
                # 1 이면 4로 출발
                num = 4
                num -= self.getVal(g, x, y, i-1, j)
                num -= self.getVal(g, x, y, i, j-1)
                num -= self.getVal(g, x, y, i+1, j)
                num -= self.getVal(g, x, y, i, j+1)
                ret += num

        
        return ret

    def getVal(self, g, x, y, i, j):
        if i > x -1 or j > y -1 or i < 0 or j < 0:
            return 0
        else:
            # print(f"{i} {j}")
            return g[i][j]
        
        