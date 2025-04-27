class Solution(object):
    def countSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        for i in range(2,len(nums)):
            x=nums[i]+nums[i-2]
            if nums[i-1] == 2*x:
                count+=1

        return count