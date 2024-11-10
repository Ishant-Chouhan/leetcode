# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if guess(n) == 0:
            return n
            
        high = n
        low = 1

        while True:
            num = (low + high) // 2
            if guess(num) == -1:
                high = num
            elif guess(num) == 1:
                low = num
            else:
                return num
                break
                
        