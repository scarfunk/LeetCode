class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        r_maxs = []
        c_maxs = []
        for i in range(0, len(grid)):
            r_maxs.append(max(grid[i]))
            cols = []
            for j in range(0, len(grid)):
                cols.append(grid[j][i])
            c_maxs.append(max(cols))

        ret = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid)):
                # [i][j] = [0][0] [0][1]...
                # [j][i] = [0][0] [1][0]...
                can_max = min(r_maxs[i], c_maxs[j])
                # print(can_max)
                ret += can_max - grid[i][j]

        return ret
        