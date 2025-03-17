class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]=nums[i]*2
                nums[i+1]=0
        
        z_count=nums.count(0)

        i=0
        while i < len(nums):
            if nums[i]==0:
                nums.pop(i)
            else:
                i+=1

        nums.extend([0]*z_count)
        return nums