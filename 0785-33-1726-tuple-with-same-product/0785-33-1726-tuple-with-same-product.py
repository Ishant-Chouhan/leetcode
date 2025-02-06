class Solution(object):
    def tupleSameProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d=dict()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                element=nums[i]*nums[j]
                if element not in d:
                    d[element]=1
                else:
                    d[element]+=1
        s=d.values()
        count=0
        for i in s:
            if i>=2:
                count+= i  * (i-1) * 4
        return count
                    