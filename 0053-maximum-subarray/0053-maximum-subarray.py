class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        cur_sum = 0
        for i in nums:
            cur_sum = max(cur_sum,0)
            cur_sum += i
            res = max(res,cur_sum)
            
        return res