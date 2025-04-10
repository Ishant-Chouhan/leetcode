class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        operations=0
        for i in range(0,len(nums),3):
            if len(nums[i:len(nums)])==len(set(nums[i:len(nums)])):
                return operations
            operations+=1
        
        return operations