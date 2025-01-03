class Solution(object):
    def waysToSplitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur_sum = 0
        sum_nums=sum(nums)
        result=0
        for i in range(len(nums)-1):
            cur_sum += nums[i]
            if cur_sum >= sum_nums-cur_sum:
                result+=1

        return result
        