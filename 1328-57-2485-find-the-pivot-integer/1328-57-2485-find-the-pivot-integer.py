class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        numsum=0
        for i in range(1,n+1):
            numsum+=i
        addition=0
        for i in range(1,n+1):
            addition+=i
            if addition==numsum+i-addition:
                return i
        else:
            return -1