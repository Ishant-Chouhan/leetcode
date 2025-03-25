class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        low=0
        high=len(numbers)-1
        while low<high:
            x=numbers[low]+numbers[high]
            if x > target:
                high-=1
            elif x < target:
                low+=1
            else:
                return [low+1,high+1]
        
