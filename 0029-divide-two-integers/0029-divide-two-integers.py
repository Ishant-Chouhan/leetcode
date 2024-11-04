class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend//divisor > 2**31 - 1:
            return 2**31 -1
        elif dividend//divisor < -2**31:
            return -2**31
        elif (dividend >= 0 and divisor < 0 ) or (dividend < 0 and divisor >=0) :
            return -1*(abs(dividend)//abs(divisor))
        return dividend//divisor 
    