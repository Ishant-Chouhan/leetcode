class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        i = 0
        integer = 0
        length = len(s)
        while i!= length:
            rom = d[s[i]]
            if i!= length-1 and rom < d[s[i+1]]:
                integer += d[s[i+1]] - rom
                i+=2
            else:
                integer += rom
                i+=1
                
        return integer
            

        