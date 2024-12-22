class Solution:
    def minPathSum(self, grid):
        n = len(grid)
        m = len(grid[0])
        dp = [0] * m
        for i in range(n):
            temp = [0] * m
            for j in range(m):
                if i == 0 and j == 0:
                    temp[j] = grid[i][j]
                else:
                    top = float('inf') if i == 0 else dp[j]
                    left = float('inf') if j == 0 else temp[j - 1]
                    temp[j] = min(top, left) + grid[i][j]
            dp = temp
        return dp[m - 1]