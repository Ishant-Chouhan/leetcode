class Solution(object):
    def missingInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j = 1
        s=nums[0]
        while j < len(nums) and  nums[j] == nums[j-1] + 1  :
            s+=nums[j]
            j+=1
        while s in nums:
            s+=1
            
        return s
        