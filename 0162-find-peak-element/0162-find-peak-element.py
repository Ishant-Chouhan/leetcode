class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if sorted(nums) ==  nums or len(nums) <= 2 :
            return nums.index(max(nums))
        peak=0
        for i in range(1,len(nums)-1):
            if nums[i-1]<nums[i] and nums[i+1]<nums[i] and nums[i]>nums[peak]:
                peak=i

        return peak