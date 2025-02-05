class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                if i+2==len(nums):
                    nums[i+1]=nums[i]
                elif nums[i]<nums[i+2]:
                    nums[i+1]=nums[i]
                else:
                    nums[i]=nums[i+1]
                break
        return nums==sorted(nums)