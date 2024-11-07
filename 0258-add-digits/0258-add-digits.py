class Solution(object):
    def addDigits(self, num):
        while len(str(num)) != 1:
            n=num
            num = 0
            while n != 0:
                num += n%10
                n = n//10
                
        return num
        