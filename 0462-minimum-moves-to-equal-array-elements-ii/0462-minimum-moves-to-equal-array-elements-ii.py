class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()

        m=nums[len(nums)//2]

        steps=0

        for i in nums:
            steps+=abs(i-m)

        return steps