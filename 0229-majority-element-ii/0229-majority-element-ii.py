class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) < 3:
            return list(set(nums))
        
        condition = len(nums)/3
        result = [i for i in set(nums) if nums.count(i) > condition]
        
                
        return result