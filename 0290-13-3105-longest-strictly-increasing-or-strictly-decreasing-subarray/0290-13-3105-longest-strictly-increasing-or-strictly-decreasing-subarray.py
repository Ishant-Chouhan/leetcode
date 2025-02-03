class Solution(object):
    def longestMonotonicSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        lencount=1
        result=list()
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                lencount+=1
            else:
                result.append(lencount)
                lencount=1
        result.append(lencount)
        nums=nums[::-1]
        lencount=1
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                lencount+=1
            else:
                result.append(lencount)
                lencount=1
        result.append(lencount)
         
        return max(result)
                