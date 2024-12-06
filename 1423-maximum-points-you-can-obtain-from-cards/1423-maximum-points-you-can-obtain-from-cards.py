class Solution:
    def maxScore(self, C, K):
        best = total = sum(C[:K])
        for i in range (K-1, -1, -1):
            total += C[i + len(C) - K] - C[i]
            best = max(best, total)
        return best
                    
        