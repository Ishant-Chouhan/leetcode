class Solution(object):
    def minOperations(self, grid, x):
        """
        :type grid: List[List[int]]
        :type x: int
        :rtype: int
        """
        nums=[]
        m=float("-inf")
        for i in grid:
            for j in i:
                nums.append(j)

        nums.sort()
        m=nums[len(nums)//2]

        add=0
        for i in nums:
            n=abs(i-m)
            if n%x!=0:
                return -1
            else:
                add += n//x

        return add
