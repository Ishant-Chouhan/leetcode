class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if target not in nums:
            return [-1,-1]
        left=nums.index(target)
        right=len(nums) - sorted(nums,reverse=True).index(target) - 1
        
        return [left,right]