class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=1:
            return len(nums)
        
        k,i=1,1
        while i<len(nums):
            
            if nums[i]==nums[i-1] and nums[i]!="_":
                nums.pop(i) 
            else:
                k+=1
                i+=1

        return k

