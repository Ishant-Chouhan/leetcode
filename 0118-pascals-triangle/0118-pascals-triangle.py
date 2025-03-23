class Solution(object):
    def generate(self, numRows):
        lists = [0] * numRows
        for i in range(numRows):
            lists[i] = [1] * (i + 1)  
            for j in range(1, i):  
                lists[i][j] = lists[i - 1][j - 1] + lists[i - 1][j]
        return lists