class Solution:
    def minArraySum(self, nums, k, op1, op2):
        dp = [[[float('inf')]*(op2+1) for _ in range(op1+1)] for _ in range(len(nums)+1)]
        dp[0][0][0] = 0
        
        for i, x in enumerate(nums):
            for j in range(op1+1):
                for l in range(op2+1):
                    if dp[i][j][l] == float('inf'): continue
                    c = dp[i][j][l]
                    dp[i+1][j][l] = min(dp[i+1][j][l], c+x)
                    if j < op1: dp[i+1][j+1][l] = min(dp[i+1][j+1][l], c+(x+1)//2)
                    if l < op2 and x >= k: dp[i+1][j][l+1] = min(dp[i+1][j][l+1], c+x-k)
                    if j < op1 and l < op2:
                        h = (x+1)//2
                        dp[i+1][j+1][l+1] = min(dp[i+1][j+1][l+1], c+min(h, h-k if h>=k else float('inf')), c+((x-k+1)//2 if x>=k else float('inf')))
        
        return min(min(row) for row in dp[-1])