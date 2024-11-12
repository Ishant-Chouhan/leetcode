class Solution(object):
    def isBalanced(self, num):
        """
        :type num: str
        :rtype: bool
        """
        even=0
        odd=0
        
        for i in range(len(num)):
            if i%2==0:
                even+=eval(num[i])
            else:
                odd+=eval(num[i])
                
        return even == odd
        