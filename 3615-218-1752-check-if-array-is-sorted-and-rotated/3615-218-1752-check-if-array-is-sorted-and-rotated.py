class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums==sorted(nums):
            return True
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                print(i)
                break
        
        return nums[i+1:len(nums)]+nums[0:i+1]==sorted(nums)