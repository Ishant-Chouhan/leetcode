class Solution(object):
    def isPossibleToSplit(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in set(nums):
            if nums.count(i) <=2:
                continue
            return False
        else:
            return True