class Solution(object):
    def numberOfPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [0,0]
        for i in set(nums):
            counts=nums.count(i)
            result[0] += counts // 2
            result[1] += counts % 2

        return result

        