class Solution(object):
    def sumOfGoodNumbers(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        add=0
        for i in range(len(nums)):
            if i-k>=0 and i+k>=len(nums) and nums[i]> nums[i-k]:
                add+=nums[i]
            elif i-k<0 and i+k<len(nums) and nums[i]> nums[i+k]:
                add+=nums[i]
            elif (nums[i]> nums[i-k] and nums[i]>nums[i+k]) or (i-k<0 and i+k>=len(nums)) :
                add+=nums[i]

        return add