class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=[]
        for i in set(nums):
            ans.append(nums.count(i))
            
        return max(ans) * ans.count(max(ans))