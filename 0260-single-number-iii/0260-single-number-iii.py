class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[]
        for i in set(nums):
            if len(ans)==2:
                break
            elif nums.count(i)==1:
                ans.append(i)
                
        return ans
                