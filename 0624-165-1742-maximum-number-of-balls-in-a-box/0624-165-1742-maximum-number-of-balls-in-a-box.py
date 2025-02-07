class Solution(object):
    def countBalls(self, lowLimit, highLimit):
        """
        :type lowLimit: int
        :type highLimit: int
        :rtype: int
        """
        def num_sum(n):
            if n==0:
                return 0
            else:
                return n%10 + num_sum(int(n/10))

        result=dict()
        for i in range(lowLimit,highLimit+1):
            num = num_sum(i)
            if num in result:
                result[num]+=1
            else:
                result[num]=1

        return max(result.values())
