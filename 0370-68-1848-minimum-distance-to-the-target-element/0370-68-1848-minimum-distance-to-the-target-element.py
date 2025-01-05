class Solution(object):
    def getMinDistance(self, nums, target, start):
        """
        :type nums: List[int]
        :type target: int
        :type start: int
        :rtype: int
        """
        result = float('inf')
        for i in range(len(nums)):
            absolute = abs(i-start)
            if nums[i]==target and absolute < result :
                result = absolute

        return result
