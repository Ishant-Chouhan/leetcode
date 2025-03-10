class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d={}
        for i in range(len(nums)):
            temp=nums[i]
            if temp not in d:
                d[temp] = i
            else:
                if abs(d[temp]-i) <= k:
                    return True
                else:
                    d[temp]=i
        else:
            return False