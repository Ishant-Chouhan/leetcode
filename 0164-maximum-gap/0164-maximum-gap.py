class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        max_diff=0
        for i in range(len(nums)-1):
            max_diff=max(max_diff,nums[i+1]-nums[i])

        return max_diff
            
