class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        for i in range(0,len(bits)):
            if bits[i]==1:
                bits[i+1]="_"
                bits[i]="_"
        return bits[-1]==0