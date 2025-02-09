class Solution(object):
    def countBadPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        check=dict()
        n=len(nums)
        tp= (n-1)*n/2
        answer=0
        for i in range(len(nums)):
            x = i - nums[i]
            print(x)
            if x in check:
                tp -= check[x]
                check[x]+=1
            else:
                check[x]=1

        return tp-answer