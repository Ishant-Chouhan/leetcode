class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if sum(nums[1:len(nums)])==0 or len(nums)==1:
                return 0
        for i in range(1,len(nums)):
            if sum(nums[0:i]) == sum(nums[i+1:len(nums)]):
                return i
        else:
            return -1