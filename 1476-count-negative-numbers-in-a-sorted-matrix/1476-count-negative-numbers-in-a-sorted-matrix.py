class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        neg=0
        for i in grid:
            for j in i:
                if j<0:
                    neg+=1

        return neg