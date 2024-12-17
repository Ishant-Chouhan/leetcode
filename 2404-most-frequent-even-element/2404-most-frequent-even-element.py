class Solution(object):
    def mostFrequentEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        result=None
        temp = list(set(nums))
        temp.sort(reverse = True)
        for i in temp:
            if i % 2 == 0 and nums.count(i) >= count :
                count = nums.count(i)
                result = i
                
        if result is None:
            return -1
        return result