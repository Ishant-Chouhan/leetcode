class Solution(object):
    def maxAscendingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum=0
        j=0
        for i in range(len(nums)):
            if i==len(nums)-1:
                max_sum = max(max_sum,sum(nums[j:i+1]))
                break
            elif nums[i]>=nums[i+1]:
                max_sum = max(max_sum,sum(nums[j:i+1]))
                j=i+1


        return max_sum
