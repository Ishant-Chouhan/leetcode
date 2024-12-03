class Solution:
    def maximumTop(self, nums,k):
        if len(nums) == 1:
            if k%2 != 0:
                return -1
            return nums[0]
        
        if k == 0:
            return nums[0]
        if k == len(nums):
            return max(nums[:-1])
        if k > len(nums):
            return max(nums)
        if k == 1:
            return nums[1]
        m = max(max(nums[:k-1]), nums[k])
        return m