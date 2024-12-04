class Solution(object):
    def minimumSumSubarray(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: int
        :type r: int
        :rtype: int
        """
        min_sum=float('inf')
        j=0
        while l<=r:
            if j==len(nums):
                j=0
                l+=1
                continue
            elif len(nums[j:j+l])==l and sum(nums[j:j+l])>0 and sum(nums[j:j+l])<min_sum:
                min_sum=sum(nums[j:j+l])
            
            j+=1
            
        if min_sum==float('inf'):
            return-1
        return min_sum