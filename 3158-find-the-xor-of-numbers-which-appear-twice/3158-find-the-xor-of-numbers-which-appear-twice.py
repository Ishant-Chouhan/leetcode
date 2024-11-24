class Solution(object):
    def duplicateNumbersXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        xor=0
        for i in set(nums):
            if nums.count(i)==2:
                xor = xor ^ i
        
        return xor
                