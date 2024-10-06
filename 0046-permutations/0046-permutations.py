from itertools import permutations as perm
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return [list(i) for i in perm(nums)]
        