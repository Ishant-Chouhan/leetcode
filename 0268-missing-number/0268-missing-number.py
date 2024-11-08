class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #running loop upto 1+length of array since it is exclusive value
        for i in range(len(nums)+1):
            #checking weather i is present in array or not
            if i not in nums:
                
                return i 
        